from flask import Flask, jsonify
from prometheus_flask_exporter import PrometheusMetrics
import time

app = Flask(__name__)
metrics = PrometheusMetrics(app)
start_time = time.time()

@app.route('/')
def home():
    return jsonify({"status": "running", "uptime": round(time.time() - start_time, 2)})

@app.route('/health')
def health():
    return jsonify({"healthy": True}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)