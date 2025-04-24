from flask import Flask, render_template, jsonify
from Mqtt import Mqtt
from Config import Config

app = Flask(__name__)
mqtt = Mqtt()

if not Config.USE_MOCK:
    mqtt.start()  # só conecta ao broker se mock estiver desativado

@app.route("/")
def index():
    return render_template("Dashboar.html")

@app.route("/data")
def get_data():
    return jsonify(mqtt.get_latest_data())

app.run(host="0.0.0.0")
