from smartapi import SmartConnect
import helper
from datetime import date

print(date.today())
api.generateSession('P892158', '5542', '838285')
# api = SmartConnect(
# api.generateSession('P892158', '5542', '696317')
# )
# api.generateSession('P892158', '5542', '165412')

# data = api.ltpData("NSE", "NIFTY", "26000")
# ltp = data['data']['ltp']
# print(ltp)
# const = 250
# base = 50
# ce1 = helper.roundUp(ltp + 250, base)
# pe1 = helper.roundDown(ltp - 250, base)

# #sell
# print(f"sell {ce1} ")


# #buy

# ce2 = helper.roundUp(ltp + (2 * 250), base)
# pe2 = helper.roundDown(ltp - (2 * 250), base)


