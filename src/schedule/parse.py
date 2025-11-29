import csv
from model import Customer, Employee, Customers, Employees

def parse_customers() -> Customers: 
    customer_list: list[Customer] = []
    with open('static/Kundplaneringsdata_a.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')

        for row in reader:
            id, name = row['Kundobjekt'].split(' - ')
            customer_list.append(Customer(
                customer_id=id,
                customer_name=name,
                required_period=row['Krav på tider'],
                hours_per_week=float(row['Behov per vecka i timmar'].replace(',', '.')),
                hours_per_day=float (row['Behov per dag timmar'].replace(',', '.')),
                days_per_week=row['Antal dagar i veckan'],
                amount_of_FTE=float (row['Antal heltidsekvivalenter'].replace(',', '.')),
                group=row['Gruppering'],
                service=row['Tjänst']
            ))
    return Customers(customers=customer_list)


def parse_employees() -> Employees: 
    employee_list: list[Employee] = []
    with open('static/Medarbetare.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')

        for row in reader:
            employee_list.append(Employee(
                id=row['Anställningsnummer'],
                name=row['Namn'],
                working_hours_per_week=float(row['Anställningsgrad'].replace(',', '.')),
                position=row['Kompetenser'],
                competence_ratio=float(row['Kapacitetsfaktor'].replace(',', '.')),
                group=row['Grupp']
            ))
    return Employees(employees=employee_list)
