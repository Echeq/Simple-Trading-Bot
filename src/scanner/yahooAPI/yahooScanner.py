import yfinance as yf
import matplotlib.pyplot as plt

#from movingAverages import golden_death_crosses

fscope = open("../scanner/scope.txt", "r")
scope = fscope.read().splitlines()
fscope.close()

for data in scope:

    info = yf.Ticker("data").history(period = "2m")
    
    price = info["Close"]
    volumen = info["Volume"]

    plt.figure(figsize = (12, 6))
    plt.plot(price)
    plt.show()