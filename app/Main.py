from flask import Flask, render_template, jsonify
from DataManeger import get_latest_data

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("dashboard.html")

@app.route('/data')
def data():
    return jsonify(get_latest_data())

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
