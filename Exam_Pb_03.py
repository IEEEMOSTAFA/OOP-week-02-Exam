import math
class Myclass:
    def __init__(self,a,b,c) -> None:
        self.a = a
        self.b = b
        self.c = c

    def Sum(self):
        return self.a + self.b + self.c
    
    def factorial(self):
        if self.b < 0:
            raise ValueError("b must be non negative ")
        
        return math.factorial(self.b)
    

my_class = Myclass(1,3,3)
print(my_class.Sum())
print(my_class.factorial())    