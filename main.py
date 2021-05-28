import smtplib
# please note to got to https://myaccount.google.com/lesssecureapps and
# turn it off to allow gmail to send
# creates SMTP session
s = smtplib.SMTP("smtp.gmail.com", 587)
sender_email_id = "aaliyahjar13@gmail.com"
receiver_email_id = "zaidflandorp4@gmail.com"
password = input("Enter senders email password")
#starts TLS for security
s.starttls()
# Authentification
s.login(sender_email_id, password)
# message to be sent
message = "When your wrist like this, you don't check for forcast cos everyday it's gonna rain\n"
message = message + ""
# sending the mail
s.sendmail(sender_email_id, receiver_email_id, message)
# terminating the session
s.quit()
