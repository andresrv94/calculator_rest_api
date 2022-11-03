from flask import Flask,request,render_template
# from flask import request
import calc_functions

app = Flask(__name__)

#This should return a rendered HTML page explaining what can be done with the API
@app.route("/")
def info():
    return render_template('info.html')

@app.route("/sum", methods=["POST"])
def f_sum():
    return { "result" : calc_functions.sum(float(request.form['x']), float(request.form['y'])) }

@app.route("/substract", methods=["POST"])
def f_substract():
    return { "result" : calc_functions.substract(float(request.form['x']), float(request.form['y'])) }

@app.route("/multiply", methods=["POST"])
def f_multiply():
    return { "result" : calc_functions.multiply(float(request.form['x']), float(request.form['y'])) }

@app.route("/divide", methods=["POST"])
def f_divide():
    return { "result" : calc_functions.divide(float(request.form['x']), float(request.form['y'])) }

