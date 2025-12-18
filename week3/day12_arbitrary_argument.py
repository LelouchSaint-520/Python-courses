"""
# 这个函数可以计算任意数量数字的总和
def sum_all(*numbers):
    print(f"收到的参数打包成元组: {numbers}")
    total = 0
    for num in numbers:
        total += num
    return total

print(sum_all(1, 2))          # 传入 2 个参数
print(sum_all(1, 2, 3, 4, 5)) # 传入 5 个参数
print(sum_all())              # 不传入参数
"""


# *numbers 会收集所有传入的位置参数
def sum_all_numbers(*numbers):
    print(f"I received these numbers: {numbers}")
    print(f"The type of 'numbers' is: {type(numbers)}")  # 验证它是一个元组

    total = 0
    for number in numbers:
        total += number
    return total
# 我们可以用任意数量的参数来调用它
print(f"Sum: {sum_all_numbers(1, 2, 3)}")
print("---")
print(f"Sum: {sum_all_numbers(10, 20, 30, 40, 50)}")
print("---")
print(f"Sum: {sum_all_numbers()}")  # 即使不传参数也可以

#**user_details will collect all passing keyword arguments
def build_user_profile(username,**user_details):
    print(f"Building profile for:{username}")
    print(f"I received these details:{user_details}")
    print(f"The type of 'user_details' is: {type(user_details)}")

    # we can operate it like operating dictionary
    if 'city' in user_details:
        print(f"{username} is form {user_details['city']}.")
build_user_profile("Aragorn", city="Gondor",race="Human",title="King")
print("---")
build_user_profile("Lego",race="Elf",weapon="Bow")

"""
参数的终极顺序：
当一个函数同时使用所有类型的参数时，必须遵循以下天条般的顺序：
1. 标准位置参数(a, b)
2. 默认参数(c=1, d=2)
3. *args
4. **kwargs
def my_ultimate_function(a, b, c=1, d=2, *args, **kwargs):


The order of the arguments in the function:
1. standard positional argument
2. default argument
3. arbitrary argument:
    3.1 positional argument *args
    3.2 keyword argument **kwargs
    
|No.|  define function  |                               |  function calling   |
| 1 |Parameter name     |  Positional Parameters        |Positional arguments |
| 2 |Default argument   |                               |                     |
| 3 |                   |                               |  Keyword arguments  |
| 4 |arbitrary arguments|Arbitrary positional arguments |                     |
| 5 |                   |Arbitrary keyword arguments    |                     |

1. 一个函数def后的内容（函数名，形参和默认参数）被称为function signature
2. 一个函数签名中，只能存在一个*args或**kwargs,不能同时出现两个*args和**kwargs
3. 在定义函数的阶段，参数都为形参parameters，比如default parameters， arbitrary parameters,但是此处arguments更常用
"""

# --- 任务一：使用 *args 打造一个字符串连接器 ---
def combine_strings(*words):
    """接收任意数量的字符串，并将它们用空格连接成一句话。"""
    # ' '.join(iterable) 是一个非常有用的字符串方法
    sentence = " ".join(words)
    return sentence

print(combine_strings("hello","world","form","Python","!"))
print(combine_strings("I","Love","coding","."))
print("\n")

# --- 任务二：使用 **kwargs 打印一份配置报告 ---
def print_system_config(**configs):
    print("---System Configuration Report---")
    if not configs:
        print("Warning:No configuration provided! \n")
        return
    for key, value in configs.items():
        print(f"\u2022 {key.replace('_',' ').title()}:{value}")
    print("---------------------------------\n")

print_system_config(
    user_name = "Gandalf",
    access_level = "admin",
    log_file = "/var/log/system.log",
    debug_mode = True
)
print_system_config()

# --- 任务三：【综合挑战】一个灵活的pizza订单函数 ---
def order_pizza(size, *toppings, **customer_details):
    """
    制作披萨订单。
    - size 是必须的位置参数。
    - *toppings 收集所有配料。
    - **customer_details 收集顾客信息。
    """
    print(f"--- New Pizza Order ---")
    print(f"Size:{size}")
    if toppings:
        print("Toppings:")
        for topping in toppings:
            print(f"\u2022 {topping.title()}")
    else:
        print("Toppings: Plain Cheese")
    if customer_details:
        print("Customer Details:")
        for key, value in customer_details.items():
            print(f"\u2022 {key.upper()}: {value}")
    print("-----------------------\n")
# a simple order:
order_pizza("Large","Mushroom","Pepperoni")
# a complex order:
order_pizza(
    "Medium",
    "Onions","green peppers","Extra cheese",
    delivery = True,
    customer_name = "Frodo",
    address="Bag End, The Shire"
)



