import json 
import paho.mqtt.client as paho
import time
if __name__ == "__main__":
    client = paho.Client()
    if client.connect("test.mosquitto.org", 1883, 60) == 0 :
        print("Conectado")
        dados = {
            "identificador": 1,
            "adcs_on": True,
            "telemetrias": [
                {"IMU": [0, 0, 180]},
                {"Vbat": 2.1},
                {"Temp1": 30.3},
                {"Hall" : -60}
            ],
            "tempo" : time.time(),
            "Mem_livre" : 0xFF0F10
        }
    client.publish("czar_telemetria", payload = json.dumps(dados), qos = 1, retain=True)
else:
    print("Falha na conexão com broker")
    sys.exit(-1)