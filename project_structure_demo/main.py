"""
项目的主执行文件，用于演示模块的导入
"""
from project_structure_demo.string_formatter import format_as_warning

#---方法一：导入整个模块---
print("---Testing 'import module'---")
import calculator
import string_formatter

# 调用时必须使用 模块名.函数名
sum_result = calculator.add(10,5)
product_result = calculator.multiply(10,5)
print(f"The sum is : {sum_result}")
print(f"The product is: {product_result}")
print(f"The value of PI from calculator module is {calculator.PI}")

#使用另一个模块的函数
title = string_formatter.format_as_title("  my first multi-file-project ")
print(title)
print("\n")

# ---方法二：从模块中导入特定函数---
print("--- Testing 'from module import function' ---")
from calculator import add,multiply
from string_formatter import format_as_warning as fw
sum_result_2 = add(100,50)
print(f"Another sum : {sum_result_2}")

warning_message = fw("the system is going down for maintenance.")
warning_message_2 = format_as_warning("the system is going down for maintenance.")
print(f"{warning_message} \n")
print(warning_message_2)

# --- 方法三：使用别名 ---
import string_formatter as sf
print(sf.format_as_title("using alias"))
