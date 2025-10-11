from fastapi import FastAPI
import requests
import socket
import threading
import time

app = FastAPI()

@app.get("/login")
def login():
    return {"message": "Login Successful"}

@app.get("/register")
def register():
    return {"message": "Register Successful"}

def register_service():
    consul_url = "http://consul:8500/v1/agent/service/register"
    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)

    payload = {
        "Name": "auth-service",
        "ID": "auth-service",
        "Address": ip,
        "Port": 5000,
        "Check": {
            "HTTP": f"http://{ip}:5000/login",
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
