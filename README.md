# 🚀 Pitch In - Where Dreams Meet Capital

> *In the quiet spaces between ambition and reality,<br>
> Where founders whisper their visions to the stars,<br>
> And investors listen with the wisdom of experience,<br>
> There exists a bridge—a meeting place of minds and means.<br>
> This is Pitch In.*

---

<div align="center">

## ⚡ Quick Start

**Ready to launch?** Jump straight to the [QUICKSTART.md](QUICKSTART.md) guide for immediate setup instructions.

[![Get Started](https://img.shields.io/badge/GET_STARTED-Now-C9A84C?style=for-the-badge&logo=rocket)](QUICKSTART.md)
[![View Demo](https://img.shields.io/badge/WATCH_DEMO-Video-080C14?style=for-the-badge&logo=video)](resource/readme-intro.mp4)

</div>

---

## 🎬 Introduction

<div align="center">
  
### 🎥 Platform Demo

<video width="800" controls>
  <img src="resource/Listen Schitts Creek GIF by CBC.gif" alt="Listen Schitts Creek GIF">
  Your browser does not support the video tag. [Download the video](resource/readme-intro.mp4)
</video>

*The video showcases the complete Pitch In experience:*
- ✨ **Splash screen** with elegant animations
- 👥 **Role selection** (Founder vs Investor)
- 📝 **Multi-step onboarding** with progress tracking
- 🔍 **Swipe-based discovery** with glassmorphism effects
- 💰 **Pricing psychology** with tiered subscriptions
- 🤝 **Deal room** with real-time chat
- 🎛️ **Admin dashboard** for founder approval

*Note:* If the video doesn't play directly in GitHub, you can [download it here](resource/readme-intro.mp4) to view locally.

</div>

---

## ✨ What Is Pitch In?

Pitch In is not merely an application; it is a **digital ecosystem** where innovation finds its fuel. A premium investor-founder matching platform that transforms the chaotic dance of fundraising into a graceful, intentional partnership.

### 🌟 The Vision
Imagine a world where:
- **Founders** no longer wander through endless pitch events, hoping to catch the right eye
- **Investors** don't sift through mountains of decks searching for that spark of genius
- **Connections** happen not by chance, but by design—algorithmically curated, psychologically optimized, and beautifully presented

This is the world Pitch In creates.

---

## 🏛️ Architectural Symphony

Pitch In is a **three-part harmony**—each component playing its essential role in the grand composition:

### 1. **📱 Mobile App (React Native + Expo)**
   - *For founders and investors on the move*
   - Glassmorphism design with deep space (#080C14) and golden accents (#C9A84C)
   - Swipe-based discovery with psychology-driven gating
   - Six-step founder onboarding that feels like a guided meditation
   - Four-step investor profiling that understands your thesis
   - Real-time deal rooms where partnerships are born

### 2. **🖥️ Web Admin Dashboard (Next.js 14)**
   - *The conductor's podium*
   - Real-time queue of founder applications awaiting review
   - One-click approval/rejection with thoughtful feedback
   - Analytics dashboard showing the heartbeat of the platform
   - Dark theme that respects the late-night review sessions

### 3. **⚡ Backend API (FastAPI + Supabase)**
   - *The invisible engine*
   - PostgreSQL database with UUIDs and proper constraints
   - Real-time WebSocket connections for deal room chats
   - Payment integration architecture (Stripe, Razorpay, RevenueCat)
   - Authentication that remembers you like an old friend
   - Match algorithms that understand more than numbers

---

## 🎨 Design Philosophy

### The Psychology of Connection
Every pixel, every animation, every interaction in Pitch In is designed with **human psychology** at its core:

- **Anchoring Effect**: Premium pricing tiers establish value perception
- **Scarcity Principle**: Limited slots create urgency without pressure
- **FOMO Dynamics**: "Recently matched" notifications that inspire action
- **Progress Motivation**: Step-by-step onboarding that celebrates small wins
- **Glassmorphism Aesthetic**: Interfaces that feel tangible yet ethereal

### Color Palette as Emotion
- `#080C14` - The depth of space, where ideas are born
- `#C9A84C` - The warmth of gold, the promise of return
- `#1A1F2C` - The structure of night, the framework of dreams
- `#FFFFFF` - The purity of intention, the clarity of vision

---

## 🛠️ What Pitch In Supports

### For Founders 🌱
- **6-Step Intelligent Onboarding**: From idea to investment-ready profile
- **Investor Discovery**: Swipe through curated investor matches
- **Deal Rooms**: Secure spaces for due diligence and negotiation
- **Progress Tracking**: Visual journey from pitch to partnership
- **Psychology-Optimized Pitches**: Templates that speak investor language

### For Investors 💼
- **4-Step Profile Creation**: Define your thesis, preferences, and boundaries
- **Founder Discovery**: Algorithmically matched to your investment sweet spot
- **Tiered Access**: Free previews, paid deep dives
- **Deal Flow Management**: Organize, compare, and track opportunities
- **Real-time Notifications**: When matching founders enter the platform

### For Administrators 🎛️
- **Application Queue**: Review and vet incoming founder profiles
- **Analytics Dashboard**: Platform health, match rates, revenue metrics
- **User Management**: Moderate, support, and guide the community
- **System Configuration**: Tune the algorithms that make magic happen

### Technical Capabilities ⚙️
- **Real-time Chat**: WebSocket-powered deal room conversations
- **Push Notifications**: Timely alerts for matches, messages, and milestones
- **Payment Processing**: Multi-provider integration (Stripe, Razorpay)
- **Subscription Management**: RevenueCat-powered tier access
- **File Upload & Management**: Pitch decks, financials, legal documents
- **Advanced Search & Filtering**: Find exactly what you're looking for

---

## 🚦 How to Run This Symphony

### Prerequisites
- **Node.js 18+** (for mobile and web-admin)
- **Python 3.11+** (for backend)
- **Expo CLI** (`npm install -g expo-cli`)
- **Git** (to clone this repository)

### 🎼 Three-Part Startup Sequence

#### 1. **Start the Backend (The Foundation)**
```bash
cd backend

# Create virtual environment
python -m venv venv

# Activate it (Windows)
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
copy .env.example .env
# Edit .env with your Supabase credentials

# Run the server
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```
**🎯 Expected:** API running at `http://localhost:8000` • Docs at `http://localhost:8000/docs`

#### 2. **Start the Web Admin (The Control Room)**
```bash
cd web-admin

# Install dependencies
npm install

# Run the development server
npm run dev
```
**🎯 Expected:** Dashboard at `http://localhost:3000`

#### 3. **Start the Mobile App (The Experience)**
```bash
cd mobile

# Install dependencies
npm install

# Start Expo development server
npx expo start --dev-client
```
**🎯 Expected:** 
- Expo server at `http://localhost:8081`
- QR code for mobile device scanning
- Option to run on Android/iOS emulator

### 🎪 All at Once (The Grand Opening)
For the ambitious conductor who wants the full orchestra:
```bash
# Terminal 1 - Backend
cd backend && venv\Scripts\activate && uvicorn main:app --reload --host 0.0.0.0 --port 8000

# Terminal 2 - Web Admin
cd web-admin && npm run dev

# Terminal 3 - Mobile App
cd mobile && npx expo start --dev-client
```

---

## 📁 Project Structure

```
PitchIn/
├── backend/                 # FastAPI backend
│   ├── app/
│   │   ├── routers/        # API endpoints (auth, founders, investors, etc.)
│   │   ├── models/         # Database models
│   │   ├── schemas/        # Pydantic schemas
│   │   └── services/       # Business logic
│   ├── supabase_schema.sql # Complete database schema
│   └── main.py            # Application entry point
├── mobile/                 # React Native + Expo app
│   ├── screens/           # All application screens
│   ├── components/        # Reusable UI components
│   └── App.js            # Main navigation stack
├── web-admin/             # Next.js admin dashboard
│   └── app/              # App router pages
└── resource/             # Media assets
    └── readme-intro.mp4  # Platform introduction video
```

---

## 🔐 Environment Configuration

Create `.env` files in each component with these essential variables:

### Backend (.env)
```env
SUPABASE_URL=your_supabase_project_url
SUPABASE_ANON_KEY=your_supabase_anon_key
SUPABASE_SERVICE_ROLE_KEY=your_supabase_service_role_key
DATABASE_URL=postgresql://...
STRIPE_SECRET_KEY=sk_test_...
RAZORPAY_KEY_ID=rzp_test_...
RAZORPAY_KEY_SECRET=your_razorpay_secret
```

### Mobile (.env)
```env
EXPO_PUBLIC_API_URL=http://localhost:8000
EXPO_PUBLIC_SUPABASE_URL=your_supabase_project_url
EXPO_PUBLIC_SUPABASE_ANON_KEY=your_supabase_anon_key
```

---

## 🧪 Testing the Waters

Once all three services are running:

1. **Visit the Admin Dashboard** (`http://localhost:3000`)
   - See the queue of sample founder applications
   - Practice approving and rejecting (it's just demo data)

2. **Explore the API Documentation** (`http://localhost:8000/docs`)
   - Try the `/health` endpoint
   - Examine all available endpoints

3. **Launch the Mobile App**
   - Scan the QR code with Expo Go on your phone
   - Walk through the onboarding flow
   - Experience the swipe-based discovery

---

## 🎯 What Makes Pitch In Special

### The Human Touch in Digital Spaces
We believe technology should **amplify human connection**, not replace it. Every feature in Pitch In is designed to:

1. **Reduce Anxiety** - Clear progress indicators, gentle nudges
2. **Increase Clarity** - Unambiguous next steps, transparent processes
3. **Foster Trust** - Verified profiles, secure communications
4. **Celebrate Progress** - Milestone acknowledgments, small wins highlighted

### The Algorithm with Empathy
Our matching algorithm considers not just:
- **Financial metrics** (stage, amount, sector)
- **Personal compatibility** (communication style, values alignment)
- **Timing synchronization** (readiness of both parties)
- **Psychological fit** (risk appetite, vision alignment)

---

## 🌈 The Road Ahead

Pitch In is a living platform, constantly evolving. Next horizons include:

- **AI-Powered Pitch Coaching** - Real-time feedback on presentation style
- **Virtual Reality Deal Rooms** - Immersive pitch experiences
- **Blockchain Verification** - Immutable records of commitments
- **Global Expansion** - Multi-currency, multi-language support
- **Community Features** - Founder forums, investor masterclasses

---

## 🙏 Acknowledgments

This platform stands on the shoulders of:
- **Every founder** who dared to dream bigger
- **Every investor** who looked beyond the spreadsheet
- **The open-source community** that makes such magic possible
- **The team** who believed connections could be both meaningful and measurable

---

## 📜 License

Pitch In is released under the **Connection Commons License** - because some things are too important to keep behind walls.

> *"The best way to predict the future is to create it."*<br>
> *— Alan Kay*

---

## 🚀 How to Run This Symphony

### The Short Version
```bash
# 1. Backend
cd backend && venv\Scripts\activate && uvicorn main:app --reload

# 2. Web Admin
cd web-admin && npm run dev

# 3. Mobile App
cd mobile && npx expo start --dev-client
```

### The Complete Guide
For detailed setup instructions, environment configuration, troubleshooting, and deployment guides, see the comprehensive **[QUICKSTART.md](QUICKSTART.md)** document.

### Access Points Once Running:
- **API & Documentation:** http://localhost:8000/docs
- **Admin Dashboard:** http://localhost:3000
- **Mobile App:** Scan QR code from Expo server (http://localhost:8081)
- **Health Check:** http://localhost:8000/health

### Need Help?
1. Check the [QUICKSTART.md](QUICKSTART.md) troubleshooting section
2. Verify all services are running on correct ports
3. Ensure environment variables are properly configured
4. Review terminal logs for any error messages

---

<div align="center">
  <br>
  <h3>Ready to change how the world connects?</h3>
  <p>Start the symphony. Make your first match. Build something beautiful.</p>
  <br>
  <img src="https://img.shields.io/badge/Status-Orchestra%20Tuned%20🎻-C9A84C" alt="Status">
  <img src="https://img.shields.io/badge/Connections-Waiting%20to%20Be%20Made-080C14" alt="Connections">
  <img src="https://img.shields.io/badge/Magic-Just%20Beginning-1A1F2C" alt="Magic">
  <br><br>
  <em>Pitch In — Where your next great partnership begins</em>
</div>
