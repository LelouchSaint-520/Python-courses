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

