import tkinter as tk
from tkinter import messagebox
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time
import threading
from datetime import datetime

def send_email():
    to_email = to_email_entry.get()
    subject = subject_entry.get()
    message = message_text.get(1.0, 'end')
    scheduled_time = scheduled_time_entry.get()
    
    try:
        scheduled_time = datetime.strptime(scheduled_time, '%Y-%m-%d %H:%M:%S')
        current_time = datetime.now()
        time_difference = (scheduled_time - current_time).total_seconds()
        
        if time_difference <= 0:
            messagebox.showerror("Error", "Please enter a future time for scheduling.")
            return
        
    except ValueError:
        messagebox.showerror("Error", "Invalid date/time format. Please use 'YYYY-MM-DD HH:MM:SS'")
        return

    def send_email_thread():
        try:
            smtp_server = 'smtp.gmail.com'  # Update this with your SMTP server
            smtp_port = 465  # Update this with the SMTP port
            username = 'your_email@gmail.com'  # Update this with your email
            password = 'your_email_password'  # Update this with your email password
            
            msg = MIMEMultipart()
            msg['From'] = username
            msg['To'] = to_email
            msg['Subject'] = subject
            msg.attach(MIMEText(message, 'plain'))

            server = smtplib.SMTP_SSL(smtp_server, smtp_port)
            server.login(username, password)
            server.sendmail(username, to_email, msg.as_string())
            server.quit()

            messagebox.showinfo("Success", "Email sent successfully.")
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to send email: {str(e)}")

    threading.Thread(target=send_email_thread).start()

# Create the GUI window
root = tk.Tk()
root.title("Email Scheduler")

# Create and place widgets
to_email_label = tk.Label(root, text="To:")
to_email_label.pack()
to_email_entry = tk.Entry(root)
to_email_entry.pack()

subject_label = tk.Label(root, text="Subject:")
subject_label.pack()
subject_entry = tk.Entry(root)
subject_entry.pack()

message_label = tk.Label(root, text="Message:")
message_label.pack()
message_text = tk.Text(root, height=5, width=40)
message_text.pack()

scheduled_time_label = tk.Label(root, text="Scheduled Time (YYYY-MM-DD HH:MM:SS):")
scheduled_time_label.pack()
scheduled_time_entry = tk.Entry(root)
scheduled_time_entry.pack()

send_button = tk.Button(root, text="Schedule and Send Email", command=send_email)
send_button.pack()

root.mainloop()
