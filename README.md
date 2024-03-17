# Automatic-Email-Scheduler
This Python application allows users to schedule emails to be sent automatically at a specified date and time. It provides a graphical user interface (GUI) built using Tkinter for user interaction.

# Features
Schedule Emails: Users can input recipient email addresses, subject, message content, and the scheduled time for sending the email.
Validation: The application validates the scheduled time to ensure it's set in the future and in the correct format (YYYY-MM-DD HH:MM:SS).
SMTP Integration: Utilizes the Simple Mail Transfer Protocol (SMTP) to send emails. Currently configured for Gmail SMTP server.
Error Handling: Provides informative error messages in case of failures during email sending.

# Requirements
Python 3.x
Tkinter (usually included in Python standard library)
smtplib (for sending emails)
email.mime (for email composition)
threading (for scheduling)
