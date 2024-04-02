#!/usr/bin/env python3

from flask import Flask
#To create a Flask applcation instance
app = Flask(__name__)

#Define a route for the root URL ('/')
@app.route('/')
def index():
    #Return an HTML string as the response
 return '<h1>Python Operations with Flask Routing and Views</h1>'

#To define a route that accepts a string parameter
@app.route('/print/<string:str>')
def print_string(str):
    print(str)
    return str

#Define a route for the endpoint
@app.route('/hello')
def hello():
    #Define a string variable
    text = 'hello\n'
    print(text)
    return text

# Define a route that accepts an integer parameter
@app.route('/count/<int:num>')
def count(num):
    #Generate a string containing numbers from O to num
    numbers = '\n'.join(str(i) for i in range(num))
    #To add a newline charater at the end
    numbers += '\n'
    return numbers

# Define a route for the '/math/<num1>/<operation>/<num2>' endpoint
@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math(num1, operation, num2):
    result = None
     # Perform the specified operation on the two numbers
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        result = num1 / num2
    elif operation == '%':
        result = num1 % num2
    
    # Check if a valid result was computed    
    if result is not None:
         # Return the result as a string
        return str(result)
    else:
        return 'Invalid operation'
# Run the Flask application if this script is executed directly            
if __name__ == '__main__':
    #Start the Flask development server on port 5555 in debug mode
    app.run(port=5555, debug=True)
