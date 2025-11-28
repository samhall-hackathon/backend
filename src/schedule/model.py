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