from ortools.sat.python import cp_model
from parse import parse_employees

def main():
    # -------------------------------------------------------------------------
    # 1. Data Setup
    # -------------------------------------------------------------------------
    
    # We define the shift length to calculate total hours. 
    # Let's assume a standard shift is 6 hours for this example to make the math clean 
    # (e.g., 30 hours = 5 shifts).
    SHIFT_DURATION_HOURS = 8
    
    # Days of the week
    days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    num_days = len(days)
    
    # Shifts per day (0: Morning, 1: Afternoon)
    shifts = ['Morning', 'Afternoon']
    num_shifts = len(shifts)

    # Employee Data
    # We map the data from your request here.
    employees = parse_employees()

    # -------------------------------------------------------------------------
    # 2. Model Initialization
    # -------------------------------------------------------------------------
    model = cp_model.CpModel()

    # Decision Variables: 
    # work[(employee_id, day, shift)] is true (1) if employee works that shift, else false (0)
    work = {}
    for e in employees:
        for d in range(num_days):
            for s in range(num_shifts):
                work[(e['id'], d, s)] = model.NewBoolVar(f"work_e{e['id']}_d{d}_s{s}")

    # -------------------------------------------------------------------------
    # 3. Constraints
    # -------------------------------------------------------------------------

    # A. No Overlapping Shifts (At most one shift per day per employee)
    # This prevents an employee from working Morning AND Afternoon on the same day.
    # If double shifts are allowed, remove this constraint.
    for e in employees:
        for d in range(num_days):
            model.AddAtMostOne(work[(e['id'], d, s)] for s in range(num_shifts))

    # B. Contract Hours Requirement
    # Sum of all shifts worked * duration == contract_hours
    for e in employees:
        total_shifts_worked = sum(
            work[(e['id'], d, s)] for d in range(num_days) for s in range(num_shifts)
        )
        
        # Calculate target number of shifts (e.g., 30 hours / 6 hours per shift = 5 shifts)
        # Note: If hours aren't perfectly divisible, you might want to use a range (>= min, <= max)
        target_shifts = e['contract_hours'] // SHIFT_DURATION_HOURS
        
        model.Add(total_shifts_worked == target_shifts)

    # -------------------------------------------------------------------------
    # 4. Solver
    # -------------------------------------------------------------------------
    solver = cp_model.CpSolver()
    # Optional: Randomize search to get different valid schedules each run
    solver.parameters.random_seed = 42 
    
    status = solver.Solve(model)

    # -------------------------------------------------------------------------
    # 5. Output
    # -------------------------------------------------------------------------
    if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
        print("Solution Found!\n")
        print(f"{'Day':<10} | {'Shift':<10} | {'Employee':<15} | {'Position'}")
        print("-" * 55)

        # Iterate through time to print the schedule chronologically
        for d in range(num_days):
            for s in range(num_shifts):
                for e in employees:
                    if solver.Value(work[(e['id'], d, s)]):
                        print(f"{days[d]:<10} | {shifts[s]:<10} | {e['name']:<15} | {e['position']}")
            print("-" * 55) # Separator between days

        print("\nSummary:")
        for e in employees:
            shifts_assigned = 0
            for d in range(num_days):
                for s in range(num_shifts):
                    if solver.Value(work[(e['id'], d, s)]):
                        shifts_assigned += 1
            print(f"{e['name']} ({e['position']}): {shifts_assigned * SHIFT_DURATION_HOURS} hours scheduled (Goal: {e['contract_hours']})")

    else:
        print("No solution found. Check if the required hours fit into the available slots.")

if __name__ == '__main__':
    main()