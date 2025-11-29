from ortools.sat.python import cp_model
from parse import parse_employees, parse_customers
import random

def main():
    # -------------------------------------------------------------------------
    # 1. Data Setup
    # -------------------------------------------------------------------------
    
    customers = parse_customers()
    employees = parse_employees()

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
                if c.service in e.get_skills() and c.hours_per_week > 0:
                    work[(e.id, c.customer_id, d)] = model.NewBoolVar(f"work_e{e.id}_c{c.customer_id}_d{d}")

    # -------------------------------------------------------------------------
    # 3. Constraints
    # -------------------------------------------------------------------------

    # A. No overlaping employer
    # This prevents an employee from working two companies at the same time.
    for e in employees.employees:
        for d in range(num_days):
            shifts_in_day = []
            for c in customers.customers:
                shift = work.get((e.id, c.customer_id, d))
                if shift is not None:
                    shifts_in_day.append(shift)
            if shifts_in_day:
                model.Add(sum(shifts_in_day) <= 1)

    # B. Contract Hours Requirement
    # Sum of all shifts worked * duration <= contract_hours
    # We use a scaling factor to handle float hours in CP-SAT (which requires integers)
    SCALING_FACTOR = 10 
    
    for e in employees.employees:
        employee_max_week_hours = int(e.get_hours_week() * SCALING_FACTOR)
        shifts_with_duration = []
        for c in customers.customers:
            for d in range(num_days):
                shift = work.get((e.id, c.customer_id, d))
                if shift is not None:
                    # Duration of this specific shift
                    duration = int(c.hours_per_day * SCALING_FACTOR)
                    shifts_with_duration.append(shift * duration)

        if shifts_with_duration:
            model.Add(sum(shifts_with_duration) <= employee_max_week_hours)

    # C. Customer Demand Requirement
    # Sum of shifts for a customer * duration <= customer_hours_per_week
    for c in customers.customers:
        customer_shifts = []
        duration = int(c.hours_per_day * SCALING_FACTOR)
        limit = int(c.hours_per_week * SCALING_FACTOR)
        
        for e in employees.employees:
            for d in range(num_days):
                shift = work.get((e.id, c.customer_id, d))
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
        print("No solution found. Check if the required hours fit into the available slots.")
        return
    print("Solution Found!\n")
    print(f"{'Employee':<20} | {'Customer':<35} | {'Day':<2} | {'Period':<10} | {'Hours':<5}")
    print("-" * 70)

    # Iterate through time to print the schedule chronologically
    for d in range(num_days):
        for e in employees.employees:
            for c in customers.customers:
                shift = work.get((e.id, c.customer_id, d))
                if shift is not None and solver.Value(shift):
                    print(f"{e.name:<20} | {c.customer_name:<35} | {d:<2} | {c.required_period:<10} | {c.hours_per_day:<5}")
        print("-" * 70) # Separator between days

    print("\nCustomer Summary:")
    for c in customers.customers:
        total_hours_scheduled = 0
        for e in employees.employees:
            for d in range(num_days):
                shift = work.get((e.id, c.customer_id, d))
                if shift is not None and solver.Value(shift):
                    total_hours_scheduled += c.hours_per_day
        
        if total_hours_scheduled > 0:
            print(f"{c.customer_name} ({c.service}): {total_hours_scheduled} hours scheduled (Goal: {c.hours_per_week})")

    print("\nEmployee Summary:")
    for e in employees.employees:
        total_hours_scheduled = 0
        for c in customers.customers:
            for d in range(num_days):
                shift = work.get((e.id, c.customer_id, d))
                if shift is not None and solver.Value(shift):
                    total_hours_scheduled += c.hours_per_day
        
        if total_hours_scheduled > 0:
            print(f"{e.name} ({e.position}): {total_hours_scheduled} hours scheduled (Goal: {e.get_hours_week()})")

if __name__ == '__main__':
    main()