import time
import random
import paho.mqtt.client as mqtt
from datetime import  datetime
from config import *
msgV = ""
topicV = ""

def printSeparator():
    print("-"*10)
def getTimestamp():
    now=datetime.now()
    timestamp = now.strftime("%m%d%Y%H%M%S%f")
    return timestamp

def on_connect(client, userdata, rc):
    #print("Connected with result code "+str(rc))
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    for i in range(0,len(SUB_TOPICS)):
        client.subscribe(SUB_TOPICS[i])

# The callback for when a PUBLISH message is received from the server.


def on_message(client, userdata, msg):

    global msgV, topicV
    #print(msg.topic+" "+str(msg.payload))
    topicV = str(msg.topic)
    msgV = str((msg.payload).decode('utf-8'))
    printSeparator()
    print("Topic: "+topicV)
    print("Data: "+msgV)
    printSeparator()

clientID_prefix = ""
for i in range(0, 6):
    clientID_prefix = clientID_prefix + str(random.randint(0, 99999))


client = mqtt.Client("C1"+clientID_prefix)
#client.on_connect = on_connect
client.on_message = on_message

client.connect(BROKER_URL, 1883, 60)
for i in range(0,len(SUB_TOPICS)):
    client.subscribe(SUB_TOPICS[i])


client.loop_start()


def sendDataToServer_MQTT():
    
    global client
    TOPICV=PUB_PAYLOAD_CONFIG["PUBLISHING_TOPIC"]
    client.publish(TOPICV, str(PUB_PAYLOAD))
    printSeparator()
    print("Published at ",TOPICV)
    print(PUB_PAYLOAD)
    printSeparator()


oldtime = time.time()

while 1:
    if time.time() - oldtime > int(PUB_PAYLOAD_CONFIG['PUBLISHING_INTERVAL']):  # get data after every 2 seconds
        oldtime = time.time()
        try:
            
            sendDataToServer_MQTT()
        except Exception as e:
            print("e: ", e)