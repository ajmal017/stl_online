# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 23:44:39 2020

@author: Vishal
"""


from ibapi.client import EClient
from ibapi.wrapper import EWrapper
from ibapi.contract import Contract
from threading import Timer
import pandas as pd

class strategy(EClient, EWrapper):
    
    def __init__(self):
        EClient.__init__(self, self)
        self.df = pd.DataFrame(columns=['Time', 'Open', 'Close'])

    def historicalData(self, reqId, bar):
        dictionary = {'Time':bar.date, 'Open':bar.open, 'Close':bar.close}
        self.df = self.df.append(dictionary, ignore_index=True) 
        print(f'Time:{bar.date}, Open:{bar.open}, Close:{bar.close}')

    def historicalDataEnd(self, reqId, start, end):
        print('\nData Received End\n')
        print(self.df.head())
        
        
app = strategy()


app.connect(host='127.0.0.1', port=7496, clientId=1)
print(app.isConnected()) 

eurusd_contract = Contract()



'''
eurusd_contract.symbol = 'MSFT'
eurusd_contract.currency = 'USD'
eurusd_contract.secType = 'STK'
eurusd_contract.exchange = 'SMART'


eurusd_contract.symbol = 'EUR'
eurusd_contract.currency = 'USD'
eurusd_contract.secType = 'CASH'
eurusd_contract.exchange = 'IDEALPRO'
'''

eurusd_contract.symbol = 'RELIANCE'
eurusd_contract.currency = 'INR'
eurusd_contract.secType = 'STK'
eurusd_contract.exchange = 'NSE'

app.reqHistoricalData(reqId=11, 
                      contract=eurusd_contract,
                      endDateTime = '',
                      durationStr = '1 D',
                      barSizeSetting = '15 mins',
                      whatToShow = 'MIDPOINT',
                      useRTH = 0,
                      formatDate = 1,
                      keepUpToDate = False,
                      chartOptions = [])

Timer(10, app.disconnect).start()

app.run()       
        