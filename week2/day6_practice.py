# --- 任务一：切片大师---
print("---切片练习---")
nums = list(range(1,11))
print(f'the original list is {nums}')

# 练习1： 获取前5个数字 obtain the first 5 elements in list nums
first_five = nums[:5]
print(f'the first five elements in this list is {first_five}')

# exercise 2: obtain the last 3 elements in the list nums
last_three = nums[-1:-4:-1]
last_3 = nums[-3:]
print(f'the last three elements in nums is {last_three}')
print(last_3)

#exersise 3: obtain all even numbers in this list
even_nums = nums[1::2]
print(f'even nums in the list is {even_nums}')

#exercise 4: creat a reversed copy of nums
reversed_copy = nums[-1::-1]
print(reversed_copy)
print("------")

# --- 任务二：列表推导式达人 ---
print("--- 列表推导式练习 ---")
temps_celsius = [0, 10, 25, 32, 40]

# exercise 1: change the celsius degree into fahrenheit degree
temps_fahrenheit = [temp * 9/5 +32 for temp in temps_celsius]
print(f'celsius degree is {temps_celsius}')
print(f'fahrenheit degree is {temps_fahrenheit}')

# exercise 2: Change the strings sorted out from the mixed list into upper letters
mixed_data = [1 ,"apple" ,3.14 ,"Banana", True, "CHERRY"]
upper_fruits = [fruit.upper() for fruit in mixed_data if isinstance(fruit, str)]
# isinstance(fruit, str)判断一个变量是否为字符串
print(f'the list only contains upper letters for fruits : {upper_fruits}')
print("---")

# task 3: to feel the immutable data structure of tuple
print("---元祖练习---")
# 定义一个元组，代表一个学生的固定信息 (学号, 姓名)
student_info = (2025001, "LelouchSaint-520")
# read the information
student_id = student_info[0]
student_name = student_info[1]
print(f'学号:{student_id},姓名:{student_name}')

## 关键：尝试修改元组，并观察错误
print("现在，我们将尝试修改元组的第一个元素...")
try:
    student_info[0] = 2025002
except TypeError as e:
    print(f"操作失败！发生了错误: {e}")
    print("这个错误明确告诉我们，元组(tuple)对象不支持元素赋值操作。")

#list shallow copy and copy
old_list = list(range(10))
new_list_1 = old_list
new_list_2 = old_list[:]
old_list[3] = 100
print(new_list_1,new_list_2)

# homework
data = list(range(5))
result = [x*10 for x in data[1:4]][::-1]
print(result)