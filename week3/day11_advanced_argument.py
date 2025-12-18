"""
Three concepts: Positional argument, Default argument, Keyword argument
1. Positional argument: the common mode of the function
def func(a,b,c):
    xxx
func(m,n,o)
a <- m
b <- n
c <- o
each argument has its own position. There will be mistakes if the arguments are at the incorrect position.
And all argument need to be defined when calling the function

2. Default argument：set the argument when define the function, and will call them if there are no arguments passed in.
def func(a,b=n,c=o)：
    xxx
func(m)
parameter b and c are defined with their own default value, and it will use the default value if they haven't been passed arguments
the golden principle of the default argument is itself must be set after the positional argument

3. Keyword argument: set the argument with its parameters when calling the function
def func(a,b,c)：
    xxx
func(m, c=o, b=n)
the order of the passing argument could be changed.
the golden principle of the keyword argument is itself must be set after the positional argument

"""

# --- 任务一：带有默认值的用户注册函数 ---
def create_user(username, email, is_active=True, role="guest"):
    """创建一个新用户，is_active和role有默认值。"""
    print("---Creating New User---")
    print(f"Username: {username}")
    print(f"Email: {email}")
    print(f"Active Status: {is_active}")
    print(f"Role: {role}")
    print("-----------------------\n")

#create an ordinary user
create_user("alex","alex@example.com")

#create an administrator user, overwrite the default argument of role
create_user("admin_user","admin@example.com",role="admin")

# --- 任务二：使用关键字参数配置一个复杂的图形 ---
def draw_shape(shape,x,y,width,height,color,border_width,style):
    """a function created to simulate to draw the graphics with many parameters"""
    print(f"Drawing a {color} {style} {shape} with border width {border_width}.")
    print(f"Positioned at {x} {y} with size ({width},{height}).")

# 不使用关键字参数（非常难以阅读和维护！）
# draw_shape("rectangle", 10, 20, 100, 50, "blue", 2, "solid")
# 使用关键字参数（清晰、易读、不易出错！）
draw_shape(
    shape = "rectangle",
    x = 10,
    y = 20,
    width = 100,
    height = 50,
    color = "blue",
    border_width = 2,
    style = "solid"
)
print("\n")

# --- 任务三：【综合挑战】一个灵活的邮件发送函数 ---
def send_notification(to_email,subject,body,from_email="noreply@myservice.com",cc=None):
    """To send an email, from_email and CC is selectable"""
    print("---Sending Email---")
    print(f"From: {from_email}")
    print(f"To: {to_email}")
    if cc:
        print(f"CC: {cc}")
    print(f"Subject: {subject}")
    print("---Body---")
    print(body)
    print("-------------------\n")

#1. 发送一封最简单的邮件：
send_notification(
    to_email="customer@example.com",
    subject="Your order has shipped!",
    body="Dear customer, \n"
         "Your item is on its way. \n"
         "Good luck to you! \n"
)

#2. 发送一封需要抄送的邮件：
send_notification(
    to_email = "manager@example.com",
    subject = "Weekly Report",
    body = "Please find the attached report.\n"
           "If there is anything need more detail, pls. contact me!\n",
    cc = "team@exapmle.com"
)
