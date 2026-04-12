-- Pitch In Database Schema for Supabase PostgreSQL

-- Enable UUID extension
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- Users table (Supabase Auth already has a users table, we'll create a profiles table)
-- We'll assume Supabase Auth provides auth.users with id, email, etc.
-- We'll create a separate table for our app-specific user data
CREATE TABLE IF NOT EXISTS public.users (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    auth_id UUID REFERENCES auth.users(id) ON DELETE CASCADE,
    email TEXT UNIQUE NOT NULL,
    role TEXT CHECK (role IN ('founder','investor')) NOT NULL,
    created_at TIMESTAMPTZ DEFAULT NOW(),
    last_active TIMESTAMPTZ DEFAULT NOW()
);

-- Founder profiles
CREATE TABLE IF NOT EXISTS public.founder_profiles (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id UUID NOT NULL REFERENCES public.users(id) ON DELETE CASCADE,
    -- Step 1
    full_name TEXT NOT NULL,
    phone TEXT,
    linkedin_url TEXT NOT NULL,
    country TEXT NOT NULL,
    -- Step 2
    company_name TEXT NOT NULL,
    website TEXT,
    industry TEXT NOT NULL,
    stage TEXT NOT NULL,
    year_founded INTEGER,
    team_size INTEGER,
    co_founders INTEGER,
    -- Step 3
    mrr NUMERIC DEFAULT 0,
    mau INTEGER,
    key_metric TEXT,
    accelerator TEXT,
    -- Step 4
    amount_raising NUMERIC NOT NULL,
    equity_offered NUMERIC,
    use_of_funds TEXT,
    prev_funding TEXT,
    -- Step 5
    pitch_deck_url TEXT,
    one_line_pitch VARCHAR(150) NOT NULL,
    problem_description TEXT,
    -- Status
    status TEXT CHECK (status IN ('pending','approved','rejected','paused')) DEFAULT 'pending',
    payment_status TEXT CHECK (payment_status IN ('unpaid','paid')) DEFAULT 'unpaid',
    payment_platform TEXT,
    payment_id TEXT,
    paid_at TIMESTAMPTZ,
    active_until TIMESTAMPTZ,
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW()
);

-- Investor profiles
CREATE TABLE IF NOT EXISTS public.investor_profiles (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id UUID NOT NULL REFERENCES public.users(id) ON DELETE CASCADE,
    -- Step 1
    full_name TEXT NOT NULL,
    linkedin_url TEXT NOT NULL,
    country TEXT NOT NULL,
    -- Step 2
    investor_type TEXT NOT NULL,
    check_size_range TEXT NOT NULL,
    sectors TEXT[] NOT NULL,
    stage_pref TEXT[] NOT NULL,
    geo_focus TEXT[] NOT NULL,
    -- Step 3
    looking_for_text TEXT,
    deals_per_month TEXT,
    capital_status TEXT,
    -- Subscription
    subscription_tier TEXT CHECK (subscription_tier IN ('free','connector','partner')) DEFAULT 'free',
    subscription_status TEXT CHECK (subscription_status IN ('active','cancelled','expired')) DEFAULT 'active',
    subscription_end_date TIMESTAMPTZ,
    revenue_cat_id TEXT,
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW()
);

-- Match requests
CREATE TABLE IF NOT EXISTS public.match_requests (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    investor_id UUID NOT NULL REFERENCES public.users(id) ON DELETE CASCADE,
    founder_id UUID NOT NULL REFERENCES public.users(id) ON DELETE CASCADE,
    note TEXT,
    status TEXT CHECK (status IN ('pending','accepted','declined','expired')) DEFAULT 'pending',
    deal_room_id UUID,
    created_at TIMESTAMPTZ DEFAULT NOW(),
    responded_at TIMESTAMPTZ,
    expires_at TIMESTAMPTZ DEFAULT NOW() + INTERVAL '7 days'
);

-- Deal rooms
CREATE TABLE IF NOT EXISTS public.deal_rooms (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    match_request_id UUID NOT NULL REFERENCES public.match_requests(id) ON DELETE CASCADE,
    investor_id UUID NOT NULL REFERENCES public.users(id) ON DELETE CASCADE,
    founder_id UUID NOT NULL REFERENCES public.users(id) ON DELETE CASCADE,
    deal_stage TEXT CHECK (deal_stage IN ('intro','due_diligence','term_sheet','closed','passed')) DEFAULT 'intro',
    created_at TIMESTAMPTZ DEFAULT NOW(),
    last_activity TIMESTAMPTZ DEFAULT NOW()
);

-- Deal room messages
CREATE TABLE IF NOT EXISTS public.deal_room_messages (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    room_id UUID NOT NULL REFERENCES public.deal_rooms(id) ON DELETE CASCADE,
    sender_id UUID NOT NULL REFERENCES public.users(id) ON DELETE CASCADE,
    content TEXT,
    file_url TEXT,
    file_name TEXT,
    file_size BIGINT,
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- Payments
CREATE TABLE IF NOT EXISTS public.payments (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id UUID NOT NULL REFERENCES public.users(id) ON DELETE CASCADE,
    type TEXT CHECK (type IN ('founder_fee','investor_subscription')) NOT NULL,
    amount NUMERIC NOT NULL,
    currency VARCHAR(3) DEFAULT 'USD',
    platform TEXT CHECK (platform IN ('razorpay','stripe','apple_iap','google_play')) NOT NULL,
    payment_id TEXT,
    status TEXT CHECK (status IN ('pending','completed','failed')) DEFAULT 'pending',
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- Admin actions
CREATE TABLE IF NOT EXISTS public.admin_actions (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    admin_id UUID NOT NULL REFERENCES public.users(id) ON DELETE CASCADE,
    target_user_id UUID NOT NULL REFERENCES public.users(id) ON DELETE CASCADE,
    action TEXT CHECK (action IN ('approve','reject','request_info','ban')) NOT NULL,
    note TEXT,
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- Indexes for performance
CREATE INDEX idx_founder_profiles_user_id ON public.founder_profiles(user_id);
CREATE INDEX idx_founder_profiles_status ON public.founder_profiles(status);
CREATE INDEX idx_investor_profiles_user_id ON public.investor_profiles(user_id);
CREATE INDEX idx_investor_profiles_subscription_tier ON public.investor_profiles(subscription_tier);
CREATE INDEX idx_match_requests_investor_id ON public.match_requests(investor_id);
CREATE INDEX idx_match_requests_founder_id ON public.match_requests(founder_id);
CREATE INDEX idx_match_requests_status ON public.match_requests(status);
CREATE INDEX idx_deal_rooms_match_request_id ON public.deal_rooms(match_request_id);
CREATE INDEX idx_deal_room_messages_room_id ON public.deal_room_messages(room_id);
CREATE INDEX idx_payments_user_id ON public.payments(user_id);

-- Row Level Security (RLS) will be enabled later via Supabase dashboard
-- ALTER TABLE ... ENABLE ROW LEVEL SECURITY;

-- Functions for updated_at triggers
CREATE OR REPLACE FUNCTION update_updated_at_column()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = NOW();
    RETURN NEW;
END;
$$ language 'plpgsql';

CREATE TRIGGER update_founder_profiles_updated_at BEFORE UPDATE ON public.founder_profiles FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();
CREATE TRIGGER update_investor_profiles_updated_at BEFORE UPDATE ON public.investor_profiles FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();