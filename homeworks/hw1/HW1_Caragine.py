############ HOMEWORK 1 ####################
## Crystal Caragine
## 8/7/2019
## HW1_Caragine

class Portfolio:
    def __init__(self, cash=0, mf=0, s=0):
        self.cash = cash
        self.mf = mf
        self.s = s
        self.db = {}
    
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
        self.cash += cash
        
    def __sub__(self, cash):
        self.cash -= cash
        
    def buystock(self, stock):    
        self.stock += stock 
     
    def sellstock(self, stock):
        self.stock -= stock 
   
    def buymutualfund(self, mutualfund, symbol):
        self.mf += mutualfund 
        
    def sellmutualfund(self, mutualfund, symbol):
        self.mf -= mutualfund
         
     def add(self, history, transactions): 
        if mf in self.db:
            self.db[history].append(transactions)
        else: self.db[history] = [transactions]   
    
       
        
port = Portfolio()     # creating portfolio

port = Portfolio(cash=15, mf=20.0, s=4)  # Setting values for port
port.show(15, 20.0, 4)

port.cash + 300.5         # adding cash 

S = port.stock("HFH", 20)    # Creating stock

port.buystock(5)    ##### Not working trying to buy stock

MF1 = port.mutualfund(0,"BRT")     
MF2 = port.mutualfund(0,"GHT") 

port.buymutualfund(10.3, MF1)  
port.buymutualfund(2, MF2)   # Buying mutualfund 


