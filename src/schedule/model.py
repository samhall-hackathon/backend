from pydantic import BaseModel, Field
import uuid

class Customer(BaseModel):
    """
    Entity representing customer and its requirements
    """
    id: uuid.UUID = Field(description="ID of the customer")
    company_name: str = Field(description="Name of the customer")
    shift_requirement: str = Field(description="required period")
    weekly_hours: float = Field(description="Amount of hours per week")
    daily_hours: float = Field(description="Hours per day")
    days_per_week: int = Field(description="Days per week needed")
    fte: float = Field(description="Amount of fulltime employees needed")
    days_of_week: list[str] = Field(description="Days the customer requires work")
    region: str = Field(description="Group beloning")
    service_type: str = Field(description="Type of service needed")

class Employee(BaseModel):
    """
    Entity representing an employee
    """
    id: uuid.UUID = Field(description="ID of the employee")
    name: str = Field(description="Name of the employee")
    employment_rate: float = Field(description="Working hours per week for the employee")
    skills: list[str] = Field(description="Position")
    capacity_factor: float = Field(description="Maximum working hours per day for the employee")
    #group: str = Field(description="Days the employee is available to work")

    def get_hours_week(self) -> float:
        """
        Returns the amount of hours the employee is working per week
        """
        return self.employment_rate * 40
    
    def get_skills(self) -> list[str]:
        """
        Returns the skills of the employee
        """
        return self.skills


class Schedule(BaseModel):
    """
    Entity representing a schedule
    """
    version: int = Field(description="Version of the schedule")
    customer_id: str = Field(description="ID of the customer")
    employee_id: str = Field(description="ID of the employee")
    week_day: int = Field(description="Day of the week")
    period: str = Field(description="Period of the day")
    hours_per_day: float = Field(description="Hours worked per day")

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
