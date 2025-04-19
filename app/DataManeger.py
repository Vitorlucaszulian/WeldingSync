from Config import Config
from Mock import generate_mock_data

# Isso pode ser substituído por cache, banco, etc
latest_data = {}

def update_data(data):
    global latest_data
    latest_data = data

def get_latest_data():
    if Config.USE_MOCK:
        return generate_mock_data()
    return latest_data or {}
