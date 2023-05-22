import datetime 
import helper
# print(helper.Month[date.today().month - 1])


with open("holidays") as holidays:
    lines = holidays.readlines()

for i,line in enumerate(lines):
    lines[i] = line.strip()

gotExitDate = False
exitDate = None
d = 7
today = datetime.date.today()
while not gotExitDate:
    week = datetime.timedelta(days=d)
    exitDate_unformatted = today + week
    exitDate = f"{'{0:02d}'.format(exitDate_unformatted.day)}-{helper.Month[exitDate_unformatted.month - 1]}-{exitDate_unformatted.year}"
    print(exitDate)
    if exitDate not in lines:
        gotExitDate = True
    else:
        d -= 1