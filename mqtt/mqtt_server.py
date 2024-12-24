from mqtt_handler import MQTTHandler
import time


# Server setup
server = MQTTHandler(client_id="secretary", broker_address="localhost", port=1883)

# Connect to the broker and start publishing
server.connect()

# Send a broadcast message to all clients
broadcast_topic = "play/school-bell"
server.publish(broadcast_topic, "Play audio on all clients")

# Send a message to a specific client (e.g., client1)
client_specific_topic = "play/all"
server.publish(client_specific_topic, "Play audio on client 1")

# Disconnect after publishing
time.sleep(2)  # Allow time for messages to be sent
server.disconnect()
