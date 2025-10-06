"""
练习题

变量解包：
有一个列表 records = ['USER001', '2025-10-07', 'LOGIN_SUCCESS', '192.168.1.100']。
请使用解包一次性将 USER001 赋值给 user_id，将 192.168.1.100 赋值给 ip_address，并将中间的两个元素赋值给一个名为 details 的列表。

函数调用解包：
定义一个函数 def report_status(service, status, region="ap-southeast-1"): ...。
现在你有一个列表 service_info = ['Database', 'Operational'] 和一个字典 location = {'region': 'us-west-2'}。
请只用一行代码调用 report_status 函数来正确传递这些参数。

合并字典：
有两个字典 default_settings = {'theme': 'dark', 'font_size': 12}
和 user_preferences = {'font_size': 14, 'language': 'Python'}。
请使用解包在一行代码内创建一个新的 final_settings 字典，它应该包含所有设置，并优先使用用户的偏好。
"""

# 1
records = ['USER001', '2025-10-07', 'LOGIN_SUCCESS', '192.168.1.100']
user_id,*details,ip_address = records
print(user_id,details,ip_address)

# 2
service_info = ['Database', 'Operational']
location = {'region': 'us-west-2'}
loca = "us-west"
def report_status(service, status, region="ap-southeast-1"):
    print(f"Service:{service}")
    print(f"status: {status}")
    print(f"region:{region}")

report_status(*service_info,**location)
report_status(*service_info,location)
report_status(*service_info,loca)

# 3
default_settings = {'theme': 'dark', 'font_size': 12}
user_preferences = {'font_size': 14, 'language': 'Python'}
final_setting = {**default_settings,**user_preferences}
print(final_setting)