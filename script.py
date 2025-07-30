
#Install all necessary packages
import requests
import time
from alpaca.trading.client import TradingClient
from alpaca.trading.requests import MarketOrderRequest
from alpaca.trading.enums import OrderSide, TimeInForce
#Set up API Key for Alpaca
trading_client = TradingClient('YOURAPIKEY', 'YOURSECRETKEY', paper=True)
orderopen = False
rsi = 0

#Logic to update RSI variable (be sure to replace API key in API link!)
def updatersi():
   global rsi 
    rsijson = requests.get("https://api.twelvedata.com/rsi?symbol=TSLA&interval=1min&outputsize=14&apikey=YOURAPIKEY&source=docs")
    rsiplain = rsijson.json()['values'][0]['rsi']
    rsiplain2 = float(rsiplain)
    rsi = round(rsiplain2, 2)

#Define buy/sell functions (assuming $500.000 balance with $800.000+ buying power)
def buy():
    global orderopen
    market_order_data = MarketOrderRequest(
                        symbol="TSLA",
                        notional=800000,
                        side=OrderSide.BUY,
                        time_in_force=TimeInForce.DAY
                        )
    market_order = trading_client.submit_order(
                    order_data=market_order_data
                   )
    orderopen = True

def sell():
    global orderopen
    trading_client.close_all_positions(cancel_orders=True)
    orderopen = False

while orderopen == False:
    time.sleep(35)
    updatersi()
    print("RSI:", rsi)
    if rsi <= 31:
        buy()
        print("Order placed at RSI:", rsi)
while orderopen == True:
    time.sleep(35)
    updatersi()
    print("RSI:", rsi)
    if rsi >= 69:
        sell()  
        print("Order closed at RSI:", rsi)

