# 🚀 GitHub Push Checklist for Pitch In

## ✅ Pre-Push Verification

### 1. **Sensitive Data Check**
- [ ] `.env` files contain only dummy/placeholder values
- [ ] No real API keys, secrets, or credentials are committed
- [ ] Database connection strings use placeholders
- [ ] JWT secrets are dummy values

### 2. **File Structure Cleanup**
- [ ] `node_modules/` directories are excluded (in .gitignore)
- [ ] `__pycache__/` and `.pyc` files are excluded
- [ ] `.expo/` and build directories are excluded
- [ ] `.next/` and `.venv/` directories are excluded
- [ ] Temporary files and logs are excluded

### 3. **Documentation Complete**
- [ ] `README.md` is comprehensive and poetic
- [ ] `QUICKSTART.md` has practical run instructions
- [ ] `LICENSE` file is present (MIT)
- [ ] `.gitignore` covers all necessary exclusions
- [ ] Video conversion scripts are included

## 📁 Project Structure for GitHub

```
PitchIn/
├── 📄 README.md                    # Main documentation (poetic)
├── 📄 QUICKSTART.md                # Practical run guide
├── 📄 PUSH_CHECKLIST.md           # This file
├── 📄 LICENSE                     # MIT License
├── 📄 .gitignore                  # Comprehensive ignore rules
├── 🔧 convert_video.bat           # Windows video converter
├── 🔧 convert_video.sh            # Unix video converter
├── 📁 backend/                    # FastAPI backend
│   ├── 📄 main.py                 # App entry point
│   ├── 📄 requirements.txt        # Python dependencies
│   ├── 📄 supabase_schema.sql     # Database schema
│   ├── 📄 .env.example           # Environment template
│   └── 📁 app/                   # Application code
├── 📁 mobile/                     # React Native + Expo app
│   ├── 📄 App.js                 # Main navigation
│   ├── 📄 package.json           # Dependencies
│   ├── 📄 app.json              # Expo config
│   └── 📁 screens/              # All app screens
├── 📁 web-admin/                  # Next.js admin dashboard
│   ├── 📄 package.json           # Dependencies
│   ├── 📄 next.config.ts         # Next.js config
│   └── 📁 app/                  # App router pages
└── 📁 resource/                  # Media assets
    └── 🎬 readme-intro.mp4      # Platform demo video
```

## 🔧 Git Commands to Push

### First Time Setup
```bash
# Initialize git repository
git init

# Add all files (excluding .gitignore patterns)
git add .

# Commit with descriptive message
git commit -m "feat: Initial commit - Pitch In investor-founder matching platform

- Complete 3-tier architecture (React Native + Next.js + FastAPI)
- Psychology-driven UI with glassmorphism design
- Founder signup (6-step) and investor signup (4-step) flows
- Swipe-based discovery with free-tier gating
- Pricing psychology with three subscription tiers
- Deal Room with real-time chat
- Admin dashboard for founder approval
- Payment integration architecture
- Comprehensive documentation and run guides"
```

### Connect to GitHub
```bash
# Create new repository on GitHub (no README, no .gitignore, no license)
# Then connect local repository

git remote add origin https://github.com/yourusername/pitch-in.git
git branch -M main
git push -u origin main
```

### Subsequent Updates
```bash
# Add changes
git add .

# Commit
git commit -m "feat: [Brief description of changes]"

# Push
git push
```

## 🚫 Files That Should NOT Be Pushed

The following files/directories are excluded by `.gitignore`:
- `node_modules/` (all three projects)
- `backend/__pycache__/`, `backend/.venv/`, `backend/venv/`
- `web-admin/.next/`, `web-admin/out/`
- `mobile/.expo/`, `mobile/android/`, `mobile/ios/`
- `.env` files (use `.env.example` instead)
- `*.log` files
- `resource/demo.gif` (can be regenerated)

## 🌐 GitHub Repository Settings

### Recommended Repository Settings:
1. **Description**: "Pitch In - Premium investor-founder matching platform with psychology-driven UI"
2. **Topics**: `investor-matching`, `founder-platform`, `react-native`, `nextjs`, `fastapi`, `startup`, `fundraising`
3. **Visibility**: Public (recommended for portfolio)
4. **README**: Displayed (our beautiful README.md)
5. **License**: MIT (already included)

### GitHub Actions (Optional):
Consider adding workflows for:
- Automated testing
- Code quality checks
- Dependency updates

## 📊 GitHub Stats Badges (Add to README)

After pushing, you can add these badges to your README:

```markdown
![GitHub last commit](https://img.shields.io/github/last-commit/yourusername/pitch-in)
![GitHub repo size](https://img.shields.io/github/repo-size/yourusername/pitch-in)
![GitHub language count](https://img.shields.io/github/languages/count/yourusername/pitch-in)
![GitHub top language](https://img.shields.io/github/languages/top/yourusername/pitch-in)
```

## 🎯 Final Verification

Run these commands to verify what will be pushed:

```bash
# Check git status
git status

# See what files are staged
git diff --cached --name-only

# Check file sizes
git ls-files | xargs ls -lh | sort -k5 -h -r | head -20
```

## 🆘 Troubleshooting

### "File too large" error
If `resource/readme-intro.mp4` is too large:
```bash
# Remove from git (if already added)
git rm --cached resource/readme-intro.mp4

# Add to .gitignore
echo "resource/readme-intro.mp4" >> .gitignore

# Commit .gitignore change
git add .gitignore
git commit -m "chore: Exclude large video file from repo"
```

### "Too many files" error
If you have many node_modules files:
```bash
# Ensure .gitignore is correct
# Remove all files and re-add
git rm -r --cached .
git add .
```

## 🎉 Ready to Push!

Your Pitch In project is now GitHub-ready with:
- ✅ Clean project structure
- ✅ Comprehensive documentation
- ✅ Proper license
- ✅ Sensitive data protection
- ✅ Exclusion of build artifacts
- ✅ Video assets properly handled

**Next Steps:**
1. Run `git status` to verify clean working directory
2. Commit with the provided commit message
3. Push to your GitHub repository
4. Share the repository link with your network!

---

<div align="center">
  <br>
  <h3>🌟 Your Pitch In platform is ready for the world!</h3>
  <p>Showcase this innovative investor-founder matching platform to potential employers, collaborators, or investors.</p>
  <br>
  <img src="https://img.shields.io/badge/Status-GitHub_Ready-brightgreen" alt="Status">
  <img src="https://img.shields.io/badge/License-MIT-blue" alt="License">
  <img src="https://img.shields.io/badge/Architecture-3_Tier_✨-C9A84C" alt="Architecture">
  <br><br>
</div>