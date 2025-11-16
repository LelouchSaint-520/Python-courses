from flask import Flask, render_template, request, url_for, redirect  # import flask render_template request url_for and redirect
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
        "task1",
        "task2",
        "task3"
    ]
    # 2. calling render_template, pass the template name and data
    # 'username=name' means that there is a variable named as 'username' in the template, and its value is that of the variable named as 'name' in Python.
    # 'tasks = user_tasks' is the same as that above
    if name.lower() == "admin":
        admin = True
    else:
        admin = False

    return render_template(
        'user_profile.html',
                            username = name,
                            tasks = user_tasks,
                            is_admin = admin
                            )

@app.route("/contact",methods=["GET","POST"])
def contact():
    # judge the method of request:
    if request.method == "POST":
        #This is a POST request, we need to deal with a form data
        visitor_name = request.form["visitor_name"]
        visitor_message = request.form["visitor_message"]

        # In the real app instance, you will store the data into database. However, we only print it to show that we received the request.
        print("--- New Message Received ---")
        print(f"From: {visitor_name}")
        print(f"Message: {visitor_message}")
        print("----------------------------")
        #redirect to the "Thank_you" page after dealing with the data
        return redirect(url_for("thank_you"))
    # Otherwise, the required method is GET, and we only need to show the form page.
    return render_template("contact.html")

@app.route("/login", methods=["GET","POST"])
def login():
    if request.method == "POST":
        click_action = request.form.get("action")
        if click_action == "login":
            login_name = request.form["login_name"]
            login_password = request.form["login_password"]
            print("--- Login information ---")
            print(f"Login name is {login_name}")
            print(f"Login Password is {login_password}")
            return redirect(url_for("thank_you"))

        elif click_action == "forget":
            print("--- Forget information ---")
            print("custom forget the login name and password.")
            return redirect(url_for("home"))

        elif click_action == "message":
            message_text = request.form.get("login_remark")
            login_name = request.form.get("login_name", "anonymous")
            print(f"Form: {login_name}")
            print(f"Message: {message_text}")
            return redirect(url_for("home"))

    return render_template("login.html")

@app.route("/thank-you")
def thank_you():
    return render_template("thank_you.html")


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


