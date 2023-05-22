import datetime 
import helper
# print(helper.Month[date.today().month - 1])

week = datetime.timedelta(days=7)
today = datetime.date.today()
exitDate_unformatted = today + week

exitDate = f"{exitDate.day}-{helper.Month[exitDate.month - 1]}-{exitDate.year}"

with open("holidays") as holidays:
    lines = holidays.readlines()

for i,line in enumerate(lines):
    lines[i] = line.strip()
    
