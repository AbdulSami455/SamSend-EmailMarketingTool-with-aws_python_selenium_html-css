from flask import Flask,render_template,jsonify

app=Flask(__name__)


@app.route("/")
def mainpage():
    return "Hello"

app.run(port=6000,debug=True)
