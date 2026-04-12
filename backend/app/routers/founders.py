from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import HTTPBearer
from pydantic import BaseModel
from typing import List, Optional
import uuid

router = APIRouter()
security = HTTPBearer()

# Step models
class PersonalInfo(BaseModel):
    full_name: str
    phone: str
    linkedin_url: str
    country: str

class CompanyInfo(BaseModel):
    company_name: str
    website: Optional[str]
    industry: str
    stage: str
    year_founded: Optional[int]
    team_size: Optional[int]
    co_founders: Optional[int]

class TractionInfo(BaseModel):
    mrr: float = 0
    mau: Optional[int]
    key_metric: Optional[str]
    accelerator: Optional[str]

class FundingAsk(BaseModel):
    amount_raising: float
    equity_offered: Optional[float]
    use_of_funds: str
    prev_funding: Optional[str]

class ProofInfo(BaseModel):
    pitch_deck_url: Optional[str]
    one_line_pitch: str
    problem_description: str

class FounderProfile(BaseModel):
    step1: PersonalInfo
    step2: CompanyInfo
    step3: TractionInfo
    step4: FundingAsk
    step5: ProofInfo

@router.post("/submit")
async def submit_founder_profile(profile: FounderProfile, credentials = Depends(security)):
    # In real implementation, save to database
    return {"message": "Founder profile submitted", "status": "pending"}

@router.get("/status/{user_id}")
async def get_founder_status(user_id: str):
    return {"status": "pending", "payment_status": "unpaid"}

@router.post("/payment-webhook")
async def payment_webhook():
    # Handle payment confirmation
    return {"success": True}