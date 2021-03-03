#!C:\Users\WinWinTrader\AppData\Local\Programs\Python\Python38\python.exe

from kiteconnect import KiteConnect
import acctkn

att=acctkn.att()
ap=acctkn.atp()

kite = KiteConnect(api_key=ap)
kite.set_access_token(att)
print('Successfully logged in Kite API!, WOW Great Achievement!')

stock_to_chck_LTP = 'INFY'

while True:
 #quote_date = kite.quote(['NSE:'+stock_to_chck_LTP]['ohlc'])['ohlc']
 quote_date = kite.quote('NSE:{}'.format(stock_to_chck_LTP))
 ohl=quote_date['NSE:{}'.format(stock_to_chck_LTP)]['ohlc']
 print('printing OHL:',ohl)

exit()