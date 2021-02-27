import json 
import paho.mqtt.client as paho

if __name__ == "__main__":
    client = paho.Client()
if client.connect("test.mosquitto.org", 1883, 60) == 0 :
    dados = {
        "identificador": 1,
        "modo": 1,
        "telemetrias": [
            {"adcs": [0, 0, 180]},
            {"eps": [1]},
            {"tcs": 30}
        ],
    }
    client.publish("topico_envio_czar", payload = json.dumps(dados), qos = 1)
else:
    print("Falha na conexão com broker")
    sys.exit(-1)