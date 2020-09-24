
"""
Created on Tue Aug 25 14:37:19 2020

@author: Vishal
"""

from ibapi.client import EClient
from ibapi.wrapper import EWrapper
from ibapi.contract import Contract
from threading import Timer
import datetime as dt
import pandas as pd

atm_strike = 24000

class strategy(EClient, EWrapper):
    
    global atm_strike
    
    def __init__(self):
        self.atm_flag = False
        self.PEtrade = False
        self.CEtrade = False
        self.CEsellPrice = 0
        self.CEbuyPrice = 0
        self.PEsellPrice = 0
        self.PEbuyPrice = 0
        self.CEmtm = 0
        self.PEmtm = 0
        self.ATM = 0
        EClient.__init__(self, self)
        
    def buy_operation(lot)
        
    def tickPrice(self, reqId, tickType, price, attrib):
        global atm_strike
        if(tickType == 4 and self.atm_flag == False):
            self.ATM = int(price / 100) * 100
            self.atm_flag = True
            atm_strike = int(self.ATM)
            print(f'Id: {reqId}, TickType: {tickType}, Price: {price}', self.ATM)
            print(dt.datetime.now())
        else:
            if(tickType == 4 and reqId == 7):
                if(self.CEtrade == False):
                    self.CEsellPrice = price
                    self.CEtrade = True
                if(price >= (self.CEsellPrice * 1.2)):
                    self.CEbuyPrice = price
                self.CEmtm = (self.CEsellPrice - price) if self.CEbuyPrice == 0 else (self.CEsellPrice - self.CEbuyPrice)
            if(tickType == 4 and reqId == 9):
                if(self.PEtrade == False):
                    self.PEsellPrice = price
                    self.PEtrade = True
                if(price >= (self.PEsellPrice * 1.2)):
                    self.PEbuyPrice = price
                self.PEmtm = (self.PEsellPrice - price) if self.PEbuyPrice == 0 else (self.PEsellPrice - self.PEbuyPrice)

                print(f'CE_MTM: {self.CEmtm}, PE_MTM: {self.PEmtm}, MTM: {self.CEmtm+self.PEmtm}')
        
   
        
        
app = strategy()


app.connect(host='127.0.0.1', port=7496, clientId=1)
print(app.isConnected()) 

bnf_contract = Contract()
atm_option_CE = Contract()
atm_option_PE = Contract()

bnf_contract.symbol = 'BANKNIFTY'
bnf_contract.currency = 'INR'
bnf_contract.secType = 'IND'
bnf_contract.exchange = 'NSE'

atm_option_CE.secType = 'OPT'
atm_option_CE.currency = 'INR'
atm_option_CE.exchange = 'NSE'
atm_option_CE.symbol = 'BANKNIFTY'
atm_option_CE.strike = atm_strike
atm_option_CE.right = 'CALL'
atm_option_CE.lastTradeDateOrContractMonth = '20200903'

atm_option_PE.secType = 'OPT'
atm_option_PE.currency = 'INR'
atm_option_PE.exchange = 'NSE'
atm_option_PE.symbol = 'BANKNIFTY'
atm_option_PE.strike = atm_strike
atm_option_PE.right = 'PUT'
atm_option_PE.lastTradeDateOrContractMonth = '20200903'

reqId1 = 8
reqId2 = 7
reqId3 = 9

app.reqMktData(reqId = reqId1, 
               contract = bnf_contract, 
               genericTickList = '', 
               snapshot = False, 
               regulatorySnapshot = False, 
               mktDataOptions = [])
app.reqMktData(reqId = reqId2, 
               contract = atm_option_CE, 
               genericTickList = '', 
               snapshot = False, 
               regulatorySnapshot = False, 
               mktDataOptions = [])

app.reqMktData(reqId = reqId3, 
               contract = atm_option_PE, 
               genericTickList = '', 
               snapshot = False, 
               regulatorySnapshot = False, 
               mktDataOptions = [])

#Timer(15, app.cancelMktData, [reqId1]).start()

#Timer(20, app.disconnect).start()

app.run()       
        