from ortools.sat.python import cp_model
import random
from src.schedule.model import Customers, Employees, Schedule

def create_new_schedule(version: str, customers: Customers, employees: Employees) -> Schedule:
    # -------------------------------------------------------------------------
    # 1. Data Setup
    # -------------------------------------------------------------------------
    # We define the shift length to calculate total hours. 
    # Let's assume a standard shift is 6 hours for this example to make the math clean 
    # (e.g., 30 hours = 5 shifts).
    num_days = 7

    # -------------------------------------------------------------------------
    # 2. Model Initialization
    # -------------------------------------------------------------------------
    model = cp_model.CpModel()

    # Decision Variables: 
    # work[(employee_id, customer, day)] is true (1) if employee works that shift, else false (0)
    work = {}
    for e in employees.employees:
        for c in customers.customers:
            for d in range(num_days):
                if c.service_type in e.skills and c.weekly_hours > 0:
                    work[(e.id, c.id, d)] = model.NewBoolVar(f"work_e{e.id}_c{c.id}_d{d}")

    # -------------------------------------------------------------------------
    # 3. Constraints
    # -------------------------------------------------------------------------

    # A. No overlaping employer
    # This prevents an employee from working two companies at the same time.
    for e in employees.employees:
        for d in range(num_days):
            shifts_in_day = []
            for c in customers.customers:
                shift = work.get((e.id, c.id, d))
                if shift is not None:
                    shifts_in_day.append(shift)
            if shifts_in_day:
                model.Add(sum(shifts_in_day) <= 1)

    # B. Contract Hours Requirement
    # Sum of all shifts worked * duration <= contract_hours
    # We use a scaling factor to handle float hours in CP-SAT (which requires integers)
    SCALING_FACTOR = 10 
    
    for e in employees.employees:
        employee_max_week_hours = int(e.employment_rate * SCALING_FACTOR)
        shifts_with_duration = []
        for c in customers.customers:
            for d in range(num_days):
                shift = work.get((e.id, c.id, d))
                if shift is not None:
                    # Duration of this specific shift
                    duration = int(c.weekly_hours * SCALING_FACTOR)
                    shifts_with_duration.append(shift * duration)

        if shifts_with_duration:
            model.Add(sum(shifts_with_duration) <= employee_max_week_hours)

    # C. Customer Demand Requirement
    # Sum of shifts for a customer * duration <= customer_hours_per_week
    for c in customers.customers:
        customer_shifts = []
        duration = int(c.weekly_hours * SCALING_FACTOR)
        limit = int(c.weekly_hours * SCALING_FACTOR)
        
        for e in employees.employees:
            for d in range(num_days):
                shift = work.get((e.id, c.id, d))
                if shift is not None:
                     customer_shifts.append(shift * duration)
        
        if customer_shifts:
            # We use <= to ensure we don't over-schedule. 
            # Since we maximize shifts, the solver will try to get as close to the limit as possible.
            # We allow a small buffer? No, let's try strict first.
            model.Add(sum(customer_shifts) <= limit)

    # -------------------------------------------------------------------------
    # 4. Solver
    # -------------------------------------------------------------------------
    # Objective: Maximize the number of shifts assigned
    # We could also maximize hours, but maximizing shifts is a good proxy if shifts are similar.
    # To maximize hours: model.Maximize(sum(shift * int(c.hours_per_day * SCALING_FACTOR) for (e_id, c_id, d, p), shift in work.items()))
    # But we need to lookup c.hours_per_day.
    # Let's just maximize shifts for now as a simple start.
    model.Maximize(sum(work.values()))

    solver = cp_model.CpSolver()
    # Optional: Randomize search to get different valid schedules each run
    solver.parameters.random_seed = random.randint(0, 100)
    #solver.parameters.log_search_progress = True
    solver.parameters.max_time_in_seconds = 60.0
    
    status = solver.Solve(model)

    # -------------------------------------------------------------------------
    # 5. Output
    # -------------------------------------------------------------------------
    if status not in [cp_model.OPTIMAL, cp_model.FEASIBLE]:
        raise Exception("No solution found. Check if the required hours fit into the available slots.")
    
    # Iterate through time to print the schedule chronologically
    schedule = []
    for d in range(num_days):
        for e in employees.employees:
            for c in customers.customers:
                shift = work.get((e.id, c.id, d))
                if shift is not None and solver.Value(shift):
                    schedule.append(Schedule(
                        version=version,
                        employee_id=str(e.id),
                        customer_id=str(c.id),
                        week_day=d,
                        period=c.shift_requirement,
                        hours_per_day=c.daily_hours,
                        
                    ))
    return schedule
