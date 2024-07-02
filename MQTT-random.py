import paho.mqtt.client as mqtt
import json
import time
import random

# Configurații MQTT
mqtt_broker = "mqtt.beia-telemetrie.ro"
mqtt_port = 1883
mqtt_topic = "/training/device/Crina-Bolocan/"

# Funcție pentru simularea datelor
def simulate_data():
    temperature = round(random.uniform(5.0, 40.0), 2)
    humidity = round(random.uniform(30.0, 60.0), 2)
    return {"temperature": temperature, "humidity": humidity}

def on_connect(client, userdata, flags, rc):
    print(f"Connected to MQTT broker with result code {str(rc)}")

def on_publish(client, userdata, mid):
    print(f"Published message with MID {mid}")

# Creare client MQTT
client = mqtt.Client()
client.on_connect = on_connect
client.on_publish = on_publish

# Conectare la broker MQTT
client.connect(mqtt_broker, mqtt_port, 60)
client.loop_start()

try:
    while True:
        # Simulare date
        data = simulate_data()

        # Trimitere date MQTT
        payload = json.dumps(data)
        client.publish(mqtt_topic, payload)

        print(f"Published: {payload} to topic {mqtt_topic}")
        time.sleep(10)  # Așteaptă 10 secunde între trimiterea de date

except KeyboardInterrupt:
    print("Exiting...")
    client.loop_stop()
    client.disconnect()
