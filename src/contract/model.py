from pydantic import BaseModel, Field

from datetime import time

class Contract(BaseModel):
    """
    """
    company_name: str = Field(description="Name of the customer company")
    position: str = Field(description="required services")
    position_english: str = Field(description="required services, but in english")
    weekly_hours: int = Field(description="Amount of hours per week")
    days_of_the_week: list[int] = Field(description="Days of the week in number, where Monday is 0 and Sunday is 6 and so on")
    start_shift_time: time = Field(description="Start time of the shift")
    end_shifttime: time = Field(description="End time of the shift")
    
    start_date_contract: str = Field(description="Start date of the contract")
    end_date_contract: str = Field(description="End date of the contract")
    noticed_period: int = Field(description="Notice period in months")


contract_prompt = """
This is a service agreement with description of contract between a person and a company.
"""