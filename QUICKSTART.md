# ⚡ Pitch In - Quick Start Guide

## 🚀 One-Minute Setup

### Prerequisites Checklist
- [ ] **Node.js 18+** (Download from [nodejs.org](https://nodejs.org))
- [ ] **Python 3.11+** (Download from [python.org](https://python.org))
- [ ] **Git** (Already installed if you cloned this repo)
- [ ] **Expo Go** app on your phone (Optional, for mobile testing)

### 📦 Installation Steps

#### 1. Clone & Navigate
```bash
git clone <repository-url>
cd PitchIn
```

#### 2. Backend Setup (FastAPI)
```bash
# Navigate to backend
cd backend

# Create virtual environment
python -m venv venv

# Activate (Windows)
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Configure environment
copy .env.example .env
# Edit .env with your credentials (see below for test values)
```

#### 3. Web Admin Setup (Next.js)
```bash
# Navigate to web-admin
cd ../web-admin

# Install dependencies
npm install
```

#### 4. Mobile App Setup (React Native)
```bash
# Navigate to mobile
cd ../mobile

# Install dependencies
npm install
```

## 🎬 Running All Services

### Option A: Separate Terminals (Recommended)

**Terminal 1 - Backend API:**
```bash
cd backend
venv\Scripts\activate
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

**Terminal 2 - Web Admin:**
```bash
cd web-admin
npm run dev
```

**Terminal 3 - Mobile App:**
```bash
cd mobile
npx expo start --dev-client
```

### Option B: Using PM2 (Advanced)
```bash
# Install PM2 globally
npm install -g pm2

# Start all services
pm2 start ecosystem.config.js
```

## 🔧 Environment Configuration

### Backend (.env) - Test Values
```env
# For local development only
SUPABASE_URL=http://localhost:54321
SUPABASE_ANON_KEY=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...
SUPABASE_SERVICE_ROLE_KEY=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...
DATABASE_URL=postgresql://postgres:postgres@localhost:54322/postgres
STRIPE_SECRET_KEY=sk_test_51...
RAZORPAY_KEY_ID=rzp_test_...
RAZORPAY_KEY_SECRET=test_secret_...
JWT_SECRET=your-super-secret-jwt-key-change-this
```

### Mobile (.env) - Create in mobile directory
```env
EXPO_PUBLIC_API_URL=http://localhost:8000
EXPO_PUBLIC_SUPABASE_URL=http://localhost:54321
EXPO_PUBLIC_SUPABASE_ANON_KEY=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...
```

## 🌐 Access Points

Once running, access the platform at:

| Service | URL | Purpose |
|---------|-----|---------|
| **Backend API** | http://localhost:8000 | REST API endpoints |
| **API Docs** | http://localhost:8000/docs | Interactive Swagger UI |
| **Health Check** | http://localhost:8000/health | Service status |
| **Web Admin** | http://localhost:3000 | Admin dashboard |
| **Expo Server** | http://localhost:8081 | Mobile app bundle |
| **Expo Dev Tools** | http://localhost:19002 | Expo development UI |

## 📱 Testing the Mobile App

### Method 1: Physical Device (Easiest)
1. Install **Expo Go** from App Store (iOS) or Play Store (Android)
2. Scan the QR code shown in Terminal 3
3. App loads automatically on your phone

### Method 2: Android Emulator
```bash
# Start Android emulator first (from Android Studio)
cd mobile
npx expo start --android
```

### Method 3: iOS Simulator (macOS only)
```bash
# Ensure Xcode is installed
cd mobile
npx expo start --ios
```

## 🧪 Quick Verification

Run this command to verify all services:
```bash
# Check backend
curl http://localhost:8000/health

# Check web-admin
curl -I http://localhost:3000

# Check Expo
curl http://localhost:8081 | grep -o '"name":"mobile"'
```

Expected output:
- Backend: `{"status":"healthy"}`
- Web-admin: `HTTP/1.1 200 OK`
- Expo: Should find the mobile app name

## 🐛 Common Issues & Solutions

### 1. "Port already in use"
```bash
# Find process using port
netstat -ano | findstr :8000
# Kill process (replace PID)
taskkill /PID <PID> /F
```

### 2. "Module not found" in backend
```bash
cd backend
venv\Scripts\activate
pip install -r requirements.txt --upgrade
```

### 3. "Expo not working"
```bash
cd mobile
rm -rf node_modules
npm install
npx expo start --clear
```

### 4. "Supabase connection failed"
- Use the mock client (already configured in database.py)
- Or set up local Supabase: `docker-compose up supabase`

## 📊 Service Ports Reference

| Port | Service | Can be changed? |
|------|---------|-----------------|
| 8000 | FastAPI Backend | Yes (edit main.py) |
| 3000 | Next.js Web Admin | Yes (edit package.json) |
| 8081 | Expo Dev Server | Yes (EXPO_DEV_SERVER_PORT) |
| 19002 | Expo Dev Tools | Yes (EXPO_DEV_TOOLS_PORT) |
| 54321 | Supabase Local | If running locally |

## 🚀 Production Deployment

### Backend (FastAPI)
```bash
# Production server
uvicorn main:app --host 0.0.0.0 --port 8000 --workers 4

# With Gunicorn (Linux)
gunicorn main:app -w 4 -k uvicorn.workers.UvicornWorker -b 0.0.0.0:8000
```

### Web Admin (Next.js)
```bash
# Build for production
npm run build

# Start production server
npm start
```

### Mobile App (React Native)
```bash
# Build for iOS
eas build --platform ios

# Build for Android
eas build --platform android

# Or create standalone builds
expo build:ios
expo build:android
```

## 🔗 Useful Commands

### Database Management
```bash
# Apply schema to Supabase
psql -h localhost -U postgres -d postgres -f backend/supabase_schema.sql

# Reset database (careful!)
cd backend
python reset_db.py
```

### Dependency Updates
```bash
# Backend
cd backend
pip freeze > requirements.txt

# Frontend
cd web-admin
npm update

# Mobile
cd mobile
npm update
```

### Logs Monitoring
```bash
# Backend logs
cd backend && tail -f uvicorn.log

# Web-admin logs
cd web-admin && npm run dev 2>&1 | tee dev.log

# Expo logs
cd mobile && npx expo start 2>&1 | tee expo.log
```

## 🆘 Need Help?

1. **Check the README.md** for detailed platform overview
2. **View API documentation** at http://localhost:8000/docs
3. **Examine error logs** in respective terminal windows
4. **Verify all services are running** using the verification commands above

---

<div align="center">
  <br>
  <h3>🎯 All Set! Your Pitch In platform is ready.</h3>
  <p>Start exploring at <a href="http://localhost:3000">http://localhost:3000</a> (admin)</p>
  <p>Or scan the QR code to launch the mobile app!</p>
  <br>
  <img src="https://img.shields.io/badge/Status-All%20Systems%20Go-brightgreen" alt="Status">
  <img src="https://img.shields.io/badge/Ports-8000%2C%203000%2C%208081-blue" alt="Ports">
  <br><br>
</div>