import json as js
import sys
import time
import random
import paho.mqtt.client as paho


client = paho.Client()
if client.connect("test.mosquitto.org", 1883, 60) != 0 :
    print("Falha na conexão com broker")
    sys.exit(-1)
print("conectado")

for i in range (10):
    vbat = round(random.uniform(2, 3.9),1) #Volts
    modo = random.randint(1,3)
    soc = random.randint(85,100) #%
    temp_int = round(random.uniform(-10, 25),2) #°C
    euler1 = round(random.uniform(-180,180),1) #°
    euler2 = round(random.uniform(-180,180),1) #° 
    euler3 = round(random.uniform(-180,180),1) #°

    dados = {
        "identificador": i,
        "hora": time.time(),
        "modo": modo,
        "telemetrias": [
            {"adcs": [euler1, euler2, euler3]},
            {"eps": [vbat, soc]},
            {"tcs": temp_int}
        ],
    }
    client.publish("czarspace_telemetria", js.dumps(dados))
    time.sleep(5)