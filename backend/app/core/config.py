from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    # Supabase
    supabase_url: str
    supabase_anon_key: str
    supabase_service_role_key: str
    
    # JWT
    secret_key: str = "your-secret-key-change-in-production"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30
    
    # Resend
    resend_api_key: Optional[str] = None
    from_email: str = "noreply@pitchin.example.com"
    
    # RevenueCat
    revenuecat_api_key: Optional[str] = None
    
    # Stripe
    stripe_secret_key: Optional[str] = None
    stripe_webhook_secret: Optional[str] = None
    
    # Razorpay
    razorpay_key_id: Optional[str] = None
    razorpay_key_secret: Optional[str] = None
    
    # App URLs
    web_app_url: str = "http://localhost:3000"
    mobile_app_scheme: str = "pitchin"
    api_base_url: str = "http://localhost:8000"
    
    # Admin
    admin_username: str = "admin"
    admin_password: str = "admin123"
    
    class Config:
        env_file = ".env"

settings = Settings()