from fastapi import FastAPI
from fastapi import (WebSocket, WebSocketDisconnect)
from backend.routers import staff
from backend.routers import chat
from fastapi.responses import HTMLResponse


app = FastAPI()

#api calls
app.include_router(staff.router,prefix="/api")

#websocket for chat
manager = chat.connectionmanager
@app.websocket("/ws/{client_id}")
async def websocket_endpoint(websocket: WebSocket, client_id: int):
    print(client_id)
    await manager.connect(websocket)
    while True:
        data = await websocket.receive_text()
        await manager.broadcast(f"Client {client_id}: {data}")

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"Message text was: {data}")