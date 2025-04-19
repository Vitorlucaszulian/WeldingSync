import random
from datetime import datetime

def generate_mock_data():
    return {
        "timestamp": datetime.now().strftime("%H:%M:%S"),
        "current": round(random.uniform(120, 150), 2),
        "voltage": round(random.uniform(20, 25), 2),
        "wire_speed": round(random.uniform(5, 10), 2)
    }
