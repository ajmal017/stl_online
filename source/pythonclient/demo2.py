# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 23:44:39 2020

@author: Vishal
"""


from ibapi.client import EClient
from ibapi.wrapper import EWrapper
from ibapi.contract import Contract
from threading import Timer


class strategy(EClient, EWrapper):
    
    def __init__(self):
        EClient.__init__(self, self)

    def contractDetails(self, reqId, contractDetails):
        print('\nReqId: ', reqId, '\nContract Detail: ', contractDetails)
        
    def contractDetailsEnd(self, reqId):
        print('\nReqId: ', reqId, 'Contract detail Ended.')
        

app = strategy()


app.connect(host='127.0.0.1', port=7496, clientId=1)
print(app.isConnected()) 

eurusd_contract = Contract()



'''
eurusd_contract.symbol = 'MSFT'
eurusd_contract.currency = 'USD'
eurusd_contract.secType = 'STK'
eurusd_contract.exchange = 'SMART'
'''

eurusd_contract.symbol = 'EUR'
eurusd_contract.currency = 'USD'
eurusd_contract.secType = 'CASH'
eurusd_contract.exchange = 'IDEALPRO'

app.reqContractDetails(reqId=11, contract=eurusd_contract)

Timer(10, app.disconnect).start()

app.run()       
        