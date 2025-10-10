# 1. Define the parent class Car

class Car:
    def __init__(self,make,model,year:int):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it")

    def drive(self,miles):
        """Simulate driving the car and update odometer."""
        if miles > 0:
            self.odometer_reading += miles

class ElectricCar(Car):
    """ Represents aspect of a car, specific to electric vehicles"""
    def __init__(self, make, model, year):
        """
        Initialize attribute of the parent class.
        Then initialize attribute specific to an electric car.
        """
        # 1. call the constructor of parent class
        super().__init__(make,model,year)
        # 2. add the specific attribute of child class
        self.battery_size = 75 # in kWh
        self.year += 1
    # 3. add the specific method of child class
    def describe_battery(self):
        """Print a statement describing the battery size"""
        print(f"This car has a {self.battery_size}-kWh battery.")

    # #add a new method
    def battery_cap(self,battery):
        self.battery_size = battery

    # 4. overwrite the method from parent class
    def get_descriptive_name(self):
        """Return a descriptive name with 'Electric' prefix. """
        # 仍可调用父类版本的方法
        parent_name = super().get_descriptive_name()
        return f"Electric: {parent_name}"

# --- Instantiating and calling ---
print("--- Creating a regular car instance ---")
my_beetle = Car('volkswagen','bettle',2019)
print(my_beetle.get_descriptive_name())
my_beetle.drive(100)
my_beetle.read_odometer()
#my_beetle.descriptive_battery() # 这里会报错！ 因为普通Car没有这个方法

print("\n--- Creating an electric car instance ---")
my_tesla = ElectricCar('tesla','model s', 2023)
#子类继承了父类的方法
print(my_tesla.get_descriptive_name()) # 调用的是重写后的版本
my_tesla.drive(50)
my_tesla.read_odometer()
# 子类可以使用自己独有的方法
#my_tesla.battery_cap(60)
my_tesla.describe_battery()

"""
Summary:
--- concept of function, OOP, and class inheritance
1. function:
    1. function definition
        signature
        define : def / parameters
    2. function call
        argument
    3， passing argument: argument passed into parameters
        
2. class
    1. 类名
    2. 构造方法 __init__，形参
    3. 属性（对象的特征），形参于属性的表达式
    4. 方法，类内部的函数

3.inheritance
    1. 父类
    2. 子类
    
    
        
"""

