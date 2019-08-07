## Fill in the following methods for the class 'Clock'

class Clock:
    def __init__(self, hour, minutes):
        self.minutes = minutes
        self.hour = hour

    ## Print the time
    def __str__(self):
                return("It is " + str(self.hour) + " " + str(self.minutes)) 
    
    ## Add time
    ## Don't return anything
    def __add__(self,minutes):
        while minutes > 60:
            self.minutes -= 60 
            self.hour += 1
        else: self.minutes += minutes 
    
    ## Subtract time
    ## Don't return anything
    def __sub__(self,minutes):
        while minutes > 60:
            self.minutes += 60
            self.hour -= 1
        else: self.minutes -= minutes
    
    ## Are two times equal?
    def __eq__(self, other):
        if self.minutes != other.minutes: return False
        elif self.hour != other.hour: return False
        else: return True 
    
    ## Are two times not equal?
    def __ne__(self, other):
       return not self.__eq__(other) 

        
clock1 = Clock(4,45)
clock2 = Clock(2, 15) 

clock1 == Clock(11,00)

clock2 != Clock(6,15) 

print(clock1) 

clock1 + 65
print(clock1) 

clock2 - 15  
print(clock2)    