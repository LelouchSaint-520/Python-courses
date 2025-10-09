"""
1. define a class

 class Dog:
        # We'll fill this in shortly
        pass # 'pass' is a placeholder that does nothing

2. construct method

    __init__()
    #initialize the new object and set some attributes for it.

3. self argument

self is the first parameter of __init__, and it is also the first parameter of all classes.
'self' represents the object instance itself that was created.

4. Attributes are the feature of objects

self.attribute_name = value

5. Methods - the behaviors of objects

"""


class Dog:
    """A simple attempt to model a dog."""

    def __init__(self, name, age):
        """Initialize name and age attributes"""
        self.name = name + name
        self.age = age * 2

    def sit(self):
        """ Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """ Simulate rolling over in response to a command. """
        print(f"{self.name} rolled over!")

# Creat instances
print("---Creating our first dog object---")
# This line create an Instance of the Dog class
my_dog = Dog("Willie", 6)

print("\n --- Creating another dog object ---")
your_dog = Dog("Lucky", 3)

# interact with object
print("\n--- Interacting with my dog ---")
# Accessing attributes
print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old")
# Calling methods
my_dog.sit()
my_dog.roll_over()

print("\n--- Interacting with your_dog ---")
print(f"Your dog's name is {your_dog.name}")
your_dog.sit()
your_dog.roll_over()
print("\n")
print()