# define and call a function
# 1. 定义一个名为 greet 的函数
def greet():
    print("Hello, world!")
    print("Welcome to Day 10.")


# 2. 调用这个函数
print("Calling the function for the first time:")
greet()

print("\nCalling it again:")
greet()

# Parameters（形参） vs Arguments(实参)
# ‘name’ is a parameter
def greet_user(name):
    print(f"Hello, {name}")

# "Alex" is an argument
greet_user("Alex")

# "Maria" is another argument
greet_user("Maria")

# 3. return: return the result of the function after operating
def add_numbers(a,b):
    result = a + b
    return result
# call the function, then save the result into the variable 'sum_value'
sum_value = add_numbers(5,3)
print(f"The function returned : {sum_value}")
# We can conduct the following operation
if sum_value > 7:
    print("The sum is greater than 7.")

