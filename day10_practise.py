# --- 任务一：一个简单的天气预报函数 ---
# 定义一个函数，接收一个城市名(city)和天气(weather)作为参数
def repo_weather(city,weather):
    """this is a sample function and could be used to print the weather report"""
    print(f"Weather repo for {city}")
    print(f"Today's weather is {weather}")

# call the function
repo_weather("Singapore","sunny with occasional showers")
print("---")
repo_weather("London","cloud")
print("\n")

# --- 任务二：一个带返回值的矩形面积计算器 ---
# 定义一个函数，接收宽(width)和高(height)，返回计算出的面积
def calculate_rectangle_area(width,height):
    area = width * height
    return area

# call the function and assign the return value to the variable
room1_area = calculate_rectangle_area(10,5)
room2_area = calculate_rectangle_area(8.5, 6)
total_area = room1_area + room2_area
print(f"Area of Room 1 is: {room1_area} square meters.")
print(f"Area of Room 2 is: {room2_area} square meters.")
print(f"The total area is: {total_area} square meters.")
print("\n")

# --- 任务三：【挑战】处理列表的函数 ---
    # 定义一个函数，接收一个数字列表(numbers)，返回列表中的最大值
    # （暂时不要使用Python内置的max()函数，我们自己用循环实现）
def find_max_in_list(numbers):
    if not numbers:
        return None
    max_value = numbers[0]
    for number in numbers:
        if number >max_value:
            max_value = number
    return max_value
scores = [88, 95, 76, 100, 92]
highest_score = find_max_in_list(scores)
print(f"the list of scores is : {scores}")
print(f"The highest score found by our function is: {highest_score}")

empty_list = []
result_empty = find_max_in_list(empty_list)
print(f"Result for an empty list is: {result_empty}")

