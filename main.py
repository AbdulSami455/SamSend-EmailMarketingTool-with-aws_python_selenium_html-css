'''from flask import Flask,render_template,jsonify
import seswithpython as sp
app=Flask(__name__)


@app.route("/")
def mainpage():
    return render_template('index.html')

#
app.run()
'''
import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("SamSend Email Marketing Tool")
root.geometry("1000x600")

# Create a frame
composeemail = tk.Frame(master=root)
composeemail.place(x=25, y=80, relwidth=0.6, relheight=0.4)

# Add a label to the frame
label = tk.Label(composeemail, text="This is a label inside the frame")
label.pack()  # Pack the label to make it visible inside the frame

root.mainloop()

