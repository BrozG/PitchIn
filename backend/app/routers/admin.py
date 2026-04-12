from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from app.core.config import settings

router = APIRouter()
security = HTTPBasic()

def verify_admin(credentials: HTTPBasicCredentials):
    correct_username = credentials.username == settings.admin_username
    correct_password = credentials.password == settings.admin_password
    if not (correct_username and correct_password):
        raise HTTPException(
            status_code=401,
            detail="Invalid admin credentials",
            headers={"WWW-Authenticate": "Basic"},
        )
    return credentials.username

@router.get("/pending-founders")
async def get_pending_founders(admin: str = Depends(verify_admin)):
    return {"founders": []}

@router.post("/approve/{founder_id}")
async def approve_founder(founder_id: str, admin: str = Depends(verify_admin)):
    return {"message": f"Founder {founder_id} approved"}

@router.post("/reject/{founder_id}")
async def reject_founder(founder_id: str, admin: str = Depends(verify_admin)):
    return {"message": f"Founder {founder_id} rejected"}