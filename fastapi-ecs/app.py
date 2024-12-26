from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/connect")
async def connect():
    print("/connect endpoint is invoked")
    return {"message": "Connection successful"}

@app.post("/joinroom")
async def join_room():
    print("/joinroom endpoint is invoked")
    return {"message": "Room joined successfully"}

@app.get("/disconnect")
async def disconnect():
    print("/disconnect endpoint is invoked")
    return {"message": "Disconnected successfully"}