
class Animal:
    def __init__(self, name, age, sound, move):
        self.name = name
        self.age = age
        self.sound = sound
        self.move = move

    def get_sound(self):
        return f"I am {self.name}, & I produce {self.sound} sound"

    def get_move(self):
        return f"I {self.move} very fast"

class Dog(Animal):
    def get_sound(self):
        return "I produce bark sound"


class Cat(Animal):
    def get_sound(self):
        return  "I produce meow sound"


animal = Animal("sarah", 12, "speak", "walk")
print(animal.get_sound())
print(animal.get_move())

# print("--------------------------------------")
# dog = Dog("Chamelion", 5, "speak", "walk")
# print(dog.get_sound())
# print(dog.get_move())
#
#
# print("----------------------------------------")
# cat = Cat("Nyawawa", 2, "hiss", "jump")
# print(cat.get_sound())
# print(cat.get_move())


# - Inheritence
# - Encapsulation
# - Polymorphism - our objects are able to take differnt shape
# - Abstraction