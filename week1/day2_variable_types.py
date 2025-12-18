
'''
1. 创建不同类型的变量 (Creating variables of different types) --
student_name = "Li Hua"
student_age = 17
student_gpa = 3.85  # GPA: Grade Point Average
is_international_student = True

2. 使用 print() 函数将它们打印出来 (Printing them out) --
print("Student Name:", student_name)
print("Student Age:", student_age)
print("Student GPA:", student_gpa)
print("Is an international student?", is_international_student)

3. 使用 type() 函数检查它们的类型 (Checking their types) --
print("Type of student_name:", type(student_name))
print("Type of student_age:", type(student_age))
print("Type of student_gpa:", type(student_gpa))
print("Type of is_international_student:", type(is_international_student))

4. 更专业的打印方式：f-string (A better way to print) --
# f-string 是Python 3.6+版本引入的超棒功能，建议你掌握它
print(f"大家好，我叫 {student_name}，今年 {student_age} 岁。")
'''

student_name = "Li Hua"
student_age = 17
student_gpa = 3.85
is_international_student = True

print(f"Student Name:{student_age:.2f}")
print(type(student_name))
print(type(student_gpa))

a = type(student_age)
print(a)
