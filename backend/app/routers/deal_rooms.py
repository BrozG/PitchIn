from fastapi import APIRouter, Depends, WebSocket
from fastapi.security import HTTPBearer
from pydantic import BaseModel
from typing import List, Optional

router = APIRouter()
security = HTTPBearer()

class Message(BaseModel):
    content: str
    file_url: Optional[str] = None

@router.get("/")
async def list_deal_rooms(credentials = Depends(security)):
    return {"rooms": []}

@router.websocket("/{room_id}/ws")
async def websocket_endpoint(websocket: WebSocket, room_id: str):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"Echo: {data}")