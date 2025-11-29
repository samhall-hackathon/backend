from fastapi import FastAPI, File
from typing import Annotated
from src.contract.contract import parse_contract
from src.contract.model import Contract
import magic
from src.schedule.schedule import create_new_schedule
from src.supabase.supabase import SupabaseClient
from src.schedule.model import Schedule, Employees, Customers
import os
app = FastAPI()


supabase = SupabaseClient(
    os.getenv("SUPABASE_URL"),
    os.getenv("SUPABASE_KEY")
)

@app.get("/")
def root():
    return {"message": "Hello World"}


@app.post("/contract", response_model=Contract)
def contract(file: Annotated[bytes, File()]):
    mime = magic.Magic(mime=True)
    return parse_contract(file, mime.from_buffer(file))

@app.post("/schedule", status_code=201)
def schedule():
    """
    Creates a new schedule based on the latest contract.
    """
    import pdb; pdb.set_trace()
    employees = supabase.get_all_employes()
    customers = supabase.get_all_customers()

    latest_version = supabase.get_latest_schedule_version()
    new_version = latest_version + 1

    schedule = create_new_schedule(new_version, Customers(customers=customers), Employees(employees=employees))
    supabase.write_schedule(schedule)

    return schedule


@app.get("/schedule", response_model=list[Schedule])
def get_schedule():
    return supabase.get_last_schedule()