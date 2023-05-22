from smartapi import SmartConnect
import helper
import datetime
api = SmartConnect(api_key='zYJrbBfd')

api.generateSession('P892158', '5542', '015448')

data = api.ltpData("NSE", "NIFTY", "26000")
ltp = data['data']['ltp']
print("ltp=", ltp)
const = 250
base = 50
ce1 = helper.roundUp(ltp + 250, base)
pe1 = helper.roundDown(ltp - 250, base)

ce2 = helper.roundUp(ltp + (2 * 250), base)
pe2 = helper.roundDown(ltp - (2 * 250), base)


with open("holidays") as holidays:
    lines = holidays.readlines()

for i,line in enumerate(lines):
    lines[i] = line.strip()

gotExitDate = False
exitDate = None
exitDate_unformatted = None
d = 7
today = datetime.date.today()
while not gotExitDate:
    week = datetime.timedelta(days=d)
    exitDate_unformatted = today + week
    exitDate = f"{'{0:02d}'.format(exitDate_unformatted.day)}-{helper.Month[exitDate_unformatted.month - 1]}-{exitDate_unformatted.year}"
    if exitDate not in lines:
        gotExitDate = True
    else:
        d -= 1

edu = exitDate_unformatted
#sell ce1 pe1
#buy ce2 pe2

#sell
#eg NIFTY11AUG2216850PE.NFO
ce1_ticker = f"NIFTY{edu.day}{helper.Month[edu.month - 1]}{str(edu.year)[-2:]}{ce1}.NFO"
pe1_ticker = f"NIFTY{edu.day}{helper.Month[edu.month - 1]}{str(edu.year)[-2:]}{pe1}.NFO"
#buy
ce2_ticker = f"NIFTY{edu.day}{helper.Month[edu.month - 1]}{str(edu.year)[-2:]}{ce2}.NFO"
pe2_ticker = f"NIFTY{edu.day}{helper.Month[edu.month - 1]}{str(edu.year)[-2:]}{pe2}.NFO"

print("sell:", ce1_ticker, pe1_ticker)
print("buy:", ce2_ticker, pe2_ticker)