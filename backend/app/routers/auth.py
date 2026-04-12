from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pydantic import BaseModel, EmailStr
from typing import Optional
import uuid

from app.database import supabase_client
from app.core.config import settings

router = APIRouter()
security = HTTPBearer()

class SignupRequest(BaseModel):
    email: EmailStr
    password: str
    role: str  # 'founder' or 'investor'

class LoginRequest(BaseModel):
    email: EmailStr
    password: str

class TokenResponse(BaseModel):
    access_token: str
    token_type: str
    user_id: str
    role: str

@router.post("/signup")
async def signup(request: SignupRequest):
    # Use Supabase Auth to sign up
    try:
        response = supabase_client.auth.sign_up({
            "email": request.email,
            "password": request.password,
        })
        user = response.user
        if user:
            # Create entry in our users table
            supabase_client.table("users").insert({
                "auth_id": user.id,
                "email": user.email,
                "role": request.role
            }).execute()
            return {"message": "User created successfully", "user_id": user.id}
        else:
            raise HTTPException(status_code=400, detail="Signup failed")
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/login")
async def login(request: LoginRequest):
    try:
        response = supabase_client.auth.sign_in_with_password({
            "email": request.email,
            "password": request.password
        })
        user = response.user
        # Get role from users table
        user_data = supabase_client.table("users").select("role").eq("auth_id", user.id).execute()
        role = user_data.data[0]["role"] if user_data.data else "unknown"
        # In a real app, you'd generate a JWT token
        # For simplicity, we'll return a mock token
        token = "mock-jwt-token-" + str(uuid.uuid4())
        return TokenResponse(
            access_token=token,
            token_type="bearer",
            user_id=user.id,
            role=role
        )
    except Exception as e:
        raise HTTPException(status_code=401, detail="Invalid credentials")

@router.get("/me")
async def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials
    # Validate token (simplified)
    # In real implementation, decode JWT and get user
    return {"user_id": "mock", "role": "founder"}