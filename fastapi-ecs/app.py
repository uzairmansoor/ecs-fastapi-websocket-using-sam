from fastapi import FastAPI

app = FastAPI()

@app.get("/api")
async def read_root():
    return {"message": "Hello from FastAPI"}

@app.get("/health")
async def root():
    return {"message": "Welcome to the Fast APIs"}

@app.get("/connect")
async def connect():
    print("/connect endpoint is invoked")
    return {"message": "Connection successful"}

@app.post("/joinroom")
async def join_room():
    print("/joinroom endpoint is invoked")
    return {"message": "Room joined successfully"}

@app.post("/exitroom")
async def disconnect():
    print("/exitroom endpoint is invoked")
    return {"message": "Exit Room successfully"}