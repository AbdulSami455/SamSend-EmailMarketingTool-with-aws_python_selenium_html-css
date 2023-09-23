import tkinter as tk
import seswithpython as sp

def compose():
    dash = tk.Tk()
    dash.geometry("600x400")
    dash.title("Email Composer")

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

        sp.sendemail(sender_email, receiver_email, email_body, email_subject)

    def send_template_email():
        template_name = template_name_entry.get()
        sender_email = sender_email_entry.get()
        receiver_email = receiver_email_entry.get()

        # Replace this with your template email sending logic
        # Use the template_name, sender_email, and receiver_email as needed

        # After sending the template email, you can clear the template_name entry
        template_name_entry.delete(0, "end")
        sp.sendtemplatedemail(template_name,sender_email,receiver_email)
    # Sender Email Entry
    sender_email_label = tk.Label(dash, text="Sender Email:")
    sender_email_label.pack()
    sender_email_entry = tk.Entry(dash)
    sender_email_entry.pack()

    # Receiver Email Entry
    receiver_email_label = tk.Label(dash, text="Receiver Email:")
    receiver_email_label.pack()
    receiver_email_entry = tk.Entry(dash)
    receiver_email_entry.pack()

    # Email Subject Entry
    email_subject_label = tk.Label(dash, text="Subject:")
    email_subject_label.pack()
    email_subject_entry = tk.Entry(dash)
    email_subject_entry.pack()

    # Email Body Text Widget
    email_body_label = tk.Label(dash, text="Email Body:")
    email_body_label.pack()
    email_body_entry = tk.Text(dash, height=10, width=40)
    email_body_entry.pack()

    # Send Button for Regular Email
    send_button = tk.Button(dash, text="Send", command=send_email)
    send_button.pack()

    # Template Name Entry
    template_name_label = tk.Label(dash, text="Template Name:")
    template_name_label.pack()
    template_name_entry = tk.Entry(dash)
    template_name_entry.pack()

    # Send Button for Template Email
    send_template_button = tk.Button(dash, text="Send Template Email", command=send_template_email)
    send_template_button.pack()

    dash.mainloop()

# Call the compose function to create the GUI
#compose()
