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
        return score

    def print_info(self):
        print(f"the student information: {self.name.title()}'s student id {self.own} is"
              f" {self.id},{self.own} age is {self.age},{self.own} grade is {self.grade}")
"""
lucy = Student("lucy",20,"Female",9,124345345)
lucy.exam(-1,0)
lucy.print_info()
"""

class Undergraduate(Student):
    def __init__(self,name,age,sex,grade,student_id,major,major_attribute):
        super().__init__(name,age,sex,grade,student_id)
        self.major = major
        self.ma_at = major_attribute
        self.id = f"{student_id}_Undergraduate"
    def passed_grade(self):
        if self.grade >12:
            print(f"Your have been student over {self.grade - 1} years")




lucky = Undergraduate("Lucky",20,"Male",13,1231233,"Mechanic","Mechanical")
#lucky.exam(1,20)
lucky.print_info()
lucky.passed_grade()