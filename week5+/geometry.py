# 1. 定义函数 (造机器)
# width 和 height 是参数 (Parameters)，是机器的进料口
def calculate_rectangle_area(width, height):
    """
    计算矩形面积并返回结果。
    """
    area = width * height
    # 关键一步：把结果“吐”出来，而不是只打印出来
    return area

# 2. 调用函数 (使用机器)
# 我们投入原料 10 和 5
# 我们用一个变量 'my_room' 接住机器吐出来的结果
my_room = calculate_rectangle_area(10, 5)

# 3. 验证结果
print(f"我的房间面积是: {my_room} 平方米")

# 4. 进阶验证 (只有 return 才能做到！)
# 如果我想计算两个房间的总面积：
living_room = calculate_rectangle_area(6, 4)
total_area = my_room + living_room  # 看！我们可以拿结果继续做数学运算
print(f"总面积是: {total_area} 平方米")
