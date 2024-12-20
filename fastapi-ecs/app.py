from fastapi import FastAPI, WebSocket

app = FastAPI()

@app.get("/")
def root():
    return {"status": "healthy"}

@app.get("/api")
async def read_root():
    return {"message": "Hello from FastAPI"}

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    await websocket.send_text("Hello from FastAPI WebSocket")
    while True:
        try:
            data = await websocket.receive_text()
            await websocket.send_text(f"Message received: {data}")
        except:
            break
    await websocket.close()
