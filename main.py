from flask import Flask, render_template, request


app = Flask(__name__)



# ### **Problem 1:**

# Create a simple Flask application with the following specifications:

# - It should have at least three routes: **`/`**, **`/greet/<username>`**, and **`/farewell/<username>`**.
#     - **`/`** should display a welcome message.
#     - **`/greet/<username>`** should display a greeting message for the user specified 
#       in **`<username>`**. For example, if you navigate to **`/greet/John`**, it should display "Hello, John!".
#     - **`/farewell/<username>`** should display a farewell message for the user specified in **`<username>`**. 
# For example, if you navigate to **`/farewell/John`**, it should display "Goodbye, John!".



@app.route('/')
def hello_world():
    return '📍🥳 Welcome to the F L A S K, World! '

@app.route('/greet/<string:username>')
def greeting_username(username):
    return f"Hello {username}"

@app.route('/farewell/<string:username>')
def farewell_username(username):
    return f"Goodbye, {username}"


### **Problem 2:**

# Create a basic CRUD (Create, Read, Update, Delete) application without using a database:

# - It should have the following routes: **`/create`**, **`/read`**, **`/update`**, **`/delete`**.
#     - **`/create`** should be a form where the user can input data to create a new entry in a Python dictionary.
#     - **`/read`** should display the current state of the dictionary.
#     - **`/update`** should be a form where the user can update the value of an existing entry in the dictionary.
#     - **`/delete`** should be a form where the user can delete an existing entry from the dictionary.




data = {}  # Dictionary to store the entries

print(data,"🥳 hicd vcsdm x xmsc ")
@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        key = request.form['key']
        value = request.form['value']
        print(key,value)
        data[key] = value
        return f"Entry created: {key} - {value}"
    return render_template('create.html')

@app.route('/read')
def read():
    return data

@app.route('/update', methods=['GET', 'POST'])
def update():
    if request.method == 'POST':
        key = request.form['key']
        if key in data:
            value = request.form['value']
            data[key] = value
            return f"Entry updated: {key} - {value}"
        else:
            return f"No entry found for key: {key}"
    return render_template('update.html')

@app.route('/delete', methods=['GET', 'POST'])
def delete():
    if request.method == 'POST':
        key = request.form['key']
        if key in data:
            del data[key]
            return f"Entry deleted: {key}"
        else:
            return f"No entry found for key: {key}"
    return render_template('delete.html')






















if __name__ == '__main__':
    app.run(debug=True)