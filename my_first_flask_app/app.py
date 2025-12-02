from flask import Flask, render_template, request, url_for, redirect  # import flask render_template request url_for and redirect
import sqlite3

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

        # --- database operation ---
        # 1. connect database
        conn = sqlite3.connect('messages.db')
        # 2. achieve the cursor
        c = conn.cursor()
        # 3. execute the insert. use ? as a positional symbol.
        c.execute("INSERT INTO messages (visitor_name, visitor_message) VALUES (?, ?)",(visitor_name,visitor_message))
        # 4. commit the affair
        conn.commit()
        # 5. close the connection
        conn.close()
        # --- the operation of database finished ---




        """
        # In the real app instance, you will store the data into database. However, we only print it to show that we received the request.
        print("--- New Message Received ---")
        print(f"From: {visitor_name}")
        print(f"Message: {visitor_message}")
        print("----------------------------")
        #redirect to the "Thank_you" page after dealing with the data
        return redirect(url_for("thank_you"))
        """

    # Otherwise, the required method is GET, and we only need to show the form page.
    return render_template("contact.html")

@app.route("/messages")
def show_messages():
    conn = sqlite3.connect("messages.db")
    c = conn.cursor()
    # execute the select statement，and retrieve  all comments in reverse chronological order.
    c.execute("SELECT visitor_name,visitor_message,timestamp FROM messages ORDER BY timestamp DESC")
    # fetchall() retrieve all results of requisition
    all_messages = c.fetchall()
    conn.close()
    return render_template("messages.html",messages=all_messages)



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
            if login_name =="admin" and login_password=="password123":
                print("Admin login successful!")
            else:
                print("Invalid credentials!")
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


