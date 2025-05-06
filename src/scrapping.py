import yfinance as yf
import matplotlib.pyplot as plt

info_BTC = yf.Ticker("BTC-USD").history(period = "2m")

price_BTC = info_BTC["Close"]
volumen_BTC = info_BTC["Volume"]

plt.figure(figsize = (12, 6))
plt.plot(price_BTC)
plt.show()