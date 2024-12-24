import paho.mqtt.client as mqtt

class MQTTHandler:
    def __init__(self, client_id, broker_address, port=1883, keep_alive=60):
        self.client_id = client_id
        self.broker_address = broker_address
        self.port = port
        self.keep_alive = keep_alive
        self.client = mqtt.Client(client_id)
        
        # Set up callbacks
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message

    def on_connect(self, client, userdata, flags, rc):
        if rc == 0:
            print(f"{self.client_id} connected to MQTT Broker!")
        else:
            print(f"Failed to connect, return code {rc}")

    def on_message(self, client, userdata, message):
        print(f"Message received on {message.topic}: {message.payload.decode()}")

    def connect(self):
        self.client.connect(self.broker_address, self.port, self.keep_alive)
        self.client.loop_start()

    def subscribe(self, topic):
        self.client.subscribe(topic)
        print(f"{self.client_id} subscribed to {topic}")

    def publish(self, topic, message):
        self.client.publish(topic, message)
        print(f"Published message to {topic}: {message}")

    def disconnect(self):
        self.client.loop_stop()
        self.client.disconnect()
