from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from backend.routers import chat, staff

app = FastAPI()

# mount static file
app.mount('/static', StaticFiles(directory='backend/static', html=True), name='static')

#api calls
app.include_router(staff.router,prefix="/api")

#websocket for chat
# Dictionary to store connected WebSocket clients
connected_users = {}
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # can alter with time
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def get():
    with open('backend/static/adminlearningears.html') as f:
        lines = " ".join(f.readlines())
    return HTMLResponse(content=lines,status_code=200)

manager = chat.connectionmanager
@app.websocket("/ws/{client_id}")
async def websocket_endpoint(websocket: WebSocket, client_id: int):
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            
            # await manager.send_personal_message(f"{data}", websocket)
            await manager.broadcast(f"{data}")
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        await manager.broadcast(f"Client #{client_id} left the chat")
