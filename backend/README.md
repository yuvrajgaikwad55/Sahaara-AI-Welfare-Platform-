# Sahaara AI Welfare Platform - Backend API

Quick start backend server for local development.

## Setup

### 1. Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Environment Variables
Create `.env` file:
```env
FLASK_ENV=development
DATABASE_URL=sqlite:///sahaara.db
SECRET_KEY=your-secret-key-here
JWT_SECRET=your-jwt-secret
```

### 4. Run Server
```bash
python app.py
```

Server runs on `http://localhost:5000`

## API Endpoints

### Health Check
```bash
GET /health
```

### Wellness Data
```bash
POST /api/wellness/submit
GET /api/wellness/history/:personnel_id
```

### Authentication
```bash
POST /api/auth/login
POST /api/auth/logout
GET /api/auth/profile
```

### Stress Prediction
```bash
GET /api/stress/predict/:personnel_id
GET /api/stress/risk-level/:personnel_id
```

### Resources
```bash
GET /api/resources
GET /api/resources/counselors
```

### Dashboard
```bash
GET /api/dashboard/overview
GET /api/dashboard/alerts
```
