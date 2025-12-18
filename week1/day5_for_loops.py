todos = [
    "回复老师的邮件",
    "完成物理报告",
    "练习Python，for循环",
    "去图书馆借书",
    "整理GitHub仓库"
]
total_wd = 60
print(f"{"-----今天的待办事项-----":^{total_wd}}")
for todo in todos:
    full_td = f'\u2022 {todo}'
    print(f"{full_td:^{total_wd}}")
print(f"{"----------------------":^{total_wd}}")
print("\n")
print("---")

# add the number before the tasks

print("-----今天的待办事项-----")
for todo in todos:
    full_td = f'\u2022 {todo}'
    print(full_td)
print("----------------------")
print("\n")

num_task= 1
print('-----今天的待办事项-----')
for todo in todos:
    print(f"\u2022 {num_task}.{todo}")
    num_task += 1
print('----------------------')

# add remark
num_task= 1
print('-----今天的待办事项-----')
for todo in todos:
    if "Python" in todo or "GitHub" in todo:
        print(f"\u2022 【重要】{num_task}.{todo}")
    else:
        print(f"\u2022 【普通】{num_task}.{todo}")
    num_task += 1
print('----------------------')