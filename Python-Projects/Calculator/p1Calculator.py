#create a calcualtor program with flask with basic operation to advanced
from flask import Flask, render_template, request
app = Flask(__name__) # create an instance of the Flask class and assign it to the variable app
@app.route('/') #  this line use to create a route for the home page
def home():
    return render_template('calculator.html') # this line use to render the calculator.html template when the home page is accessed 
@app.route('/calculate', methods=['POST']) # this line use to create a route for the calculate page and specify that it will only accept POST requests
def calculate():    
    num1 = float(request.form['num1']) 
    num2 = float(request.form['num2']) 
    operation = request.form['operation'] 
    if operation == 'add':     
         result = num1 + num2 
    elif operation == 'subtract':
        result = num1 - num2  
    elif operation == 'multiply': 
        result = num1 * num2  
    elif operation == 'divide':
        if num2 != 0: 
            result = num1 / num2
        else:
            result = 'Error: Division by zero' 
    else:
        result = 'Invalid Operation' 
    return render_template('result.html', result=result) # this line use to render the result.html template and pass the result variable to it when the calculate page is accessed
if __name__ == '__main__': # this line use to check if the script is being run directly and not imported as a module
    app.run(debug=True) # this line use to run the Flask application in debug mode, which allows for easier debugging and automatic reloading of the server when changes are made to the code
    