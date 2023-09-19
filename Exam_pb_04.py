#Multilevel inheritance in python:
class GrandFather:
    def ownhouse(self):
        print("It grand father house ")

class Father(GrandFather):
    def ownbike(self):
        print("It is father bike ")

class Son(Father):
    def ownbook(self):
        print("Son have a Book ")


object = Son()
object.ownhouse()
object.ownbike()
object.ownbook()       
