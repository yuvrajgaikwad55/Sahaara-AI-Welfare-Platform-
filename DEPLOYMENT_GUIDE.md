# Sahaara Platform - Deployment Guide

## Quick Start

### Prerequisites
- Node.js 16+ or Python 3.9+
- Docker & Docker Compose
- Git
- PostgreSQL 13+
- Redis 6+

---

## Development Environment Setup

### 1. Clone Repository
```bash
git clone https://github.com/yuvrajgaikwad55/Sahaara-AI-Welfare-Platform-.git
cd Sahaara-AI-Welfare-Platform-
```

### 2. Set Up Frontend (Website)
```bash
cd website
python -m http.server 8000
# OR using Node.js
npx http-server
```
Access: http://localhost:8000

### 3. Set Up Backend
```bash
cd backend
pip install -r requirements.txt
python app.py
```
Access: http://localhost:5000

### 4. Set Up Mobile App
```bash
cd mobile
npm install
npm start  # for React Native
```

---

## Docker Deployment

### 1. Build Docker Images
```bash
# Frontend
docker build -t sahaara-frontend ./website

# Backend
docker build -t sahaara-backend ./backend

# ML Engine
docker build -t sahaara-ml ./ml_engine
```

### 2. Run with Docker Compose
```bash
docker-compose up -d
```

### 3. Verify Services
```bash
docker-compose ps
```

---

## Cloud Deployment

### AWS Deployment

#### 1. Set Up EC2 Instance
```bash
# Launch Ubuntu 20.04 LTS instance
# Security Group: Allow ports 80, 443, 3000, 5000, 8000

# SSH into instance
ssh -i your-key.pem ubuntu@your-ec2-ip

# Update system
sudo apt update && sudo apt upgrade -y

# Install dependencies
sudo apt install -y python3-pip nodejs npm postgresql redis-server nginx
```

#### 2. Clone and Deploy
```bash
git clone https://github.com/yuvrajgaikwad55/Sahaara-AI-Welfare-Platform-.git
cd Sahaara-AI-Welfare-Platform-

# Install Python dependencies
cd backend
pip install -r requirements.txt

# Install Node dependencies
cd ../website
npm install
```

#### 3. Configure Nginx
```nginx
server {
    listen 80;
    server_name your-domain.com;

    # Frontend
    location / {
        proxy_pass http://localhost:3000;
    }

    # API
    location /api {
        proxy_pass http://localhost:5000;
    }
}
```

#### 4. Start Services
```bash
# Terminal 1: Backend
cd backend
gunicorn -w 4 -b 0.0.0.0:5000 app.py

# Terminal 2: Frontend
cd website
npm start

# Terminal 3: ML Engine
cd ml_engine
python main.py
```

### Azure Deployment

#### 1. Create Resource Group
```bash
az group create --name SaharaRG --location eastus
```

#### 2. Create App Service
```bash
az appservice plan create --name SaharaPlan --resource-group SaharaRG --sku B1 --is-linux

az webapp create --resource-group SaharaRG --plan SaharaPlan --name sahaara-platform
```

#### 3. Deploy Code
```bash
az webapp up --resource-group SaharaRG --name sahaara-platform --location eastus
```

### Google Cloud Deployment

#### 1. Create GCP Project
```bash
gcloud projects create sahaara-platform
gcloud config set project sahaara-platform
```

#### 2. Deploy to Cloud Run
```bash
# Build and push to Container Registry
gcloud builds submit --tag gcr.io/sahaara-platform/backend
gcloud builds submit --tag gcr.io/sahaara-platform/frontend

# Deploy
gcloud run deploy sahaara-backend --image gcr.io/sahaara-platform/backend
gcloud run deploy sahaara-frontend --image gcr.io/sahaara-platform/frontend
```

---

## Database Setup

### PostgreSQL Configuration
```bash
# Connect to PostgreSQL
sudo -u postgres psql

# Create database
CREATE DATABASE sahaara_db;

# Create user
CREATE USER sahaara_user WITH PASSWORD 'secure_password';

# Grant privileges
ALTER ROLE sahaara_user SET client_encoding TO 'utf8';
ALTER ROLE sahaara_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE sahaara_user SET default_transaction_deferrable TO on;
GRANT ALL PRIVILEGES ON DATABASE sahaara_db TO sahaara_user;
```

### Run Migrations
```bash
cd backend
python manage.py migrate
python manage.py createsuperuser
```

---

## Security Configuration

### 1. SSL/TLS Setup
```bash
# Generate self-signed certificate
openssl req -x509 -newkey rsa:4096 -nodes -out cert.pem -keyout key.pem -days 365

# Or use Let's Encrypt (Recommended)
certbot certonly --standalone -d your-domain.com
```

