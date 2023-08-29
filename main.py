from flask import Flask,render_template,jsonify

app=Flask(__name__)


@app.route("/")
def mainpage():
    return render_template('index.html')
,

app.run()
