# Quick Start Guide - Sahaara AI Welfare Platform

## 🚀 Get Started in 5 Minutes

### Option 1: Using Shell Scripts (Easiest)

```bash
# 1. Setup
chmod +x start.sh
./start.sh

# 2. Run (in a new terminal)
chmod +x run.sh
./run.sh

# 3. Open browser
# Website: http://localhost:8000
# API: http://localhost:5000/health
```

### Option 2: Using Docker Compose (Recommended)

```bash
# 1. Start all services
docker-compose up

# 2. Access
# Website: http://localhost:8000
# API: http://localhost:5000
```

### Option 3: Manual Setup

```bash
# Terminal 1: Backend
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python app.py
# Runs on http://localhost:5000

# Terminal 2: Frontend
cd website
python -m http.server 8000
# Runs on http://localhost:8000
```

---

## 📚 What's Included

### Website (Frontend)
- ✅ Professional responsive design
- ✅ Mobile-optimized interface
- ✅ Contact form
- ✅ Feature showcase
- ✅ Smooth animations

### Backend API
- ✅ Authentication endpoints
- ✅ Wellness data submission
- ✅ Stress prediction
- ✅ Alert management
- ✅ Resource access
- ✅ Dashboard data

---

## 🔑 API Examples

### Login
```bash
curl -X POST http://localhost:5000/api/auth/login \
  -H "Content-Type: application/json" \
  -d '{"email":"user@example.com","password":"pass123"}'
```

### Submit Wellness Data
```bash
curl -X POST http://localhost:5000/api/wellness/submit \
  -H "Content-Type: application/json" \
  -d '{"personnel_id":"P001","stress_level":5,"sleep_quality":7,"mood":"good"}'
```

### Get Stress Prediction
```bash
curl -X GET http://localhost:5000/api/stress/predict/P001
```

### Get Dashboard Overview
```bash
curl -X GET http://localhost:5000/api/dashboard/overview
```

---

## 🌐 Access Points

| Component | URL | Purpose |
|-----------|-----|----------|
| Website | http://localhost:8000 | User interface |
| API | http://localhost:5000 | Backend API |
| Health Check | http://localhost:5000/health | API status |
| Docs | http://localhost:5000/api/docs | API documentation |

---

## 📋 Available Endpoints

### Authentication
- `POST /api/auth/login` - User login
- `GET /api/auth/profile` - Get user profile

### Wellness
- `POST /api/wellness/submit` - Submit wellness data
- `GET /api/wellness/history/<id>` - Get wellness history
- `GET /api/wellness/latest/<id>` - Get latest wellness data

### Stress Prediction
- `GET /api/stress/predict/<id>` - Predict stress level
- `GET /api/stress/risk-level/<id>` - Get risk level

### Alerts
- `GET /api/alerts` - Get all alerts
- `POST /api/alerts/create` - Create new alert

### Resources
- `GET /api/resources` - Get resources
- `GET /api/resources/counselors` - Get counselor list

### Dashboard
- `GET /api/dashboard/overview` - Dashboard overview
- `GET /api/dashboard/alerts` - Dashboard alerts

### Interventions
- `POST /api/interventions` - Create intervention

---

## 🧪 Test the System

### 1. Check API Health
```bash
curl http://localhost:5000/health
```

### 2. Login
```bash
curl -X POST http://localhost:5000/api/auth/login \
  -H "Content-Type: application/json" \
  -d '{"email":"test@example.com","password":"test123"}'
```

### 3. Submit Wellness Data
```bash
curl -X POST http://localhost:5000/api/wellness/submit \
  -H "Content-Type: application/json" \
  -d '{
    "personnel_id":"P001",
    "stress_level":6,
    "sleep_quality":7,
    "mood":"good",
    "physical_activity":45,
    "notes":"Feeling better"
  }'
```

### 4. Get Stress Prediction
```bash
curl http://localhost:5000/api/stress/predict/P001
```

### 5. Get Dashboard Data
```bash
curl http://localhost:5000/api/dashboard/overview
```

---

## 🐛 Troubleshooting

### Port Already in Use
```bash
# Find process using port 5000
lsof -i :5000
# Kill process
kill -9 <PID>
```

### Virtual Environment Issues
```bash
# Remove and recreate
rm -rf venv
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Docker Issues
```bash
# Clean up
docker-compose down -v
# Restart
docker-compose up --build
```

---

## 📊 Project Structure

```
Sahaara-AI-Welfare-Platform/
├── website/                    # Frontend
│   ├── index.html
│   ├── styles.css
│   ├── script.js
│   └── README.md
├── backend/                    # Backend API
│   ├── app.py                 # Main Flask application
│   ├── requirements.txt
│   ├── Dockerfile
│   └── README.md
├── docker-compose.yml          # Docker configuration
├── start.sh                    # Setup script
├── run.sh                      # Run script
├── QUICKSTART.md              # This file
├── DEPLOYMENT_GUIDE.md
├── ARCHITECTURE.md
└── SIH_CHALLENGE_SIH26186.md
```

---

## ✅ Checklist

- [ ] Backend running on port 5000
- [ ] Frontend running on port 8000
- [ ] Can access http://localhost:8000
- [ ] Can access http://localhost:5000/health
- [ ] Can login via API
- [ ] Can submit wellness data
- [ ] Can see stress prediction
- [ ] Website shows all sections

---

## 🎯 Next Steps

1. Explore the website at http://localhost:8000
2. Test API endpoints using curl or Postman
3. Submit wellness data
4. Check stress predictions
5. Review documentation files
6. Deploy to cloud (see DEPLOYMENT_GUIDE.md)

---

## 📞 Support

For issues or questions:
- Check troubleshooting section above
- Review ARCHITECTURE.md for system design
- Check DEPLOYMENT_GUIDE.md for deployment help
- Review backend/README.md for API details

---

**Version**: 1.0  
**Last Updated**: September 2026  
**Status**: ✅ Ready to Use
