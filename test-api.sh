#!/bin/bash

echo ""
echo "╔════════════════════════════════════════════════════════════╗"
echo "║    SAATHI - Test API Endpoints (Local Development)         ║"
echo "╚════════════════════════════════════════════════════════════╝"
echo ""

BASE_URL="http://localhost:5000"
API_URL="$BASE_URL/api/v1"

# Colors
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m'

echo -e "${BLUE}Testing SAATHI API Endpoints${NC}"
echo ""

# Test 1: Health Check
echo -e "${GREEN}[Test 1]${NC} Health Check"
echo -e "${YELLOW}GET $BASE_URL/health${NC}"
curl -s $BASE_URL/health | jq . || echo "Failed to connect"
echo ""
echo ""

# Test 2: Login
echo -e "${GREEN}[Test 2]${NC} Personnel Login"
echo -e "${YELLOW}POST $API_URL/auth/login${NC}"
TOKEN=$(curl -s -X POST $API_URL/auth/login \
  -H "Content-Type: application/json" \
  -d '{
    "email": "personnel@saathi.local",
    "password": "demo123"
  }' | jq -r '.data.token' 2>/dev/null)

if [ ! -z "$TOKEN" ] && [ "$TOKEN" != "null" ]; then
    echo -e "${GREEN}✓ Login successful${NC}"
    echo "Token: ${TOKEN:0:20}..."
else
    echo -e "${YELLOW}⚠ Login response (check if API is running)${NC}"
    curl -s -X POST $API_URL/auth/login \
      -H "Content-Type: application/json" \
      -d '{"email": "personnel@saathi.local", "password": "demo123"}' | jq .
fi
echo ""
echo ""

# Test 3: Submit Wellness
echo -e "${GREEN}[Test 3]${NC} Submit Wellness Check-in"
echo -e "${YELLOW}POST $API_URL/wellness/checkin${NC}"
curl -s -X POST $API_URL/wellness/checkin \
  -H "Authorization: Bearer test_token" \
  -H "Content-Type: application/json" \
  -d '{
    "energy": 7,
    "workload": 6,
    "recovery": 5,
    "duty_demand": 8,
    "support_need": "no"
  }' | jq . || echo "API not responding"
echo ""
echo ""

# Test 4: Get Dashboard
echo -e "${GREEN}[Test 4]${NC} Get Wellness Dashboard"
echo -e "${YELLOW}GET $API_URL/wellness/dashboard${NC}"
curl -s -X GET $API_URL/wellness/dashboard \
  -H "Authorization: Bearer test_token" | jq . || echo "API not responding"
echo ""
echo ""

# Test 5: Get AI Prediction
echo -e "${GREEN}[Test 5]${NC} Get AI Prediction with Explanation"
echo -e "${YELLOW}GET $API_URL/predictions/explain${NC}"
curl -s -X GET $API_URL/predictions/explain \
  -H "Authorization: Bearer test_token" | jq . || echo "API not responding"
echo ""
echo ""

echo -e "${BLUE}Testing Complete!${NC}"
echo ""
echo "💡 Tips:"
echo "  - Make sure backend is running on port 5000"
echo "  - Use actual token from login response in tests"
echo "  - Check backend console for errors"
echo ""
