import RPi.GPIO as GPIO
import time
from subprocess import call
import os
import glob
import smtplib
import base64
import subprocess
import sys
from email.mime.multipart import MIMEMultipart 
from email.MIMEText import MIMEText
GPIO.setmode(GPIO.BCM)
TRIG = 23
ECHO = 24
LED1 = 19
LED2 = 12
print ("Water Level Measurement In Progress")


GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(LED1, GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)
GPIO.setup(LED2, GPIO.OUT)

gmail_user="deathblinkgaming@gmail.com"
gmail_pwd="jesus bradley"
FROM="deathblinkgaming@gmail.com"
TO=["albinus20@gmail.com"]

GPIO.output(TRIG, False)
print ("Waiting For Sensor To Settle")
time.sleep(1)
while(True):
    GPIO.output(TRIG, True)
    time.sleep(1)
    GPIO.output(TRIG, False)
    while GPIO.input(ECHO)==0:
        pulse_start = time.time()
    while GPIO.input(ECHO)==1:
        pulse_end = time.time()      

    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17150
    distance = round(distance, 2)
    
    if(distance<=5):
        GPIO.output(LED1, True)
        GPIO.output(LED2, False)
        for msg in range(1):
            msg=MIMEMultipart()
            time.sleep(1)
            msg["subject"]="ALERT!!!"
            body="Switching off the motor in\n 3\n 2\n 1"
            msg.attach(MIMEText(body))
            time.sleep(1)
    
            try:
                server=smtplib.SMTP("smtp.gmail.com",587)
                print"smtp.gmail"
                server.ehlo()
                print"ehlo"
                server.starttls()
                print"starttls"
                server.login(gmail_user,gmail_pwd)
                print"reading mail and password"
                server.sendmail(FROM,TO,msg.as_string())
                print"from"
                server.close()
                print"Successfully sent the mail"
            except:
                print"FAIL NUB!!!"
        break
    else:
       GPIO.output(LED2, True)
       GPIO.output(LED1,False)
    print ("Distance:0",distance,"cm")
    
#body=sys.argv[1]+sys.argv[2]


    

    
#GPIO.cleanup()