### 2. Environment Variables
Create `.env` file:
```env
# Database
DATABASE_URL=postgresql://user:password@localhost/sahaara_db

# Security
SECRET_KEY=your-secret-key-here
ALLOWED_HOSTS=localhost,127.0.0.1,your-domain.com

# Email (for alerts)
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USER=your-email@gmail.com
EMAIL_PASSWORD=your-app-password

# ML Models
ML_MODEL_PATH=/path/to/models

# Redis
REDIS_URL=redis://localhost:6379/0

# AWS (if using)
AWS_ACCESS_KEY_ID=your-key
AWS_SECRET_ACCESS_KEY=your-secret
AWS_STORAGE_BUCKET_NAME=sahaara-data
```

### 3. HTTPS Configuration
```nginx
server {
    listen 443 ssl http2;
    server_name your-domain.com;

    ssl_certificate /etc/letsencrypt/live/your-domain.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/your-domain.com/privkey.pem;
    
    # Security headers
    add_header Strict-Transport-Security "max-age=31536000" always;
    add_header X-Frame-Options "SAMEORIGIN" always;
    add_header X-Content-Type-Options "nosniff" always;
}
```

---

## Monitoring & Logging

### 1. Set Up Logging
```bash
# Using ELK Stack (Elasticsearch, Logstash, Kibana)
docker run -d --name elasticsearch -e "discovery.type=single-node" docker.elastic.co/elasticsearch/elasticsearch:7.15.0
docker run -d --name kibana docker.elastic.co/kibana/kibana:7.15.0
```

### 2. Application Monitoring
```python
# Add to backend/app.py
from prometheus_client import Counter, Histogram
import time

request_count = Counter('request_count', 'Total requests')
request_duration = Histogram('request_duration_seconds', 'Request duration')

@app.before_request
def start_timer():
    g.start = time.time()

@app.after_request
def end_timer(response):
    duration = time.time() - g.start
    request_count.inc()
    request_duration.observe(duration)
    return response
```

### 3. Health Check Endpoint
```python
@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now(),
        'version': '1.0.0'
    }), 200
```

---

## Performance Optimization

### 1. Caching
```python
from flask_caching import Cache

cache = Cache(app, config={'CACHE_TYPE': 'redis'})

@app.route('/dashboard')
@cache.cached(timeout=300)
def dashboard():
    # Expensive operation
    pass
```

### 2. Database Indexing
```sql
-- Create indexes for frequently queried columns
CREATE INDEX idx_personnel_id ON personnel(id);
CREATE INDEX idx_stress_level ON wellness_data(stress_level);
CREATE INDEX idx_timestamp ON wellness_data(timestamp);
```

### 3. API Rate Limiting
```python
from flask_limiter import Limiter

limiter = Limiter(app, key_func=lambda: request.remote_addr)

@app.route('/api/wellness')
@limiter.limit("100/hour")
def get_wellness():
    pass
```

---

## Backup & Recovery

### 1. Database Backup
```bash
# Daily backup
sudo pg_dump sahaara_db > /backups/sahaara_db_$(date +%Y%m%d).sql

# Restore backup
sudo psql sahaara_db < /backups/sahaara_db_20260907.sql
```

### 2. AWS S3 Backup
```bash
# Upload to S3
aws s3 cp /backups/sahaara_db_*.sql s3://sahaara-backups/

# Set lifecycle policy for old backups
aws s3api put-bucket-lifecycle-configuration --bucket sahaara-backups \
  --lifecycle-configuration file://lifecycle.json
```

---

## Testing

### Unit Tests
```bash
cd backend
pytest tests/ -v
```

### Integration Tests
```bash
pytest tests/integration/ -v --cov=app
```

### Load Testing
```bash
# Using Apache Bench
ab -n 1000 -c 100 http://localhost:5000/api/wellness

# Using Locust
locust -f locustfile.py --host=http://localhost:5000
```

---

## Troubleshooting

### Common Issues

#### Issue: Port already in use
```bash
# Find process using port
lsof -i :5000

# Kill process
kill -9 <PID>
```

#### Issue: Database connection error
```bash
# Check PostgreSQL status
sudo systemctl status postgresql

# Restart PostgreSQL
sudo systemctl restart postgresql
```

#### Issue: ML model loading fails
```bash
# Verify model path
ls -la /path/to/models/

# Check model file integrity
md5sum model.pkl
```

---

## Production Checklist

- [ ] SSL/TLS certificates installed
- [ ] Database backups configured
- [ ] Monitoring and logging set up
- [ ] Security audit completed
- [ ] Rate limiting enabled
- [ ] Error handling configured
- [ ] Health checks deployed
- [ ] Performance optimized
- [ ] Documentation updated
- [ ] Team trained on platform

---

## Support & Documentation

📚 **Full Documentation**: See `/docs` directory  
🐛 **Issue Tracking**: GitHub Issues  
💬 **Discussions**: GitHub Discussions  
📧 **Support Email**: support@sahaara-ai.com  

---

**Version**: 1.0  
**Last Updated**: September 2026
