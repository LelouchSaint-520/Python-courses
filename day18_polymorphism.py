# 定义三个不同的类，它们之间没有任何继承关系
class Dog:
    def speak(self):
        return "Woof!"
class Cat:
    def speak(self):
        return "Meow!"
class Duck:
    def speak(self):
        return "Quack!"
# create different objects
dog = Dog()
cat = Cat()
duck = Duck()

#---The charm of polymorphism---
# This is a function with "general interface", it doesn't care the type of animal.
# It just supposed that the animal object passed hase a method called speak()
def make_animal_speak(animal):
    print(animal.speak())

make_animal_speak(dog)
make_animal_speak(cat)
make_animal_speak(duck)