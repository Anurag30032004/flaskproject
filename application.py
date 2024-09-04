from flask import Flask, render_template, request, flash # type: ignore

application = Flask(__name__)
application.secret_key = "manbearpig_MUDMAN888"

@application.route("/")
def index():
	flash("what's your name?")
	return render_template("index.html")

@application.route("/greet", methods=['POST', 'GET'])
def greeter():
	flash("Hi " + str(request.form['name_input']) + ", great to see you!")
	return render_template("index.html")