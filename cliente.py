import paho.mqtt.client as paho
import json
import time

class aEnviar:
    def __init__(self, dados):
        self.data = dados
        self.telecom = self.create_telecom() 

    def is_temperature_okay(self):
        if (self.data["telemetrias"]["Temp1"] >= 40 or self.data["telemetrias"]["Temp1"] <= -20):
            status = False
        else:
            status = True
        return status 
    
    def is_battery_okay(self):
        if self.data["telemetrias"]["SOC"] < 30:
            status = False
        else:
            status = True
        return status
            
    def create_telecom(self):
        mensagem = dict()
        mensagem["id"] = self.data["id"]
        mensagem["tempo"] = time.time()
        mensagem["telecomandos"] = dict()
        if not self.is_battery_okay():
            mensagem["telecomandos"]["adcs_pw"] = False 
            mensagem["telecomandos"]["tcs_pw"] = False
            mensagem["telecomandos"]["payload_pw"] = False
        elif self.is_battery_okay() and not self.is_temperature_okay():
            mensagem["telecomandos"]["adcs_pw"] = False 
            mensagem["telecomandos"]["tcs_pw"] = True
            mensagem["telecomandos"]["payload_pw"] = False
        elif self.is_battery_okay() and self.is_temperature_okay():
            mensagem["telecomandos"]["adcs_pw"] = True
            mensagem["telecomandos"]["tcs_pw"] = True
            mensagem["telecomandos"]["payload_pw"] = True
        return mensagem
    
    def to_publish(self):
        return json.dumps(self.telecom)    

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("czar_telecomando")
    client.subscribe("czar_telemetria")

def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
    obj = aEnviar(json.loads(msg.payload))
    print(obj.telecom)
    client.publish("czar_telecomando", payload = obj.to_publish(), qos=1)
   

if __name__ == "__main__":   
    client = paho.Client(client_id = "Trainees")

    client.on_connect = on_connect
    client.on_message = on_message

    client.connect("test.mosquitto.org", 1883, 60)


    client.loop_forever()

