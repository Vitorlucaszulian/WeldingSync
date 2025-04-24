import random
from datetime import datetime, timedelta

def generate_mock_data():
    start_time = datetime.now() - timedelta(seconds=random.randint(60, 300))
    end_time = datetime.now()
    cycle_time = (end_time - start_time).total_seconds()

    return {
        "timestamp": end_time.strftime("%Y-%m-%d %H:%M:%S"),
        "current": round(random.uniform(120, 150), 2),
        "voltage": round(random.uniform(20, 25), 2),
        "wire_speed": round(random.uniform(5, 10), 2),
        "job": f"JOB{random.randint(100,999)}",
        "workstation": f"EST{random.randint(1,5):02}",
        "startProgram": start_time.strftime("%Y-%m-%d %H:%M:%S"),
        "endProgram": end_time.strftime("%Y-%m-%d %H:%M:%S"),
        "operator_id": f"OP{random.randint(100,999)}",
        "program_name": f"PROG{random.randint(1,10)}",
        "material_type": random.choice(["Aço Inox", "Aço Carbono", "Alumínio"]),
        "thickness": round(random.uniform(1.0, 10.0), 1),
        "gas_type": random.choice(["ARGÔNIO+CO2", "ARGÔNIO PURO", "MISTO"]),
        "error_code": random.choice([0, 0, 0, 1, 2]),
        "cycle_time": round(cycle_time, 2),
        "machine_status": random.choice(["RUNNING", "IDLE", "ERROR"]),
        "arc_on_time": round(cycle_time * random.uniform(0.6, 0.95), 2),
        "energy_consumed": round(random.uniform(0.1, 0.5), 2)
    }
