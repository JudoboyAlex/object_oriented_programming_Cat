class Cat: 

    def __init__(self, name, preferred_food, meal_time):
        self.name = name
        self.preferred_food = preferred_food
        self.meal_time = meal_time
    
    def __str__(self):
        return "My name is {} and I eat {} at {}".format(self.name, self.preferred_food, self.meal_time)
    
    def eats_at(self):
        if self.meal_time >= 13:
            return str(self.meal_time - 12) + "PM"
        else: 
            return str(self.meal_time) + "AM"

    def meow(self):
        return "My name is {} and I eat {} at {}".format(self.name, self.preferred_food, self.eats_at())


goku = Cat("goku", "tuna", 11)
gohan = Cat("gohan", "salmon", 22)


print(gohan)
print(gohan.eats_at())
print(gohan.meow())


  

