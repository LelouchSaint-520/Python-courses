# --- 步骤一：定义我们的“蓝图” ---
from day10_practise import highest_score


class Dog:
    """A simple attempt to model a dog."""

    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(f"{self.name} rolled over!")


# --- 步骤二：根据蓝图，创造具体的“对象” ---
print("--- Creating our first dog object ---")
# This line creates an INSTANCE of the Dog class
my_dog = Dog("Willie", 6)

print("\n--- Creating another dog object ---")
your_dog = Dog("Lucy", 3)

# --- 步骤三：与对象进行交互 ---
print("\n--- Interacting with my_dog ---")
# Accessing attributes
print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
# Calling methods
my_dog.sit()
my_dog.roll_over()

print("\n--- Interacting with your_dog ---")
print(f"Your dog's name is {your_dog.name}.")
your_dog.sit()
print("\n")


# --- 【挑战任务】：创建一个 Car 类 ---
class Car:
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0 # A default attribute

    def get_descriptive_name(self):
        """
        Return a neatly formatted descriptive name
        """
        long_name = f"{self.year}{self.make}{self.model}"
        return long_name.title()
    def read_odometer(self):
        """ Print a statement showing the car's mileage"""
        print(f"This car has {self.odometer_reading} miles on it.")

# Create an instance of the Car class
my_new_car = Car("audi","a4",2024)

#Use the methods and attributes
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

# supplement
class Car:
    """一个模拟汽车的简单类"""

    def __init__(self, make, model, year):
        """初始化汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0  # 里程表
        self.fuel_level = 100      # 满油100%

    def get_descriptive_name(self):
        """返回整洁的描述性信息"""
        return f"{self.year} {self.make} {self.model}"

    # --- 这里是关键示例 ---

    def drive(self, distance):
        """
        驾驶汽车指定的距离，并更新里程表。
        'distance' 就是在 self 之后追加的参数。
        """
        if distance > 0:
            print(f"行驶了 {distance} 公里。")
            self.odometer_reading += distance  # 使用 self 访问并修改属性
        else:
            print("行驶距离必须是正数！")

    def set_fuel_level(self, level, is_percentage=True):
        """
        设置油量。
        这里我们追加了 'level' 和一个默认参数 'is_percentage'。
        """
        if is_percentage and 0 <= level <= 100:
            self.fuel_level = level
            print(f"油量已设置为 {level}%。")
        elif not is_percentage:
            # 假设油箱总共70升
            self.fuel_level = (level / 70) * 100
            print(f"已加油 {level} 升。")
        else:
            print("油量百分比必须在0到100之间。")

# --- 创建实例并调用方法 ---

my_tesla = Car('Tesla', 'Model S', 2025)
print(f"我的新车是: {my_tesla.get_descriptive_name()}")

# 调用 drive 方法，并传入 distance 参数
print(f"当前里程: {my_tesla.odometer_reading} 公里")
my_tesla.drive(150)  # 150 这个 'argument' 会传递给 'distance' 这个 'parameter'
print(f"行驶后里程: {my_tesla.odometer_reading} 公里")

print("-" * 20)

# 调用 set_fuel_level 方法
print(f"当前油量: {my_tesla.fuel_level}%")
my_tesla.set_fuel_level(85) # 调用时只提供 level 参数，is_percentage 使用默认值 True
print(f"更新后油量: {my_tesla.fuel_level:.2f}%")



# Homework
class Student:
    def __init__(self,name:str,age:int,sex:str,grade:int,student_id:int):
        self.name = name
        self.age = age + 1
        self.grade = grade
        self.id = student_id
        if sex == "Male":
            self.own = "his"
        else:
            self.own = "her"

    def homework(self,subject,amount):
        print(f"{self.name} need to finish {amount} {subject} homework!")

    def exam(self, difficulty,score):
        if difficulty:
            score *= 1.2
        elif difficulty < 0:
            score *= 0.8
        else:
            score -= 10

        if score:
            self.grade += 1
        else:
            self.grade -= 1

    def print_info(self):
        print(f"the student information: {self.name.title()}'s student id {self.own} is {self.id},{self.own} age is {self.age},{self.own} grade is {self.grade}")

lucy = Student("lucy",20,"Female",9,124345345)
lucy.exam(-1,0)
lucy.print_info()
