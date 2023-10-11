from fastapi import FastAPI
from fastapi import (WebSocket, WebSocketDisconnect)
from backend.routers import staff
from backend.routers import chat


app = FastAPI()

#api calls
app.include_router(staff.router,prefix="/api")

#websocket for chat
@app.websocket("/api/chat")
async def chat(websocket: WebSocket):
    manager = chat.manager
    # sender = websocket.cookies.get("X-Authorization")
    sender = True
    if sender:
        await manager.connect(websocket, sender)
        response = {
            "sender": sender,
            "message": "got connected"
        }
        await manager.broadcast(response)
        try:
            while True:
                data = await websocket.receive_json()
                await manager.broadcast(data)
        except WebSocketDisconnect:
            manager.disconnect(websocket, sender)
            response['message'] = "left"
            await manager.broadcast(response)