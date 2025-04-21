from flask import Flask, render_template, jsonify
app = Flask(_name_)

@app.route("/")
def index():
    return "hello from flask"

app.run(host = "0.0.0.0")
