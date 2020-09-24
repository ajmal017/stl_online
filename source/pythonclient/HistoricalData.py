from ibapi.client import EClient
from ibapi.wrapper import EWrapper
from ibapi.contract import Contract

class TestApp(EWrapper, EClient):
    def __init__(self):
        EClient.__init__(self, self)

    def error(self, reqId, errorCode, errorString):
        print("Error: ", reqId, " ", errorCode, " ", errorString)

    def historicalData(self, reqId, bar):
        print("Historical data: ", reqId, "Date: ", bar.date, "open: ", bar.open, "High: ", bar.high, "Low: ", bar.low, "Close: ", bar.close)

def main():
    app = TestApp()

    app.connect("127.0.0.1", 7496, 0)

    contract = Contract()
    # contract.symbol = "EUR"
    # contract.secType = "CASH"
    # contract.exchange = "IDEALPRO"
    # contract.currency = "USD"

    contract.symbol = "RELIANCE"
    contract.secType = "STK"
    contract.exchange = "NSE"
    contract.currency = "INR"

    app.reqHistoricalData(1, contract, "", "1 D", "1 min", "MIDPOINT", 0, 1, False, [])

    app.run()

if __name__ == "__main__":
    main()
