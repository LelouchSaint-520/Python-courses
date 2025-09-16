# Create a list
subjects = ["Chinese","Math","English"]

# Create an empty list

my_plan = []

# read the first subject in the list
first_subject = subjects[0]
print(f"第一门课程是{first_subject}")

# read the third subject in the list
third_subject = subjects[2]
print(f'The third subject is {third_subject}')

# read the last subject in the list
last_subject = subjects[-1]
print(f'the last subject is {last_subject}')

# read the second last subject
second_last_subject = subjects[-2]
print(f'the second last subject is {second_last_subject}')

# update the third/second last subject
subjects[2] = "Science"
print(f"the list after updating is {subjects}")

subjects[-2] = "Music"
print(f'the list after updating is {subjects}')

# append a subject/ an element at the end of list.
subjects.append("History")
print(f"the list after appending is {subjects}")

# insert an element at a certain position in the list
subjects.insert(1,"Art")
print(f'the list after inserting an element at the second position (No.1 index position) is {subjects}')

# delete an element - del
del subjects[0]
print(f'the list after deleting the No.0 index position is {subjects}')

# pop out an element
last_item = subjects.pop()
print(f'the element popped out is {last_item}')
print(f'the list after popping out element is {subjects}')

subjects.pop(1)
print(subjects)

# .remove(value) is only remove the first element with the value in remove command
subjects.append("Math")
subjects.insert(2,"Art")
print(subjects)
subjects.remove("Art")
print(subjects)

# to get the length of the list
num_of_subjects = len(subjects)
print(num_of_subjects)
print()
print("---")


# 1. 创建 (Create): 初始化你的待办事项列表
todos = ["完成数学作业", "练习Python编程1小时", "阅读一章《基地》"]
print(f"初始待办事项: {todos}")
print("---")

# 2. 读取 (Read): 查看你的任务
first_todo = todos[0]
last_todo = todos[-1]
print(f"我的第一项任务是: {first_todo}")
print(f"我的最后一项任务是: {last_todo}")
print("---")

# 3. 更新 (Update): 修改一项任务
print(f"修改前，索引1的任务是: {todos[1]}")
todos[1] = "练习Python列表操作1小时"  # 内容更具体
print(f"修改后，索引1的任务是: {todos[1]}")
print("---")

# 4. 增加 (Add): 有新的任务啦！
todos.append("给家里打个电话")
print(f"追加任务后: {todos}")
todos.insert(0, "【紧急】回复老师的邮件")  # 插入一个紧急任务到最前面
print(f"插入紧急任务后: {todos}")
print("---")

# 5. 删除 (Delete): 完成或取消任务
# 删掉已经完成的紧急任务
del todos[0]
print(f"删除紧急任务后: {todos}")

# 完成了最后一项任务，并看看是什么
finished_task = todos.pop()
print(f"我刚刚完成了: '{finished_task}'")
print(f"剩下的任务: {todos}")

# 取消“完成数学作业”这项任务
todos.remove("完成数学作业")
print(f"取消一项任务后: {todos}")
print("---")

# 6. 统计 (Count): 看看还剩几件事
remaining_count = len(todos)
print(f"太棒了！今天只剩下 {remaining_count} 项任务了！")


