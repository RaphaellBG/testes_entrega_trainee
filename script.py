#código exemplo de publish em um tópico mqtt hospedado em 'test.mosquitto.org'
#na avaliação da entrega, o valores associados a cada dado serão alterados com intenção 
#de validar a interpretação realizada por cada equipe da telemetria

import json 
import paho.mqtt.client as paho
import time
import sys

if __name__ == "__main__":
    client = paho.Client()
    if client.connect("test.mosquitto.org", 1883, 60) == 0 :
        print("Conectado")
        dados = {
            "id": 1,
            "telemetrias": {
                "IMU": [0, 0, 180],
                "SOC": 30,
                "Temp1": 30.3,
                "Hall" : -60
              },
            "tempo" : time.time(),
            "Mem_livre" : 0xFF0F10
        }
    client.publish("czar_telemetria", payload = json.dumps(dados), qos = 1, retain=True)
else:
    print("Falha na conexão com broker")
    sys.exit(-1)