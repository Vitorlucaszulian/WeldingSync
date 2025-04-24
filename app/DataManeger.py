from Config import Config
from Mock import generate_mock_data

class DataManeger:
    def __init__(self):
        self.latest_data = {}

    def tratarMensagem(self, topic, payload):
        # Aqui você pode fazer parsing do payload, validar, salvar, etc.
        print(f"[DataManager] Tratando mensagem do tópico {topic}")
        # Simplesmente armazenando por enquanto
        self.latest_data[topic] = payload

    def update_data(self, data):
        self.latest_data = data

    def get_latest_data(self):
        if Config.USE_MOCK:
            return generate_mock_data()
        return self.latest_data or {}
