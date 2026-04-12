from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import HTTPBearer
from pydantic import BaseModel
from typing import List, Optional

router = APIRouter()
security = HTTPBearer()

class IdentityInfo(BaseModel):
    full_name: str
    linkedin_url: str
    country: str

class InvestorProfileInfo(BaseModel):
    investor_type: str
    check_size_range: str
    sectors: List[str]
    stage_pref: List[str]
    geo_focus: List[str]

class PreferencesInfo(BaseModel):
    looking_for_text: Optional[str]
    deals_per_month: Optional[str]
    capital_status: Optional[str]

class InvestorProfile(BaseModel):
    step1: IdentityInfo
    step2: InvestorProfileInfo
    step3: PreferencesInfo

@router.post("/submit")
async def submit_investor_profile(profile: InvestorProfile, credentials = Depends(security)):
    return {"message": "Investor profile submitted", "status": "active"}

@router.get("/discover")
async def discover_founders(credentials = Depends(security)):
    # Mock founder cards
    return {
        "founders": [
            {
                "id": "1",
                "company_name": "TechStart Inc",
                "industry": "Fintech",
                "stage": "Seed",
                "amount_raising": 500000,
                "one_line_pitch": "Revolutionizing payments for SMEs",
                "match_score": 85
            },
            {
                "id": "2",
                "company_name": "HealthAI",
                "industry": "Healthtech",
                "stage": "Series A",
                "amount_raising": 2000000,
                "one_line_pitch": "AI‑powered diagnostics platform",
                "match_score": 72
            }
        ]
    }

@router.get("/subscription")
async def get_subscription(credentials = Depends(security)):
    return {"tier": "free", "status": "active"}