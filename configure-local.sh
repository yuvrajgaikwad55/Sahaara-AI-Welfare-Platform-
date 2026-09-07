#!/bin/bash

echo ""
echo "╔════════════════════════════════════════════════════════════╗"
echo "║         SAATHI - Local Environment Setup                    ║"
echo "║      Complete Development Environment Configuration         ║"
echo "╚════════════════════════════════════════════════════════════╝"
echo ""

BLUE='\033[0;34m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m'

echo -e "${BLUE}Step 1: Creating .env file...${NC}"

if [ ! -f ".env" ]; then
    cat > .env << 'EOF'
# SAATHI - Development Environment Variables

# Flask Configuration
FLASK_ENV=development
FLASK_DEBUG=True
SECRET_KEY=saathi-development-secret-key-change-in-production

# Database
DATABASE_URL=sqlite:///saathi_dev.db
DATABASE_ECHO=True

# JWT
JWT_SECRET=saathi-jwt-secret-key-change-in-production
JWT_EXPIRATION=86400

# API Configuration
API_HOST=0.0.0.0
API_PORT=5000
API_DEBUG=True

# CORS
CORS_ORIGINS=http://localhost:8000,http://localhost:3000

# Redis (Optional - for caching)
REDIS_URL=redis://localhost:6379/0

# Email (Optional - for notifications)
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
SMTP_USERNAME=your-email@gmail.com
SMTP_PASSWORD=your-app-password
SMTP_FROM_EMAIL=saathi@welfare.local

# AI/ML
ML_MODEL_PATH=./models
ML_DEBUG=True
ML_EXPLAIN_PREDICTIONS=True

# Logging
LOG_LEVEL=DEBUG
LOG_FILE=./logs/saathi.log

# Security (Development)
ALLOWED_HOSTS=localhost,127.0.0.1
SESSION_TIMEOUT=3600
MAX_LOGIN_ATTEMPTS=10
LOCKOUT_DURATION=300

# Features
ENABLE_DEMO_DATA=True
ENABLE_MOCK_PREDICTIONS=True
ENABLE_AUDIT_LOGGING=True
ENABLE_SYNTHETIC_DATA=True

# Notes
# Change all secrets before production deployment
# Update database URL for PostgreSQL in production
# Configure proper email credentials for notifications
EOF
    echo -e "${GREEN}✓ .env file created${NC}"
else
    echo -e "${YELLOW}ℹ .env file already exists${NC}"
fi

echo ""
echo -e "${BLUE}Step 2: Creating directory structure...${NC}"

mkdir -p logs
mkdir -p models
mkdir -p data
mkdir -p uploads
mkdir -p backups

echo -e "${GREEN}✓ Directories created${NC}"

echo ""
echo -e "${BLUE}Step 3: Making scripts executable...${NC}"

chmod +x setup.sh
chmod +x dev.sh
chmod +x test-api.sh
chmod +x configure-local.sh

echo -e "${GREEN}✓ Scripts are executable${NC}"

echo ""
echo "╔════════════════════════════════════════════════════════════╗"
echo -e "${GREEN}║         Local Setup Complete! ���                          ║${NC}"
echo "╚════════════════════════════════════════════════════════════╝"
echo ""
echo "📋 Quick Start:"
echo ""
echo "1. Setup Python environment (first time only):"
echo -e "   ${BLUE}./setup.sh${NC}"
echo ""
echo "2. Start development servers:"
echo -e "   ${BLUE}./dev.sh${NC}"
echo ""
echo "3. Test API endpoints:"
echo -e "   ${BLUE}./test-api.sh${NC}"
echo ""
echo "🌐 Local URLs:"
echo -e "   ${BLUE}Website: http://localhost:8000${NC}"
echo -e "   ${BLUE}API: http://localhost:5000${NC}"
echo -e "   ${BLUE}Health: http://localhost:5000/health${NC}"
echo ""
echo "📝 Demo Credentials:"
echo -e "   ${YELLOW}Personnel: personnel@saathi.local / demo123${NC}"
echo -e "   ${YELLOW}Officer: officer@saathi.local / demo123${NC}"
echo -e "   ${YELLOW}Commander: commander@saathi.local / demo123${NC}"
echo ""
echo "📄 Environment Variables (.env):"
echo -e "   ${YELLOW}Created: .env${NC}"
echo -e "   ${YELLOW}Database: sqlite:///saathi_dev.db${NC}"
echo -e "   ${YELLOW}Debug Mode: Enabled${NC}"
echo ""
echo "🔒 Important:"
echo -e "   ${RED}⚠ Change all secrets before production!${NC}"
echo -e "   ${RED}⚠ Use PostgreSQL in production, not SQLite!${NC}"
echo -e "   ${RED}⚠ Configure proper email for notifications!${NC}"
echo ""
