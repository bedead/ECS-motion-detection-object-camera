import yagmail
import os

# email details
sender_email = "testman.washere@gmail.com"
sender_password = "yyckcoqxdjhuiojk"
receiver_emails = ["vsaipranav2004@gmail.com",'satyammishra9050@gmail.com']
subject = "Video attachment"
body = "Please see the attached video file."

def send(filename):
    # attachment details
    filepath = os.path.join(os.getcwd(), filename)

    # create the yagmail object
    yag = yagmail.SMTP(sender_email, sender_password)

    # attach the video file
    yag.send(
        to=receiver_emails,
        subject=subject,
        contents=[body, filepath],
    )
