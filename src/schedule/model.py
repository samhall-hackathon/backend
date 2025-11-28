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
