from fastapi import FastAPI

app = FastAPI(root_path="/service1", openapi_url="/openapi.json", docs_url="/docs")

@app.get("/ping")
def ping():
    return {"service": "microservice1", "message": "pong"}
