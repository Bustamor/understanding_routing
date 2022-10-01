from ast import Num
from unicodedata import name
from flask import Flask
app=Flask(__name__)

@app.route('/')
def index():
    return "hello Frances!"

# @app.route('/dojo')
# def greet():
#     return "dojo"

@app.route('/say/<word>')
def say(word):
    print(word)
    return "Hello, " + word

@app.route('/repeat/<int:num>/<string:name>')
def repeat(num,name):
    return f"bye {num * name}"

# @app.route('/hello/<string:hello>/<int:num>')
# def hello(hello,num):
#     return f"bye {hello " "* num}"

if __name__=="__main__":
    app.run(debug=True, host="localhost",port=5001)
