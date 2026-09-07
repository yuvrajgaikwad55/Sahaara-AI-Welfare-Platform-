#!/bin/bash

echo ""
echo "╔════════════════════════════════════════════════════════════╗"
echo "║           SAATHI - Local Development Server                 ║"
echo "║         Starting All Services...                            ║"
echo "╚════════════════════════════════════════════════════════════╝"
echo ""

# Colors
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m'

# Check if venv exists
if [ ! -d "venv" ]; then
    echo -e "${RED}✗ Virtual environment not found. Run ./setup.sh first${NC}"
    exit 1
fi

# Activate virtual environment
source venv/bin/activate

echo -e "${BLUE}Starting SAATHI Platform...${NC}"
echo ""

# Start backend
echo -e "${GREEN}[1/2]${NC} Starting Backend API Server..."
echo -e "${YELLOW}→ Running on http://localhost:5000${NC}"
echo ""

cd backend
python app.py &
BACKEND_PID=$!

# Wait for backend to start
sleep 2

# Start frontend
echo -e "${GREEN}[2/2]${NC} Starting Frontend Server..."
echo -e "${YELLOW}→ Running on http://localhost:8000${NC}"
echo ""

cd ../website
python -m http.server 8000 &
FRONTEND_PID=$!

echo ""
echo "╔════════════════════════════════════════════════════════════╗"
echo -e "${GREEN}║         SAATHI Platform is Running! ✓                   ║${NC}"
echo "╚════════════════════════════════════════════════════════════╝"
echo ""
echo "🌐 Access Points:"
echo -e "   ${BLUE}Website: http://localhost:8000${NC}"
echo -e "   ${BLUE}API: http://localhost:5000${NC}"
echo -e "   ${BLUE}Health: http://localhost:5000/health${NC}"
echo ""
echo "📝 Demo Login:"
echo -e "   ${YELLOW}Email: personnel@saathi.local${NC}"
echo -e "   ${YELLOW}Password: demo123${NC}"
echo ""
echo -e "${YELLOW}Press Ctrl+C to stop all services${NC}"
echo ""

# Trap Ctrl+C
trap "kill $BACKEND_PID $FRONTEND_PID; exit" INT

# Wait for processes
wait
