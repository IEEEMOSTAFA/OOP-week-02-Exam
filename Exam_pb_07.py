class Person:
    def __init__(self,name,age,height,weight) -> None:
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def __lt__(self,other):
        return self.age < other.age



class Crickter(Person):
    def __init__(self, name, age, height, weight) -> None:
        super().__init__(name, age, height, weight)        
        
sakib = Crickter('Sakib',38,68,91)
Mushfiq = Crickter('Musfiq',36,55,82) 
Mustafiz = Crickter('Mustafiz',27,69,86)
Riyad = Crickter('Riyad',39,72,92)

players = [sakib,Mushfiq,Mustafiz,Riyad]
youngest_player = min(players)
print(youngest_player.name)
