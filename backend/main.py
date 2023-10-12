from pathlib import Path

from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles

from backend.routers import case, chat, messages, staff

app = FastAPI()

# mount static file
app.mount('/static', StaticFiles(directory='backend/static', html=True), name='static')

#api calls
app.include_router(staff.router,prefix="/api")
app.include_router(messages.router,prefix="/api")
app.include_router(case.router,prefix="/api")

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

@app.get("/admin")
async def get_admin():
    with open('backend/static/adminlearningears.html') as f:
        lines = " ".join(f.readlines())
    return HTMLResponse(content=lines,status_code=200)

@app.get("/client")
async def get_client():
    with open('backend/static/clientlearningears.html') as f:
        lines = " ".join(f.readlines())
    return HTMLResponse(content=lines,status_code=200)


@app.get("/therapist")
async def ge_therapistt():
    with open('backend/static/therapist_view.html') as f:
        lines = " ".join(f.readlines())
    return HTMLResponse(content=lines,status_code=200)

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"Message text was: {data}")

manager = chat.connectionmanager
@app.websocket("/ws/{client_id}")
async def websocket_endpoint(websocket: WebSocket, client_id: int):
    await manager.connect(websocket)
    global msgs
    msgs=[]
    try:
        while True:
            data = await websocket.receive_text()
            print(msgs)
            print(data)
            msgs.append(data)
            # await manager.send_personal_message(f"{data}", websocket)
            await manager.broadcast(msgs)
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        await manager.broadcast(f"Client #{client_id} left the chat")
