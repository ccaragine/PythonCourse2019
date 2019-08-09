##################### HOMEWORK 1 ####################
## Author: Crystal Caragine
## Date: 8/7/2019
## Saved as: HW1_Caragine

class Stock:
    def __init__(self, symbol= "", amount= 0):
        self.symbol = symbol
        self.amount = amount 
      
class Mutualfund:
    def __init__(self, symbol = "", amount= 0):
        self.symbol = symbol
        self.amount = amount        
      
class Cash:
    def __init__(self, amount = 0):
        self.amount = amount        

class Portfolio:
    def __init__(self, cash=0, mf=0, s=0):
        self.cash = cash
        self.mf = mf
        self.s = s
        self.db = []
    
    def __add__(self, cash):
        self.cash += cash
        my_print_statement = "My %d changed" % cash 
        self.db.append(my_print_statement)
        print(my_print_statement)

        
    def __sub__(self, cash):
        self.cash -= cash
        self.db.append(my_print_statement)
        print(my_print_statement)
        
    def buystock(self, stock):       
        self.s += stock 
        my_print_statement = "I bought %d shares of stock" % stock 
        self.db.append(my_print_statement)
        print(my_print_statement)
     
    def sellstock(self, stck):
        self.s -= stck 
   
    def buymutualfund(self, mutfun, symbol):
        self.mf += mutfun 
        
    def sellmutualfund(self, mutfun, symbol):
        self.mf -= mutfun
 
   
       
        
port = Portfolio()     # creating portfolio
thestock = Stock()     # creating stock
themutualfund = Mutualfund()   # creating mutual fund
thecash = Cash()      # creating cash 


port = Portfolio(cash=15, mf=20.0, s=4)  # Setting values for port

port.cash + 300.5         # Adding cash 

stck = Stock(20, "HFH")      # Creating Stock

port.buystock(5)   # Buy stock

mf1 = Mutualfund("BRT")     # Creating mf1
mf2 = Mutualfund("GHT")     # Creating mf2

port.buymutualfund(10.3, mf1)  
port.buymutualfund(2, mf2)   # Buying mutualfund 

print(port)

port.cash - 50

port.sellmutualfund("BRT", 3)  

port.sellstock("HFH", 1) 
