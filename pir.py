import time
import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO
from time import sleep

test = "someone is in HOME!"


localhost = "3.121.31.186"
port = 1883
timeout = 60
topic = "/ALARM/ALARM"
Qos = 0
message_payload = test

def on_connect(client, userdata, flags, rc):
  print("error = "+str(rc))

PIR_input = 36				#read PIR Output
LED = 18				#LED for signalling motion detected
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)		#choose pin no. system
GPIO.setup(PIR_input, GPIO.IN)
GPIO.setup(LED, GPIO.OUT)
GPIO.output(LED, GPIO.LOW)
sleep(2)
while True:
#when motion detected turn on LED
    if(GPIO.input(PIR_input)):
        GPIO.output(LED, GPIO.HIGH)
        print ("detected")
        client = mqtt.Client()
        client.on_connect = on_connect
        client.connect(localhost, port, timeout)
        client.publish(topic, message_payload, 0)
        time.sleep(2)
        client.disconnect()

    else:
        GPIO.output(LED, GPIO.LOW)
        print ("nie")
        sleep(1.1)

GPIO.cleanup()

