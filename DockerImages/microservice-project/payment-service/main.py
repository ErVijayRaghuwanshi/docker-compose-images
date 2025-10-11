from fastapi import FastAPI
import requests
import socket
import threading
import time

app = FastAPI()

@app.get("/get-info")
def get_info():
    return {"message": "Payment Info fetched"}

@app.post("/make-payment")
def make_payment():
    return {"message": "Payment completed"}

def register_service():
    consul_url = "http://consul:8500/v1/agent/service/register"
    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)

    payload = {
        "Name": "payment-service",
        "ID": "payment-service",
        "Address": ip,
        "Port": 5002,
        "Check": {
            "HTTP": f"http://{ip}:5002/get-info",
            "Interval": "10s"
        }
    }
    while True:
        try:
            requests.put(consul_url, json=payload)
            break
        except Exception as e:
            time.sleep(2)

threading.Thread(target=register_service).start()
