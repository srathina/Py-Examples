import smtplib

#Get the details
s1 = input("Enter sender email:")
r1 = input("Enter receiver email:")
sub = input("Enter subject:")
msg = input("Enter email message:")

#email constraints
sender = s1 #"mailtorsaravan@gmail.com"
receiver = r1 #"mailtorsaravan@gmail.com"
subject = sub #"Hello, world !"
msg = msg #"I am RSK"

#Subject: string is very important as that will place the subject content into subject field of the email
email = f'Subject: {subject}\n\n{msg}'

#get the password
with open("password.txt", 'r') as f:
    password = f.read()

#create smtp session
s = smtplib.SMTP("smtp.gmail.com", 587)

#start TLS security to encrypt all the email message
s.starttls()

try:
    #login
    s.login(sender, password)
    #send the mail
    s.sendmail(sender,receiver, email)
    #sucess message
    print("Email sent sucessfully")
except:
    print("Authentication failed")

#close the connection
s.quit()




