from ibapi.client import EClient
from ibapi.wrapper import EWrapper
from ibapi.contract import Contract
from ibapi.ticktype import TickTypeEnum

class TestApp(EWrapper, EClient):
    def __init__(self):
        EClient.__init__(self, self)

    def error(self, reqId, errorCode, errorString):
        print("Error: ", reqId, " ", errorCode, " ", errorString)

    def contractDetails(self, reqId, contractDetails):
        print("contractDetails: ", reqId, " " , contractDetails)

    def tickPrice(self, reqId , tickType, price, attrib):
        print("Tick price. Tick ID:", reqId, "tickType:", TickTypeEnum.to_str(tickType), "Price: ", price, end=' ')

    def tickSize(self, reqId, tickType, size):
        print("Tick size. Tick ID:", reqId, "tickType:", TickTypeEnum.to_str(tickType), "Size: ", size)

def main():
    app = TestApp()

    app.connect("127.0.0.1", 7496, 0)

    contract = Contract()
    contract.symbol = "RELIANCE"
    contract.secType = "STK"
    contract.exchange = "NSE"
    contract.currency = "INR"

    app.reqMarketDataType(4)
    app.reqMktData(1, contract, "", False, False, [])

    app.run()

if __name__ == "__main__":
    main()
