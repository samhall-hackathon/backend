from pydantic import BaseModel, Field

class Customer(BaseModel):
    """
    Entity representing customer and its requirements
    """
    customer_id: str = Field(description="ID of the customer")
    customer_name: str = Field(description="Name of the customer")
    required_period: str = Field(description="required period")
    hours_per_week: float = Field(description="Amount of hours per week")
    hours_per_day: float = Field(description="Hours per day")
    days_per_week: int = Field(description="Days per week needed")
    amount_of_FTE: float = Field(description="Amount of fulltime employees needed")
    
    group: str = Field(description="Group beloning")
    service: str = Field(description="Type of service needed")

class Employee(BaseModel):
    """
    Entity representing an employee
    """
    id: str = Field(description="ID of the employee")
    name: str = Field(description="Name of the employee")
    working_hours_per_week: float = Field(description="Working hours per week for the employee")
    position: str = Field(description="Position")
    competence_ratio: float = Field(description="Maximum working hours per day for the employee")
    group: str = Field(description="Days the employee is available to work")

    def get_hours_week(self) -> float:
        """
        Returns the amount of hours the employee is working per week
        """
        return self.working_hours_per_week * 40
    
    def get_skills(self) -> list[str]:
        """
        Returns the skills of the employee
        """
        return self.position.split(',')


class Employees(BaseModel):
    """
    Entity representing a list of employees
    """
    employees: list[Employee] = []
    
    def get_all_groups(self) -> list[str]:
        """
        Returns a list of all groups the employees are available to work
        """
        return list(set([e.group for e in self.employees]))

    def get_all_skills(self) -> list[str]:
        """
        Returns a list of all skills the employees are available to work
        """
        return list(set([e.position for e in self.employees]))

class Customers(BaseModel):
    """
    Entity representing a list of customers
    """
    customers: list[Customer] = []
    
    def get_all_periods(self) -> list[str]:
        """
        Returns a list of all periods the customers are available to work
        """
        return list(set([c.required_period for c in self.customers]))
