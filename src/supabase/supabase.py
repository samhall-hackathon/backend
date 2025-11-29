import os
from supabase import create_client, Client
from src.schedule.model import Schedule, Employee, Customer

class SupabaseClient:
    def __init__(self, url: str, key: str):
        self.supabase: Client = create_client(url, key)

    def get_latest_schedule_version(self) -> int:
        """
        Queries the latest version of the schedule from the database.
        Returns 0 if no schedule exists.
        """
        response = (
            self.supabase.table("schedule")
            .select("version")
            .order("version", desc=True)
            .limit(1)
            .execute()
        )
        
        if response.data:
            return response.data[0]["version"]
        return 0

    def write_schedule(self, schedules: list[Schedule]) -> None:
        """
        Writes a list of schedules to the database in a single batch.
        """
        if not schedules:
            return

        data = [schedule.model_dump() for schedule in schedules]
        self.supabase.table("schedule").insert(data).execute()
    
    def get_last_schedule(self) -> list[Schedule] | None:
        """
        Returns the last schedule from the database.
        """
        latest_version = self.get_latest_schedule_version()
        response = (
            self.supabase.table("schedule")
            .select("*")
            .eq("version", latest_version)
            .execute()
        )
        
        if response.data:
            return [Schedule(**schedule) for schedule in response.data]
        return None

    def get_all_employes(self) -> list[Employee]:
        """
        Returns a list of all employees from the database.
        """
        response = self.supabase.table("employees").select("*").execute()
        return [Employee(**employee) for employee in response.data]

    def get_all_customers(self) -> list[Customer]:
        """
        Returns a list of all customers from the database.
        """
        response = self.supabase.table("customers").select("*").execute()
        return [Customer(**customer) for customer in response.data]

