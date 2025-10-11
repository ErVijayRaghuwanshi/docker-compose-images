from fastapi import FastAPI
import requests
import socket
import threading
import time

app = FastAPI()

@app.get("/get-video")
def get_video():
    return {"message": "Video fetched"}

@app.post("/upload-video")
def upload_video():
    return {"message": "Video uploaded"}

def register_service():
    consul_url = "http://consul:8500/v1/agent/service/register"
    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)

    payload = {
        "Name": "video-service",
        "ID": "video-service",
        "Address": ip,
        "Port": 5001,
        "Check": {
            "HTTP": f"http://{ip}:5001/get-video",
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