from flask import Flask,request,render_template,make_response,redirect,url_for
# from flask import request
import calc_functions

app = Flask(__name__)

#This should return a rendered HTML page explaining what can be done with the API
@app.route("/")
def info():
    if request.cookies.get('throttle') == "true":
        print("This user already downloaded this page. Redirecting him to Reddit :D")
        return redirect('https://www.reddit.com')

    resp = make_response(render_template('info.html'))
    resp.set_cookie('throttle', 'true')
    return resp

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

