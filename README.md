****Simple RSI Trading Bot****

This Python script automates buying and selling Tesla (**TSLA**) stock based on RSI values using Alpaca’s paper trading API and Twelve Data’s RSI indicator.

****How It Works****

Fetches TSLA’s RSI every 35 seconds via Twelve Data API

Buys TSLA when RSI ≤ 31

Sells TSLA when RSI ≥ 69

Executes trades through Alpaca paper trading environment (no real money involved)

****Necessary Packages:****

alpaca-py

requests

****Replace API keys in the script:****


Alpaca API key & secret
Twelve Data API key

****Disclaimer****

This script is for educational and testing purposes only. It uses Alpaca’s paper trading API and does not involve real financial risk. Trading cryptocurrencies or stocks involves substantial risk, and you should not rely on this script for real trading decisions. I am not responsible for any financial losses or damages resulting from the use of this software.
