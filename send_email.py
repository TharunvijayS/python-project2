import smtplib,ssl

host="smtp.gmail.com"
port=465

username="tharunapp8@gmail.com"
password="vwja mtnn tlob iggd"

receiver="tharunapp8@gmail.com"
context=ssl.create_default_context()

message="""\
subject:Hi!
How are you?
Bye!
"""

with smtplib.SMTP_SSL(host, port, context=context)as server:
    server.login(username,password)
    server.sendmail(username,receiver,message)
