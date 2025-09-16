todos = [
    "回复老师的邮件",
    "完成物理报告",
    "练习Python，for循环",
    "去图书馆借书",
    "整理GitHub仓库"
]
print(f"{"---今天的待办事项---":^50}")
for todo in todos:
    full_td = f'\u2022 {todo}'
    print(f"{full_td:^50}")
print(f"{"------------------":^50}")
print("\n")
print("---")

import unicodedata

def get_visual_width(s: str) -> int:
    """计算字符串在终端中的视觉宽度，汉字宽度为2，其他为1"""
    width = 0
    for char in s:
        # 'F' (Full-width) 和 'W' (Wide) 通常被视为双字符宽度
        if unicodedata.east_asian_width(char) in ('F', 'W'):
            width += 2
        else:
            width += 1
    return width

# --- 主要逻辑 ---

todos = [
    "回复老师的邮件",
    "完成物理报告",
    "练习Python，for循环",
    "去图书馆借书",
    "整理GitHub仓库"
]

# 准备好所有要打印的行
full_todos = [f'\u2022 {todo}' for todo in todos]
header = "---今天的待办事项---"
footer = "------------------"

# 将所有内容统一处理
lines_to_print = [header] + full_todos + [footer]

# 1. 找到所有行中最长的视觉宽度
max_width = 0
for line in lines_to_print:
    width = get_visual_width(line)
    if width > max_width:
        max_width = width

# 假设终端/总宽度为60
total_width = 60

# 2. 计算为了使整个文本块居中，左侧需要的空格数
# (总宽度 - 文本块的宽度) / 2
left_padding_count = (total_width - max_width) // 2
left_padding = ' ' * left_padding_count

# 3. 打印每一行，并在前面加上相同的左边距
print("\n")
for line in lines_to_print:
    # 对于标题和结尾，我们让它们在自己的文本块内居中对齐，更美观
    if line == header or line == footer:
        # 计算当前行需要额外填充的空格，使其看起来居中
        header_footer_padding_count = (max_width - get_visual_width(line)) // 2
        header_footer_padding = ' ' * header_footer_padding_count
        print(f"{left_padding}{header_footer_padding}{line}")
    else:
        # 待办事项直接加左边距输出，实现左对齐
        print(f"{left_padding}{line}")
print("\n")