# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 23:44:39 2020

@author: Vishal
"""


from ibapi.client import EClient
from ibapi.wrapper import EWrapper
from ibapi.contract import Contract
from threading import Timer
import datetime as dt
import pandas as pd

class strategy(EClient, EWrapper):
    
    def __init__(self):
        EClient.__init__(self, self)
        
    def tickPrice(self, reqId, tickType, price, attrib):
        print(f'Id: {reqId}, TickType: {tickType}, Price: {price}')
        print(dt.datetime.now())
        
   
        
        
app = strategy()


app.connect(host='127.0.0.1', port=7496, clientId=1)
print(app.isConnected()) 

eurusd_contract = Contract()




eurusd_contract.symbol = 'BANKNIFTY'
eurusd_contract.currency = 'INR'
eurusd_contract.secType = 'IND'
eurusd_contract.exchange = 'NSE'
'''
eurusd_contract.symbol = 'EUR'
eurusd_contract.currency = 'USD'
eurusd_contract.secType = 'CASH'
eurusd_contract.exchange = 'IDEALPRO'


eurusd_contract.symbol = 'RELIANCE'
eurusd_contract.currency = 'INR'
eurusd_contract.secType = 'STK'
eurusd_contract.exchange = 'NSE'
'''
reqId = 7

app.reqMktData(reqId = reqId, 
               contract = eurusd_contract, 
               genericTickList = '', 
               snapshot = False, 
               regulatorySnapshot = False, 
               mktDataOptions = [])

Timer(15, app.cancelMktData, [reqId]).start()

Timer(20, app.disconnect).start()

app.run()       
        