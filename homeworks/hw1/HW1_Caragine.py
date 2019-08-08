############ HOMEWORK 1 ####################
## Crystal Caragine
## 8/7/2019
## HW1_Caragine

class Portfolio:
    def __init__(self, cash=0, mf=0, s=0):
        self.cash = cash
        self.mf = mf
        self.s = s
    
    def show(self, cash, mf, s) :
        print(mf)
        print(s)
        return port.cash

    def stock(self, symbol, amount):
        self.symbol = symbol 
        self.amount = amount
        
    def mutualfund(self, symbol, amount):
        self.symbol = symbol
        self.amount = amount
    
    def __add__(self,cash):
        self.cash + cash
        
    def __sub__(self, cash):
        self.cash - cash
        
    def buystock(self, stock):    
        self.stock + stock 
        self.cash - stock 
        
    
       
        
port = Portfolio()     # creating portfolio

port = Portfolio(cash=15, mf=20.0, s=4)  # Setting values for port
port.show(15, 20.0, 4)

port.cash + 300.5         # adding cash 

S = port.stock("HFH", 20)

port.buystock(5)    ##### Not working trying to buy stock

MF1 = port.mutualfund("BRT", 0)     ##### Not working 
MF2 = port.mutualfund("GHT", 0)


