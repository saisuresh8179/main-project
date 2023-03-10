from flask import Flask, render_template
from project import main1
from project1 import main2
app = Flask(__name__)

# two decorators, same function
@app.route('/')
@app.route('/index.html')
def index():
    return render_template('index.html')

@app.route('/run_function1', methods=['POST'])
def run_function1():
    # code to run your function goes here
    try:
        main1()
    # code to be executed
    except Exception as e:
        # handle the exception
        print("Error occurred: ", str(e))
    finally:
    # code to be executed after try and except blocks
        return "thank you"

@app.route('/run_function2', methods=['POST'])
def run_function2():
    # code to run your function goes here
    return main2()


if __name__ == '__main__':
    app.run(debug=True)