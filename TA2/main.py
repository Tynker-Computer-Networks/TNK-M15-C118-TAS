import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from tkinter import *


class EmailSenderApp(Tk):
    def __init__(self):
        super().__init__()
        self.title("Email Sender")

        self.frame = Frame()
        self.frame.grid(column=0, row=0, padx=10, pady=10)

        Label(self.frame, text="Sender's Email:").grid(
            column=0, row=0, sticky="w")
        self.sender_email_entry = Entry(self.frame)
        self.sender_email_entry.grid(
            column=1, row=0, padx=10, pady=5, columnspan=2)

        Label(self.frame, text="Sender's Password:").grid(
            column=0, row=1, sticky="w")
        self.sender_password_entry = Entry(self.frame, show="*")
        self.sender_password_entry.grid(
            column=1, row=1, padx=10, pady=5, columnspan=2)

        Label(self.frame, text="Recipient's Email:").grid(
            column=0, row=2, sticky="w")
        self.recipient_email_entry = Entry(self.frame)
        self.recipient_email_entry.grid(
            column=1, row=2, padx=10, pady=5, columnspan=2)

        Label(self.frame, text="Subject:").grid(column=0, row=3, sticky="w")
        self.subject_entry = Entry(self.frame)
        self.subject_entry.grid(column=1, row=3, padx=10, pady=5, columnspan=2)

        Label(self.frame, text="Message:").grid(column=0, row=4, sticky="w")
        self.message_body_text = Text(self.frame, width=40, height=10)
        self.message_body_text.grid(
            column=1, row=4, padx=10, pady=5, columnspan=2)

        # Call send_single_email function on button click
        self.send_button = Button(
            self.frame, text="Send Email", command=self.send_single_email)
        self.send_button.grid(column=1, row=5, padx=10, pady=10, columnspan=2)

    def send_single_email(self):
        #  Replace input with tkinter label values
        # sender_email = input("Enter Sender Email\n")
        # sender_password = input("Enter Sender Password\n")
        # recipient_email = input("Enter Recipient Email\n")
        # subject = input("Enter Email Subject\n")
        # message_body = input("Enter Message\n")

        sender_email = self.sender_email_entry.get()
        sender_password = self.sender_password_entry.get()
        recipient_email = self.recipient_email_entry.get()
        subject = self.subject_entry.get()
        message_body = self.message_body_text.get("1.0", "end")

        try:
            smtp_server = smtplib.SMTP("smtp.gmail.com", 587)
            smtp_server.starttls()
            smtp_server.login(sender_email, sender_password)

            message = MIMEMultipart()
            message["From"] = sender_email
            message["To"] = recipient_email
            message["Subject"] = subject
            message.attach(MIMEText(message_body, "plain"))

            smtp_server.sendmail(
                sender_email, recipient_email, message.as_string())
            smtp_server.quit()
            print("Email Sent", "Email sent successfully!")

        except Exception as e:
            print("Error", f"An error occurred: {str(e)}")


def main():
    app = EmailSenderApp()
    app.mainloop()


if __name__ == "__main__":
    main()
