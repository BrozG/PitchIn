"""
RevenueCat integration for subscription management.
Handles webhooks from RevenueCat and updates user subscription status.
"""

import logging
from typing import Optional, Dict, Any
from app.database import supabase_admin_client
from app.core.config import settings

logger = logging.getLogger(__name__)

class RevenueCatService:
    @staticmethod
    def handle_webhook(event: Dict[str, Any]) -> bool:
        """
        Process a RevenueCat webhook event.
        Expected event types: INITIAL_PURCHASE, RENEWAL, CANCELLATION, etc.
        """
        try:
            event_type = event.get('type')
            user_id = event.get('app_user_id')
            product_id = event.get('product_id')
            period_type = event.get('period_type')  # 'NORMAL', 'INTRO', 'TRIAL'
            purchased_at = event.get('purchased_at_ms')
            expires_at = event.get('expires_at_ms')

            logger.info(f"RevenueCat webhook: {event_type} for user {user_id}")

            # Map product IDs to our tiers
            tier = RevenueCatService._map_product_to_tier(product_id)
            if not tier:
                logger.warning(f"Unknown product_id: {product_id}")
                return False

            # Update investor profile
            supabase_admin_client.table('investor_profiles').update({
                'subscription_tier': tier,
                'subscription_status': 'active',
                'subscription_end_date': expires_at,
                'revenue_cat_id': user_id,
            }).eq('revenue_cat_id', user_id).execute()

            # Also update users table if needed
            logger.info(f"Updated subscription for {user_id} to {tier}")
            return True
        except Exception as e:
            logger.error(f"Error processing RevenueCat webhook: {e}")
            return False

    @staticmethod
    def _map_product_to_tier(product_id: str) -> Optional[str]:
        """
        Map RevenueCat product ID to our internal tier.
        """
        mapping = {
            'connector_monthly': 'connector',
            'connector_annual': 'connector',
            'partner_monthly': 'partner',
            'partner_annual': 'partner',
            'connector_monthly_ios': 'connector',
            'partner_monthly_ios': 'partner',
        }
        for key, tier in mapping.items():
            if key in product_id:
                return tier
        return None

    @staticmethod
    def get_subscription_status(user_id: str) -> Dict[str, Any]:
        """
        Fetch subscription status for a user from RevenueCat (mock).
        In production, you would call RevenueCat API.
        """
        # Mock response
        return {
            'active': True,
            'tier': 'connector',
            'expires_at': '2026-12-31T23:59:59Z',
            'platform': 'ios',
        }