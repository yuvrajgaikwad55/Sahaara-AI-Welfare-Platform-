# SAATHI - Local Development Guide

## Quick Start (3 Steps)

### Step 1: Configure Local Environment
```bash
chmod +x configure-local.sh
./configure-local.sh
```
This creates:
- `.env` file with configuration
- Required directories (logs, models, data)
- Executable permissions for scripts

### Step 2: Setup Python Environment
```bash
chmod +x setup.sh
./setup.sh
```
This:
- Checks Python 3 installation
- Creates virtual environment
- Installs backend dependencies

### Step 3: Start Development Servers
```bash
chmod +x dev.sh
./dev.sh
```
This starts:
- Backend API on http://localhost:5000
- Frontend Server on http://localhost:8000

---

## Access SAATHI

### URLs
- **Website**: http://localhost:8000
- **API**: http://localhost:5000
- **Health Check**: http://localhost:5000/health

### Demo Login Credentials

**Personnel Account**
```
Email: personnel@saathi.local
Password: demo123
Role: Personnel
```

**Welfare Officer Account**
```
Email: officer@saathi.local
Password: demo123
Role: Welfare Officer
```

**Commander Account**
```
Email: commander@saathi.local
Password: demo123
Role: Commander/Admin
```

---

## Available Scripts

### configure-local.sh
Sets up local development environment
```bash
./configure-local.sh
```

### setup.sh
Creates Python virtual environment and installs dependencies
```bash
./setup.sh
```

### dev.sh
Starts all development servers
```bash
./dev.sh
```

### test-api.sh
Tests API endpoints
```bash
chmod +x test-api.sh
./test-api.sh
```

---

## Environment Variables (.env)

The `.env` file contains:

```env
# Flask
FLASK_ENV=development
FLASK_DEBUG=True
SECRET_KEY=...

# Database
DATABASE_URL=sqlite:///saathi_dev.db

# API
API_PORT=5000

# JWT
JWT_SECRET=...

# Debug
LOG_LEVEL=DEBUG

# Features
ENABLE_DEMO_DATA=True
ENABLE_MOCK_PREDICTIONS=True
```

---

## Project Structure

```
SAATHI/
├── setup.sh                 # Setup script
├── dev.sh                   # Run development servers
├── test-api.sh              # Test API endpoints
├── configure-local.sh       # Configure local environment
├── .env                     # Environment variables (created)
├── .env.example             # Example env file
├── backend/
│   ├── app.py              # Flask application
│   ├── requirements.txt     # Python dependencies
│   └── README.md            # Backend docs
├── website/
│   ├── index.html          # Frontend
│   ├── styles.css
│   ├── script.js
│   └── README.md
├── logs/                    # Application logs (created)
├── models/                  # ML models (created)
├── data/                    # Data storage (created)
└── README.md                # Project README
```

---

## Troubleshooting

### Python not found
```bash
# Install Python 3
sudo apt-get install python3 python3-venv  # Ubuntu/Debian
brew install python3                        # macOS
choco install python                        # Windows
```

### Port 5000 already in use
```bash
# Find process using port
lsof -i :5000

# Kill process
kill -9 <PID>
```

### Port 8000 already in use
```bash
# Use different port
cd website
python -m http.server 9000
```

### Virtual environment activation fails
```bash
# Delete and recreate
rm -rf venv
python3 -m venv venv
source venv/bin/activate
pip install -r backend/requirements.txt
```

### API connection refused
```bash
# Check if backend is running
curl http://localhost:5000/health

# If not, start it manually
cd backend
source ../venv/bin/activate
python app.py
```

---

## Testing APIs

### Test All Endpoints
```bash
./test-api.sh
```

### Health Check
```bash
curl http://localhost:5000/health
```

### Login
```bash
curl -X POST http://localhost:5000/api/v1/auth/login \
  -H "Content-Type: application/json" \
  -d '{
    "email": "personnel@saathi.local",
    "password": "demo123"
  }'
```

### Submit Wellness
```bash
curl -X POST http://localhost:5000/api/v1/wellness/checkin \
  -H "Authorization: Bearer <token>" \
  -H "Content-Type: application/json" \
  -d '{
    "energy": 7,
    "workload": 6,
    "recovery": 5,
    "duty_demand": 8,
    "support_need": "no"
  }'
```

---

## Database

### SQLite (Development)
```
Location: saathi_dev.db
Viewer: sqlite3 saathi_dev.db
```

### Backup Database
```bash
cp saathi_dev.db backups/saathi_dev_$(date +%Y%m%d_%H%M%S).db
```

### Reset Database
```bash
rm saathi_dev.db
```

---

## Logging

### View Logs
```bash
cat logs/saathi.log
```

### Real-time Logs
```bash
tail -f logs/saathi.log
```

### Clear Logs
```bash
rm logs/saathi.log
```

---

## Development Workflow

1. **Configure**: `./configure-local.sh` (first time)
2. **Setup**: `./setup.sh` (first time)
3. **Develop**: Edit code in backend/ or website/
4. **Run**: `./dev.sh`
5. **Test**: Access http://localhost:8000
6. **Test API**: `./test-api.sh`
7. **Debug**: Check logs/ directory
8. **Repeat**: Make changes, restart servers

---

## Performance Tips

1. Use Firefox/Chrome DevTools for debugging
2. Enable debug logging in .env
3. Check network tab for API calls
4. Monitor logs in real-time: `tail -f logs/saathi.log`
5. Use API testing tool like Postman

---

## Security (Development Only)

⚠️ **WARNING**: These configurations are for LOCAL DEVELOPMENT ONLY

Before production:
- [ ] Change all secrets in .env
- [ ] Use PostgreSQL instead of SQLite
- [ ] Enable HTTPS/TLS
- [ ] Configure proper authentication
- [ ] Set up security headers
- [ ] Enable rate limiting
- [ ] Configure CORS properly
- [ ] Setup firewall rules
- [ ] Enable audit logging
- [ ] Configure backups

---

## Next Steps

1. Explore the platform at http://localhost:8000
2. Login with demo credentials
3. Submit wellness check-in
4. View AI predictions
5. Check different user roles
6. Test API endpoints
7. Review documentation files
8. Make code changes and refresh

---

**Version**: 1.0  
**Status**: Ready for Local Development  
**Last Updated**: September 2026
