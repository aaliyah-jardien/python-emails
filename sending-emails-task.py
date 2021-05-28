import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender_email_id = "aaliyahjar13@gmail.com"
receiver_email_id = ["thapelo@lifechoices.co.za", "uthmaanbreda@gmail.com", "zaidflandorp4@gmail.com"]
password = input("Enter your password")
subject = "Greetings"

msg = MIMEMultipart()
msg['From'] = sender_email_id
msg['To'] = ", ".join(receiver_email_id)
msg['Subject'] = subject
body = "Daily reminder: You are amazing."
msg.attach(MIMEText(body, 'plain'))
text = msg.as_string()
s = smtplib.SMTP('smtp.gmail.com', 587)

# start TLS for security
s.starttls()
# Authentication
s.login(sender_email_id, password)
# message to be sent

# sending the mail

s.sendmail(sender_email_id, receiver_email_id, text)

# terminating the session
s.quit()

