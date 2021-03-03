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
            "id": A, #identificador da telemetria
            "telemetrias": {
                "IMU": [0, 0, 180], #leituras da IMU (ângulos de Euler), em graus
                "SOC": 30, #estado da carga, em porcentagem
                "Temp1": 30.3, #temperatura, em °C
                "Hall" : -60, #medida sensor hall, em V
              },
            "tempo" : time.time(), #tempo, em s
            "Mem_livre" : 0xFF0F10  #memória disponível, em bytes
        }
    client.publish("czar_telemetria", payload = json.dumps(dados), qos = 1, retain=True)
else:
    print("Falha na conexão com broker")
    sys.exit(-1)