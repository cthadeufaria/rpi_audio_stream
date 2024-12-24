from mqtt_handler import MQTTHandler


class Client:
    def __init__(self, client_id, broker_address, port=1883):
        self.client_id = client_id
        self.broker_address = broker_address
        self.port = port
        self.client = MQTTHandler(client_id)

    def connect(self):
        self.client.connect(self.broker_address, self.port)

    def subscribe(self, topic):
        self.client.subscribe(topic)

    def disconnect(self):
        self.client.disconnect()

    def on_message(self, client, userdata, message):
        print(f"Message received on {message.topic}: {message.payload.decode()}")
    
    def play_audio(self, message):
        self.client.publish("play/all", message)
        print(f"Published message to play/all: {message}")
        
# Client setup
client1 = MQTTHandler(client_id="client1", broker_address="localhost", port=1883)

# Connect and subscribe to both its unique and broadcast topics
client1.connect()
client1.subscribe("play/all")
client1.subscribe("play/client1")

# Keep the client running to listen for incoming messages
try:
    while True:
        pass  # Keep the script running to listen for messages
except KeyboardInterrupt:
    print("Disconnecting client1...")
finally:
    client1.disconnect()