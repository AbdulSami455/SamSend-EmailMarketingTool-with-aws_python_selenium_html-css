from flask import Flask,render_template,jsonify
import seswithpython as sp
app=Flask(__name__)


@app.route("/")
def mainpage():
    return render_template('index.html')


app.run()
