# creat the dictionary
# 创建一个存储你个人信息的字典
my_profile = {
    "name": "LelouchSaint-520",
    "age": 17,
    "courses": ["Computer Science", "Physics", "Math"], # 值可以是一个列表
    "is_student": True
}
print(my_profile)
# 创建一个空字典
empty_dict = {}

# read
# Method 1 : index with key
value = my_profile['name']
# Method 2 : .get(key, Null)
age = my_profile.get('age')
gpa = my_profile.get('gpa', 3.5)
print(age,gpa)

# update and add
# 更新 (Update): 修改已存在的键的值
my_profile['age'] = 18 # 把年龄更新为18

# 增加 (Add): 添加一个新的键值对
my_profile['country'] = "Singapore" # 新增一个国家信息
print(my_profile)

# delete
# del dictionary[key]
del my_profile['is_student']
# .pop(key) -> return value
removed_value = my_profile.pop('age')
print(f'the removed age is :{removed_value}')
print(my_profile)

# keys values items
# Iterate keys
for key in my_profile.keys():
    print(f'this is a key:{key}')

# Iterate values
for value_1 in my_profile.values():
    print(f'this is a value:{value_1}')

# Iterate items:
for key_2, value_2 in my_profile.items():
    print(f"the value to key {key_2} is {value_2}")
