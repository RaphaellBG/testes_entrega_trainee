import paho.mqtt.client as paho

client = paho.Client()

if client.connect("test.mosquitto.org", 1883, 60) != 0 :
    print("Could not connect")
    sys.exit(-1)


#client.publish("statusczarspace", "Hello")

client.disconnect()