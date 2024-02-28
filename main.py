from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse
from models.connection_manager import ConnectionManager
from frontend.html import html

app = FastAPI()

manager = ConnectionManager()

#Al entrar al "/" muestra el html definido 
@app.get("/")
async def get():
    return HTMLResponse(html)

#
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