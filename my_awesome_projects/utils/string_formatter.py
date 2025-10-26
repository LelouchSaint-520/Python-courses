"""
This is a module with tools that can change the format of strings
"""

def format_as_title(text):
    """将字符串格式化为标题样式并加上边框"""
    print(__name__)
    title = text.strip().title()
    border = "=" *(len(title)+4)
    return f"{border}\n\u2022 | {title} |\u2022\n{border}"

def format_as_warning(text):
    print(__name__)
    """将字符串格式化为警告信息"""
    return f"WARNING: {text.upper()}"
