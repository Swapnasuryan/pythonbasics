import smtplib

sender = "sender@gmail.com"
reciever = "reciever@gmail.com"
password = "password123"
subject = "Python email test"
body = "I wrote an email!  :D"

#Header
message = f""""From: rangdalakshara {sender}             # triple quotes are used for multiple lines
To: rangdal akshara{reciever}
subject: {subject}\n
{body}
"""

server = smtplib.SMTP("smtp.gmail.com",587)
server.starttls()

try:
    server.login(sender,password)
    print("Logged in...")
    server.sendmail(sender,reciever,message)
    print("Email has been sent!")

except smtplib.SMTPAuthenticationError:
    print("Unable to sign in")