# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 23:29:26 2020

@author: Vishal
"""


from ibapi.client import EClient
from ibapi.wrapper import EWrapper
from threading import Timer


class strategy(EClient, EWrapper):
    
    def __init__(self):
        EClient.__init__(self, self)


app = strategy()


app.connect(host='127.0.0.1', port=7496, clientId=1)
print(app.isConnected()) 


#Timer(10, app.disconnect).start()

app.run()       
        