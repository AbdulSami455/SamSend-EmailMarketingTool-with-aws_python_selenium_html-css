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
import writetemplates as wt
import listcompose as lc
def send_email():
    sender_email = sender_email_entry.get()
    receiver_email = receiver_email_entry.get()
    email_body = email_body_entry.get("1.0", "end-1c")  # Get text from the Text widget
    email_subject = email_subject_entry.get()

    # Replace this with your email sending logic
    # For example, you can use the smtplib library to send emails

    # After sending the email, you can clear the entry fields
    sender_email_entry.delete(0, "end")
    receiver_email_entry.delete(0, "end")
    email_body_entry.delete("1.0", "end")
    email_subject_entry.delete(0, "end")
# Create the main window
root = tk.Tk()
root.title("SamSend Email Marketing Tool")
root.geometry("1000x600")


def composeemailf():
  #frame=event.widget
  root.destroy()
  cw.compose()

def writetemplatesf():
   root.destroy()
   wt.display_and_send_template()
def composelistf():
   root.destroy()
   lc.list()

# Create a frame
composeemail = tk.Frame(master=root,bg="lightblue")
composeemail.place(x=70, y=180, relwidth=0.2, relheight=0.4)

buttonemail = tk.Button(root, text="Write Email", command=composeemailf,bg="lightblue")
buttonemail.place(x=130,y=430)

writetemplate=tk.Frame(master=root,bg="lightblue")
writetemplate.place(x=380,y=180,relwidth=0.2,relheight=0.4)

buttontemplate = tk.Button(root, text="Write Templates", command=writetemplatesf,bg="lightblue")
buttontemplate.place(x=410,y=430)

list=tk.Frame(master=root,bg="lightblue")
list.place(x=690,y=180,relwidth=0.2,relheight=0.4)

buttonlist = tk.Button(root, text="ComposeList", command=composelistf,bg="lightblue")
buttonlist.place(x=660,y=430)

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

