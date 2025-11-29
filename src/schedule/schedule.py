from ortools.sat.python import cp_model
from parse import parse_employees, parse_customers
import logging
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
    #start_hour, end_hour = 6, 24
    #hours_per_day = end_hour - start_hour # day starts at 6 and finishes at 24
    
    # Shifts per day (0: Morning, 1: Afternoon)
    periods = customers.get_all_periods()
    #num_shifts = len(shifts)

    # -------------------------------------------------------------------------
    # 2. Model Initialization
    # -------------------------------------------------------------------------
    model = cp_model.CpModel()

    # Decision Variables: 
    # work[(employee_id, customer, day, hour, skill)] is true (1) if employee works that shift, else false (0)
    work = {}
    for e in employees.employees:
        for c in customers.customers:
            for d in range(num_days):
                # filter by period required from customer
                for p in periods:
                    # filter by skills
                    if c.service in e.get_skills():
                        work[(e.id, c.customer_id, d, p)] = model.NewBoolVar(f"work_e{e.id}_c{c.customer_id}_d{d}_p{p}")

    logging.info(f"Assembling decision variables")
    # -------------------------------------------------------------------------
    # 3. Constraints
    # -------------------------------------------------------------------------

    # A. No Overlapping Shifts (At most one shift per day per employee)
    # This prevents an employee from working Morning AND Afternoon on the same day.
    # If double shifts are allowed, remove this constraint.
    for e in employees.employees:
        for c in customers.customers:
            for d in range(num_days):
                for p in periods:
                    shift = work.get((e.id, c.customer_id, d, p))
                    if shift is not None:
                        model.AddAtMostOne(shift)


    # B. No overlaping employer
    # This prevents an employee from working two companies at the same time.
    for e in employees.employees:
        for c in customers.customers:
            for d in range(num_days):
                for p in periods:
                    shift = work.get((e.id, c.customer_id, d, p))
                    if shift is not None:
                        model.Add(shift == 0)

    # C. Contract Hours Requirement
    # Sum of all shifts worked * duration == contract_hours
    #for e in employees.employees:
    #    employee_max_week_hours = e.get_hours_week()
    #    employee_shifts = []
    #    for c in customers.customers:
    #        for d in range(num_days):
    #            for p in periods:
    #                shift = work.get((e.id, c.customer_id, d, p))
    #                if shift is not None:
    #                    employee_shifts.append(shift)

    #    model.Add(sum(employee_shifts) <= int(employee_max_week_hours))

    # -------------------------------------------------------------------------
    # 4. Solver
    # -------------------------------------------------------------------------
    solver = cp_model.CpSolver()
    # Optional: Randomize search to get different valid schedules each run
    solver.parameters.random_seed = random.randint(0, 100)
    
    status = solver.Solve(model)

    # -------------------------------------------------------------------------
    # 5. Output
    # -------------------------------------------------------------------------
    if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
        print("Solution Found!\n")
        print(f"{'Employee_id':<10} | {'Customer_id':<10} | {'Day':<10} | {'Period':<10}")
        print("-" * 55)

        # Iterate through time to print the schedule chronologically
        for d in range(num_days):
            for p in periods:
                for e in employees.employees:
                    for c in customers.customers:
                        shift = work.get((e.id, c.customer_id, d, p))
                        if shift is not None and solver.Value(shift):
                            print(shift)
            print("-" * 55) # Separator between days

        print("\nSummary:")
        for c in customers.customers:
            for e in employees.employees:
                shifts_assigned = 0
                for d in range(num_days):
                    for p in periods:
                        shift = work.get((e.id, c.customer_id, d, p))
                        if shift is not None and solver.Value(shift):
                            shifts_assigned += 1
                    if shifts_assigned > 0:
                        print(f"{c.customer_name} ({c.service}): {shifts_assigned * 3} hours scheduled (Goal: {c.hours_per_week})")

    else:
        print("No solution found. Check if the required hours fit into the available slots.")

if __name__ == '__main__':
    main()