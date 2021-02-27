import paho.mqtt.client as paho
import json
client = paho.Client(client_id = "Trainees")

def leitor(dados):
    mensagem = dados
    if dados["modo"] == 1:
        mensagem["modo"] = 0
    client.publish("czar_telecomando", payload = json.dumps(mensagem), qos = 1)

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("czar_telecomando")
    client.subscribe("czar_telemetria")

def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
    print( msg.topic == "czar_telemetria")
    if msg.topic == "czar_telemetria":
        leitor(json.loads(msg.payload))
    
  
client = paho.Client()

client.on_connect = on_connect
client.on_message = on_message

client.connect("test.mosquitto.org", 1883, 60)


client.loop_forever()

