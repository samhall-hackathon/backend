import csv
from model import Customer
customer_list: list[Customer] = []


with open('Kundplaneringsdata_a.csv', newline='') as csvfile:
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


print(customer_list)