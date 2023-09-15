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
from PIL import ImageTk, Image
import composeemailwindow as cw
# Create the main window
root = tk.Tk()
root.title("SamSend Email Marketing Tool")
root.geometry("1000x600")


def composeemail():
  #frame=event.widget
  cw.compose()

#def writetemplates():

#def composelist():


# Create a frame
composeemail = tk.Frame(master=root,bg="lightblue")
composeemail.place(x=70, y=180, relwidth=0.2, relheight=0.4)

buttonemail = tk.Button(root, text="Click Me!", command=composeemail)
buttonemail.place(x=130,y=430)


writetemplate=tk.Frame(master=root,bg="lightblue")
writetemplate.place(x=380,y=180,relwidth=0.2,relheight=0.4)

list=tk.Frame(master=root,bg="lightblue")
list.place(x=690,y=180,relwidth=0.2,relheight=0.4)

image = Image.open("list.png")
image = image.resize((200, 240), Image.ANTIALIAS)
image_tk = ImageTk.PhotoImage(image)
label = tk.Label(list, image=image_tk)
label.configure(text="")
label.pack()

image = Image.open("compose-mail-2.png")
image = image.resize((200, 240), Image.ANTIALIAS)
image_tk2= ImageTk.PhotoImage(image)
label2 = tk.Label(composeemail, image=image_tk2)
label2.configure(text="")
label2.pack()


image = Image.open("templates.png")
image = image.resize((200, 240), Image.ANTIALIAS)
image_tk3= ImageTk.PhotoImage(image)
label3 = tk.Label(writetemplate, image=image_tk3)
label3.configure(text="")
label3.pack()

root.mainloop()

