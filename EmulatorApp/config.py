from randomGenerator import *

BROKER_URL="broker.hivemq.com"

SUB_TOPICS=['ACY6P234H1FD/dosingControl'] #topics that this app will subscribe to

PUB_PAYLOAD_CONFIG={
     ########MQTT CONFIGURATIONS################################
    "PUBLISHING_TOPIC":"smartdosing/ACY6P234H1FD",
    "PUBLISHING_INTERVAL": 5, #seconds
}
PUB_PAYLOAD={
    #####################Payload Below#################
    "macAddress":"ACY6P234H1FD",
    "temperature":RandomFloatNumberAsString(20.0,45.1),
    "humidity":RandomIntegerAsString(1,100),
    "liquidtemperature":RandomFloatNumberAsString(10.0,150.2),
    "tds":RandomIntegerAsString(10,400),
    "ph":RandomFloatNumberAsString(2.1,9.1),
    "orp":RandomIntegerAsString(5,30),
    "co2":RandomIntegerAsString(8,91)
}