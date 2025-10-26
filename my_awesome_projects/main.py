# main.py in my_awesome_project
"""
Main execute file of this project, demonstrate importing module from the package
"""

# method 1 : importing module from package:
print("--- Importing module from package ---")
import utils.calculator
import utils.string_formatter

# the whole path "package.module.function" must be used while calling the function
sum_result = utils.calculator.add(10,5)
print(f"The sum is {sum_result}")

title = utils.string_formatter.format_as_title(" my first package project ")
print(title)
print("\n")

# method 2 : import the certain function from the module in the package
print("--- Importing specific function from package.module ---")
from utils.calculator import multiply
from utils.string_formatter import format_as_warning

# the function name can be used directly while calling in this method.
product_result = multiply(10,5)
print(f"The product is : {product_result}")

warning_message = format_as_warning("Package structure is important! ")
print(warning_message)

# method 3 :use alias
print("\n---use aliases---")
import utils.calculator as calc
from utils.string_formatter import format_as_title as make_title

print(f"Another sum using alias: {calc.add(100,200)}")
print(make_title("aliases are cool"))


