from datetime import datetime

import pandas
from pandas_datareader import data as pdr
import fix_yahoo_finance as yf

class Stock:


    def __init__(self, start, end, name):
        yf.pdr_override()
        self.start = start
        self.end = end
        self.name = name
        print("hej")

        self.data = pdr.get_data_yahoo(start=self.start, end=self.end, tickers=self.name, actions = True)
        
    def momentum(self, months): #Ger lista/array med momentum för en aktie i månadsintervall
        close = []
        day = 0
        for i in range(0, (self.end-self.start)/months-1): #Fixa detta så att end & start omvandlas till månader elr använd while loop
            close.append(self.data.iat[day, df.columns.get_loc('Close')])
            day = day + months*30
        momentum = []
        for i in range(1, len(close)-1): #Blir detta rätt med index elr ska det bara vara len(close)
            monentum.append(((close[i]-close[i-1])/close[i-1])*100) #tänk på att första värdet inte får ngt momentum, ger det i procentutveckling
        
