from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from contextlib import asynccontextmanager
import os
from dotenv import load_dotenv

load_dotenv()

from app.routers import auth, founders, investors, matches, deal_rooms, admin, payments
from app.database import supabase_client
from app.core.config import settings

security = HTTPBearer()

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    print("Starting Pitch In API...")
    # Test Supabase connection
    try:
        res = supabase_client.table("users").select("*").limit(1).execute()
        print("Supabase connection successful")
    except Exception as e:
        print(f"Supabase connection error: {e}")
    yield
    # Shutdown
    print("Shutting down Pitch In API")

app = FastAPI(
    title="Pitch In API",
    description="Backend for Pitch In investor-founder matching platform",
    version="1.0.0",
    lifespan=lifespan
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, restrict to mobile app and web admin domains
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(auth.router, prefix="/auth", tags=["Authentication"])
app.include_router(founders.router, prefix="/founders", tags=["Founders"])
app.include_router(investors.router, prefix="/investors", tags=["Investors"])
app.include_router(matches.router, prefix="/matches", tags=["Matches"])
app.include_router(deal_rooms.router, prefix="/deal-rooms", tags=["Deal Rooms"])
app.include_router(admin.router, prefix="/admin", tags=["Admin"])
app.include_router(payments.router, prefix="/payments", tags=["Payments"])

@app.get("/")
async def root():
    return {"message": "Welcome to Pitch In API", "docs": "/docs", "health": "/health"}

@app.get("/health")
async def health():
    return {"status": "healthy", "timestamp": "2026-04-12T11:17:00Z"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)