import tkinter as tk
import seswithpython as sp

# Function to display the existing templates and send the template data
def display_and_send_template():
    # Function to send the template data
    def send_template():
        template_name = template_name_entry.get()
        template_body = template_body_entry.get("1.0", tk.END)[:-1]  # Remove the trailing newline character
        template_subject = template_subject_entry.get()
        template_html = template_html_entry.get("1.0", tk.END)[:-1]  # Remove the trailing newline character

        # Here, you can use the 'template_name', 'template_body', 'template_subject', and 'template_html'
        # variables to send the data to your desired function or perform any other action.

    templates = sp.list_templates()
    template_names = [template['Name'] for template in templates['TemplatesMetadata']]

    window = tk.Tk()
    window.geometry("800x600")

    # Create a label for the heading
    heading_label = tk.Label(window, text="Templates", font=("Helvetica", 16))
    heading_label.pack(pady=10)  # Add some padding

    # Create a text box to display the template names
    text_box = tk.Text(window, height=10, width=40)
    text_box.place(x=25, y=25)
    text_box.pack()

    # Insert the template names into the text box
    for name in template_names:
        text_box.insert(tk.END, name + "\n")

    # Entry fields for template name, body, subject, and HTML
    template_name_label = tk.Label(window, text="Template Name:")
    template_name_label.pack()
    template_name_entry = tk.Entry(window)
    template_name_entry.pack()

    template_body_label = tk.Label(window, text="Template Body:")
    template_body_label.pack()
    template_body_entry = tk.Text(window, height=5, width=40)
    template_body_entry.pack()

    template_subject_label = tk.Label(window, text="Template Subject:")
    template_subject_label.pack()
    template_subject_entry = tk.Entry(window)
    template_subject_entry.pack()

    template_html_label = tk.Label(window, text="Template HTML:")
    template_html_label.pack()
    template_html_entry = tk.Text(window, height=5, width=40)
    template_html_entry.pack()

    # Button to send template data
    send_button = tk.Button(window, text="Send Template", command=send_template)
    send_button.pack()

    window.mainloop()

# Call the display_and_send_template function to display template names and send template data
display_and_send_template()
