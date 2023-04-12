import yagmail
import os

# email details
sender_email = "testman.washere@gmail.com"
sender_password = "yyckcoqxdjhuiojk"
# "vsaipranav2004@gmail.com"
receiver_emails = 'satyammishra9050@gmail.com'
subject = "Intruder detected"
body = "We have detected some motion during your absence.\n Check the below attached file."

def send(filename):
    # attachment details
    filepath = os.path.join(os.getcwd(), filename)

    # create the yagmail object
    yag = yagmail.SMTP(sender_email, sender_password)

    # attach the video file
    yag.send(
        to=receiver_emails,
        subject=subject,
        contents=[body, filepath]
    )

send('test.txt')