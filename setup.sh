#!/bin/bash

echo ""
echo "╔════════════════════════════════════════════════════════════╗"
echo "║         SAATHI - Local Development Setup                    ║"
echo "║     AI Welfare Intelligence Platform - Smart India          ║"
echo "╚════════════════════════════════════════════════════════════╝"
echo ""

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Check Python
echo -e "${BLUE}[1/5]${NC} Checking Python installation..."
if ! command -v python3 &> /dev/null; then
    echo -e "${RED}✗ Python 3 is not installed${NC}"
    exit 1
fi
echo -e "${GREEN}✓ Python found: $(python3 --version)${NC}"

# Check Node.js
echo -e "${BLUE}[2/5]${NC} Checking Node.js installation..."
if ! command -v node &> /dev/null; then
    echo -e "${YELLOW}⚠ Node.js not found (optional for frontend)${NC}"
else
    echo -e "${GREEN}✓ Node.js found: $(node --version)${NC}"
fi

# Create virtual environment
echo -e "${BLUE}[3/5]${NC} Creating Python virtual environment..."
if [ ! -d "venv" ]; then
    python3 -m venv venv
    echo -e "${GREEN}✓ Virtual environment created${NC}"
else
    echo -e "${YELLOW}ℹ Virtual environment already exists${NC}"
fi

# Activate virtual environment
echo -e "${BLUE}[4/5]${NC} Activating virtual environment..."
source venv/bin/activate
echo -e "${GREEN}✓ Virtual environment activated${NC}"

# Install dependencies
echo -e "${BLUE}[5/5]${NC} Installing dependencies..."
pip install --upgrade pip > /dev/null 2>&1

if [ -f "backend/requirements.txt" ]; then
    pip install -r backend/requirements.txt > /dev/null 2>&1
    echo -e "${GREEN}✓ Backend dependencies installed${NC}"
else
    echo -e "${YELLOW}⚠ backend/requirements.txt not found${NC}"
fi

echo ""
echo "╔════════════════════════════════════════════════════════════╗"
echo -e "${GREEN}║           Setup Complete! ✓                               ║${NC}"
echo "╚════════════════════════════════════════════════════════════╝"
echo ""
echo "📋 Next Steps:"
echo ""
echo "1. Start Backend Server (Terminal 1):"
echo -e "   ${BLUE}cd backend && python app.py${NC}"
echo ""
echo "2. Start Frontend Server (Terminal 2):"
echo -e "   ${BLUE}cd website && python -m http.server 8000${NC}"
echo ""
echo "3. Access SAATHI:"
echo -e "   ${BLUE}🌐 Website: http://localhost:8000${NC}"
echo -e "   ${BLUE}🔌 API: http://localhost:5000${NC}"
echo -e "   ${BLUE}✅ Health: http://localhost:5000/health${NC}"
echo ""
echo "📚 Demo Credentials:"
echo -e "   ${YELLOW}Personnel: personnel@saathi.local / demo123${NC}"
echo -e "   ${YELLOW}Officer: officer@saathi.local / demo123${NC}"
echo -e "   ${YELLOW}Commander: commander@saathi.local / demo123${NC}"
echo ""
echo "📖 Documentation:"
echo -e "   ${BLUE}Quick Start: cat GETTING_STARTED.md${NC}"
echo -e "   ${BLUE}API Docs: cat API_DOCS.md${NC}"
echo -e "   ${BLUE}Architecture: cat ARCHITECTURE.md${NC}"
echo ""
