#import all the libraries we need to run
import RPi.GPIO as GPIO
import time
import sys
import os
from time import sleep
import urllib2
GPIO.setmode(GPIO.BCM)
GPIO.setup(23,GPIO.OUT)
##GPIO.setup(24,GPIO.IN)
#setup our API and delay
myAPI = "RXJAPIRJ8N0PA06V"
myDelay =0.5  #how many seconds between posting data

print ('starting....')
baseURL='https://api.thingspeak.com/update?api_key=%s' % myAPI
print(baseURL)

##trig=23
HIGH=23

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)


##while True:
    ##GPIO.output(trig,False)
    ##time.sleep(0.1)
    ##GPIO.output(trig,True)
    ##time.sleep(0.1)
    ##GPIO.output(trig,False)
    

    ##while GPIO.input(echo)==False:
    ##   pulse_start=time.time()

    ##while GPIO.input(echo)==True:
    ##    pulse_end = time.time()

    ##pulse_duration = pulse_end-pulse_start

    ##distance=pulse_duration*17150
    ##distance=round(distance,2)
      
    ##if (distance>2 and distance<400):
    ##    print("Distance:",distance)
    ##else:
    ##    print("out of range")

while True:
    print (HIGH)

        
          
    urllib2.urlopen(baseURL +"&field1=%s" %str(HIGH))
    sleep(int(myDelay))
