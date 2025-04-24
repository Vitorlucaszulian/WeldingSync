import paho.mqtt.client as mqtt
from DataManeger        import DataManeger
from Config             import Config

# Classe de controle do serviço MQTT
class MqttService:
    def __init__(self):
        self.client             = mqtt.Client()
        self.client.on_connect  = self.onConnect
        self.client.on_message  = self.onMessage  
        self.data_manager       = DataManeger()  

    # Função chamada quando a conexão com o broker está estabelecida
    def onConnect(self, client, userdata, flags, rc):
        print(f"[mqtt] Conectando ao brocker {Config.MQTT_BROKER}:{Config.MQTT_PORT} com codigo{rc}")
        self.client.subscribe(Config.MQTT_TOPIC)                    #recebe o topico que solicitamos em config
        print (f"[mqtt] inscrito no topico {Config.MQTT_TOPIC}")    #printa o topico onde o brocker foi inscrito 

    # Função chamada quando uma mensagem é recebida
    def onMessage(self, client, userdata, msg):
        payload = msg.payload.decode("utf-8")
        topic = msg.topic                                   
        print(f"[MQTT] Mensagem recebida - Tópico: {topic} | Payload: {payload}")
        self.data_manager.tratarMensagem(topic, payload)

    def start(self):
        print(f"[MQTT] Iniciando conexão com broker: {Config.MQTT_BROKER}:{Config.MQTT_PORT}")
        self.client.connect(Config.MQTT_BROKER, Config.MQTT_PORT, 60)
        self.client.loop_start()