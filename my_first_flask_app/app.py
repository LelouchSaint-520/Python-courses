from flask import Flask, render_template  # import flask class
app = Flask(__name__)

@app.route('/')
def home():
    """Renders the static index.html page."""
    # Flask will find search the 'index.html' in the 'templates' folder
    return render_template('index.html')

@app.route('/user/<name>') #别忘了/符号
def user_profile(name):
    """Renders a dynamic page with data passed into the templates."""
    # 1. 准备要传递给模版的数据
    user_tasks = [
        "Complete Day 25 Python course",
        "Practice Flask templating",
        "Prepare for Day 26"
    ]
    # 2. calling render_template, pass the template name and data
    # 'username=name' means that there is a variable named as 'username' in the template, and its value is that of the variable named as 'name' in Python.
    # 'tasks = user_tasks' is the same as that above
    return  render_template(
        'user_profile.html',
        username = name,
        tasks = user_tasks
    )

@app.route("/show")
def show():
    show_list = [i for i in range(100)]
    html_list = "<h1> Number List</h1><ul>"
    for num in show_list:
        html_list += f"<li>{num}</li>"
    html_list += "</ul>"
    return html_list


if __name__ == "__main__":
    app.run(host="0.0.0.0",port=80,debug=True)


