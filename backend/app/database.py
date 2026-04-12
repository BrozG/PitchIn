from supabase import create_client, Client
from app.core.config import settings
import logging

logger = logging.getLogger(__name__)

# Initialize Supabase clients with error handling for development
try:
    supabase_client: Client = create_client(
        settings.supabase_url,
        settings.supabase_anon_key
    )
    supabase_admin_client: Client = create_client(
        settings.supabase_url,
        settings.supabase_service_role_key
    )
    logger.info("Supabase clients initialized successfully")
except Exception as e:
    logger.warning(f"Failed to initialize Supabase clients: {e}")
    # Create mock clients for development
    class MockClient:
        def __getattr__(self, name):
            return lambda *args, **kwargs: {"data": [], "error": None}
    
    supabase_client = MockClient()
    supabase_admin_client = MockClient()