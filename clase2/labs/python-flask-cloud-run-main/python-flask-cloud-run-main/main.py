import os
import time

from flask import Flask, jsonify
from datetime import datetime

app = Flask(__name__)

startTime = time.time()

@app.route("/")
def hello_world():
    """Example Hello World route."""
    name = os.environ.get("NAME", "World")
    return f"Hello Python {name}!"


@app.route("/health")
def health_check():
    
    system_time = time.time() - startTime
    time_format = "%Y-%m-%d %H:%M:%S"
    data = {
        "status": "success",
        "uptime": datetime.fromtimestamp(system_time).strftime(time_format),
        "timestamp": datetime.now().strftime(time_format)
    }

    return jsonify(data)

@app.route("/api/users")
def api_users():
    
    data = [
      { "id": 1, "name": 'Juan Pérez', "email": 'juan@example.com' },
      { "id": 2, "name": 'María García', "email": 'maria@example.com' },
      { "id": 3, "name": 'Carlos López', "email": 'carlos@example.com' }
    ]

    return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))