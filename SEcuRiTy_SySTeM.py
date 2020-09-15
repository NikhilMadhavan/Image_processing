from subprocess import call
import time
import os
import glob
import smtplib
import base64
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart 
from email.MIMEText import MIMEText
import subprocess
import sys
gmail_user="deathblinkgaming@gmail.com"
gmail_pwd="jesus bradley"
FROM="deathblinkgaming@gmail.com"
TO=["albinus20@gmail.com"]
subprocess.Popen("test.txt",shell=True).communicate()
time.sleep(1)

msg=MIMEMultipart()
time.sleep(1)

msg["Subject"]="Smart ATM security bish"
body="test.txt"
##body=sys.argv[1]+sys.argv[2]

msg.attach(MIMEText(body,"test.txt"))
time.sleep(1)
try:
    server=smtplib.SMTP("smtp.gmail.com",587)
    print("smtp.gmail")
    server.ehlo()
    print("ehlo")
    server.starttls()
    print("starttls")
    print("read mail")
    server.login(gmail_user,gmail_pwd)
    print("reading mail and password bish")
    server.sendmail(FROM,TO,msg.as_string())
    print("from")
    server.close()
    print("Successfully sent the mail bish")
except:
    print("FAIL NUB!!!")

    
