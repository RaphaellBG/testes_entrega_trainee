import time
import sys
import datetime
import random
import paho.mqtt.client as paho

#telemetria 
# flag, tamanho do pacote, hora, modo de operação do satélite, telemetria, subsistema da telemetria, flag

client = paho.Client()
ts = time.time() #timestamp em epoch
print(datetime.datetime.fromtimestamp(ts)) #timestamp formatada - só para visualizar
hora = str(ts)




#switch case iria aqui para gerar telemetrias aleatórias com base na hora da mensagem 
subsistema = "ADCS"
atitude = [23,65,89]
telemetria = ''.join(str(v) for v in atitude)

#publish no tópico definido
if client.connect("test.mosquitto.org", 1883, 60) != 0 :
    print("Falha na conexão com broker")
    sys.exit(-1)

for i in range(10):
    client.publish("czarspace_telemetria", hora+subsistema+telemetria)
    time.sleep(5) #publicar a cada 10 min? 

client.disconnect()
