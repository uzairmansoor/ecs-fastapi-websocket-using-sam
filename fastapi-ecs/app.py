from fastapi import FastAPI

app = FastAPI()

@app.get("/connect")
async def connect():
    print("/connect endpoint is invoked")
    return {"message": "Connection successful"}

@app.post("/joinroom")
async def join_room():
    print("/joinroom endpoint is invoked")
    return {"message": "Room joined successfully"}

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8080)
