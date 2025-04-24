import paho.mqtt.client as mqtt
import json
from Config import Config
from Mock import generate_mock_data

class Mqtt: 
    #Construtor 
    def __init__(self):
        self.client             = mqtt.Client
        self.client.on_connect  = self.on_connect()
        self.client.on_message  = self.on_message
        self.get_latest_data    = {}  

    #metodo chamado sempre que o mqqt se conecta
    def on_connect(self, client, userdata, flags, rc):
        print(f"[MQTT] Conectado ao broker {Config.MQTT_BROKER}:{Config.MQTT_PORT} | Código: {rc}")
        client.subscribe(Config.MQTT_TOPIC)
        print(f"[MQTT] Inscrito no tópico: {Config.MQTT_TOPIC}")

    #metodo chamado sempre que recebe uma mensagem
    def on_message(self, client, userdata, msg):
        payload_str = msg.payload.decode("utf-8")
        topic = msg.topic
        print(f"[MQTT] Mensagem recebida | Tópico: {topic} | Payload: {payload_str}")

        try:
            data = json.loads(payload_str)
        except json.JSONDecodeError:
            print("[MQTT] Erro ao decodificar payload")
            return

        self.tratar_mensagem(topic, data)

    #metodo para tratamento de mensagem 
    def tratar_mensagem(self, topic, data):
        # Armazena por tópico (pode evoluir para salvar em banco depois)
        self.latest_data[topic] = data

    #metodo utilizado para solicitações das mesagem recebidas  
    def get_latest_data(self):
        if Config.USE_MOCK:
            return generate_mock_data()
        return self.latest_data or {}
    
    #start do servico
    def start(self):
        print(f"[MQTT] Iniciando cliente MQTT...")
        self.client.connect(Config.MQTT_BROKER, Config.MQTT_PORT, Config.MQTT_KEEPALIVE)
        self.client.loop_start()
