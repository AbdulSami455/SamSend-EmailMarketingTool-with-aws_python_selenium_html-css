import tkinter as tk
import seswithpython as sp


# Function to display the existing templates and send/update template data
def display_and_send_template():
    # Function to send/update the template data
    def send_template():
        template_name = template_name_entry.get()
        template_body = template_body_entry.get("1.0", tk.END)[:-1]  # Remove the trailing newline character
        template_subject = template_subject_entry.get()
        template_html = template_html_entry.get("1.0", tk.END)[:-1]  # Remove the trailing newline character

        # Check if the template name exists, and decide whether to create or update
        if template_name in template_names:
            # Update the existing template
            sp.update_template(template_name, template_subject,template_body)
            print(f"Updated template: {template_name}")
        else:
            # Create a new template
            sp.createtemplate(template_name, template_body, template_subject, template_html)
            print(f"Created template: {template_name}")

        # Clear the entry fields after sending/updating
        clear_fields()

    # Function to clear the entry fields
    def clear_fields():
        template_name_entry.delete(0, tk.END)
        template_body_entry.delete("1.0", tk.END)
        template_subject_entry.delete(0, tk.END)
        template_html_entry.delete("1.0", tk.END)

    # Fetch existing templates
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

    # Button to send/update template data
    send_button = tk.Button(window, text="Send/Update Template", command=send_template)
    send_button.pack()

    window.mainloop()


# Call the display_and_send_template function to display template names and send/update template data
display_and_send_template()
