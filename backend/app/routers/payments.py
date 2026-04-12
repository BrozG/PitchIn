from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import HTTPBearer
from pydantic import BaseModel
from typing import Optional

router = APIRouter()
security = HTTPBearer()

class CreatePaymentIntent(BaseModel):
    amount: float
    currency: str = "USD"
    type: str  # "founder_fee" or "investor_subscription"

@router.post("/create-intent")
async def create_payment_intent(req: CreatePaymentIntent, credentials = Depends(security)):
    # In real implementation, integrate Stripe/Razorpay
    return {
        "client_secret": "mock_client_secret",
        "payment_id": "mock_payment_id"
    }

@router.post("/webhook/stripe")
async def stripe_webhook():
    # Handle Stripe webhook
    return {"received": True}

@router.post("/webhook/razorpay")
async def razorpay_webhook():
    # Handle Razorpay webhook
    return {"received": True}