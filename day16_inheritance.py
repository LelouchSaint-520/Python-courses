class Dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def sit(self):
        print(f"{self.name} is now sitting.")

# Create a child class of Dog
class PoliceDog(Dog):
    def __init__(self,name,age,department = "K9"):
        #call the __init__() method of parent class, to initialize the name and age
        super().__init__(name,age)
        #add the specific argument of child class
        self.department = department

    def attack(self):
        print(f"{self.name} is attacking the suspect!")

    def sit(self):
        print(f"Police dog {self.name} is sitting with a high alert!")

# call class method
police_dog = PoliceDog("Lucky",25,"CIA")
police_dog.sit()
police_dog.attack()
