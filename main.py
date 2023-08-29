from flask import Flask,render_template,jsonify

app=Flask(__name__)


@app.route("/")
def mainpage():
    return {'Message':'Hello, I m Abdul Sami'}


app.run()
