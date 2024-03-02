from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse, FileResponse
from models.connection_manager import ConnectionManager
import frontend
from fastapi.staticfiles import StaticFiles

app = FastAPI()

manager = ConnectionManager()

app.mount("/static", StaticFiles(directory="frontend"), name="static")

#Al entrar al "/" muestra el html definido 
@app.get("/", response_class=HTMLResponse)
async def get():
    return FileResponse("frontend/index.html")


@app.websocket("/ws/{client_id}")
async def websocket_endpoint(websocket: WebSocket, client_id: int):
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            await manager.send_personal_message(f"Escribiste: {data}", websocket)
            await manager.broadcast(f"El cliente #{client_id} dice: {data}")
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        await manager.broadcast(f"El cliente #{client_id} ha salido del chat")