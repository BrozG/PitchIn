from fastapi import APIRouter, Depends
from fastapi.security import HTTPBearer
from pydantic import BaseModel

router = APIRouter()
security = HTTPBearer()

class MatchRequest(BaseModel):
    founder_id: str
    note: str

@router.post("/request")
async def request_match(req: MatchRequest, credentials = Depends(security)):
    return {"match_id": "mock", "status": "pending"}

@router.get("/my-requests")
async def get_my_requests(credentials = Depends(security)):
    return {"requests": []}