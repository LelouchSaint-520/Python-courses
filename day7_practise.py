# test order
new_dic = {"Fruit":'Apple',
           'Vegetable':'carrot',
           'Meat':'Pork',
           'Meat2':'Beef'
}
print(new_dic)

set1 = {
    "Apple",
    "Carrot",
    "Pork",
    "Beef",
    "Milk"
}
print(set1)

print("------------------")

# 1. create
student_profile = {
    'student_id':'202501',
    'name':'Lelouch',
    'age':17,
    'course':['math','Physics','CS','English'],
    'contact':{
        'email':"Lelouchocean@gmial.com",
        'Phone':None
    }
}
print('---初始档案---')
print(student_profile)
print("\n")

# Read visit the info
print("---读取信息---")
student_name = student_profile["name"]
print(f"student name is :{student_name}")

# Read the GPA info safely
student_gpa = student_profile.get('gpa','N/A')
print(f'GPA of student os :{student_gpa}')

# Read the nested data: Obtain the first course subject and email address
first_course = student_profile["course"][0]
email_address = student_profile['contact']['email']
print(first_course, email_address)
print("\n")

# Update and Add: Modify the dicts
print("---Update and add information---")
student_profile["age"] = 18
student_profile["course"].append("Chemistry")
student_profile["contact"]['Phone'] = "1234-5678"
student_profile["status"] = "activate"
print("the profile after updating")
print(student_profile)
print("\n")

# Iterate: print the profile in format
print("---学生档案报告---")
for key, value in student_profile.items():
    if isinstance(value,list):
        print(f"\u2022 {key.title()} : {'，'.join(value)} ")
    else:
        print(f"\u2022 {key.title()}:{value}")
print("---报告结束---")

"""
**【小挑战：管理水果价格】**
    - 创建一个字典，存储三种水果和它们每公斤的价格，例如 `fruit_prices = {'apple': 5.5, 'banana': 3.0, 'orange': 4.5}`。
        
    - 增加一种新水果 "durian" 和它的价格。
        
    - 将 "apple" 的价格修改为 6.0。
        
    - 使用`for`循环，计算并打印出购买每种水果各2公斤的总价格。
     
"""

fruit_prices: dict[str, float] = {'apple':5.5, 'banana':3.0, 'orange':4.5}
fruit_prices['durian'] = 10.0
fruit_prices['apple'] = 6
print(fruit_prices)
total_price = 0
for value in fruit_prices.values():
    total_price += 2* value
print(f"the total price of each fruits purchase 2KG is {total_price}")
for key,value in fruit_prices.items():
    print(f"\u2022 the price of 2KG {key} is {2*value}")


