#!/bin/bash

echo "========================================"
echo "Sahaara AI Welfare Platform - Quick Start"
echo "========================================"

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed"
    exit 1
fi

echo "✅ Python found: $(python3 --version)"

# Create virtual environment
echo "📦 Creating virtual environment..."
python3 -m venv venv
source venv/bin/activate

echo "✅ Virtual environment created"

# Install dependencies
echo "📥 Installing dependencies..."
pip install --upgrade pip
pip install -r backend/requirements.txt
npm install --prefix website 2>/dev/null || echo "⚠️  npm not available for website"

echo "✅ Dependencies installed"

echo ""
echo "========================================"
echo "Setup Complete! 🎉"
echo "========================================"
echo ""
echo "To start the application:"
echo "  Terminal 1: cd backend && python app.py"
echo "  Terminal 2: cd website && python -m http.server 8000"
echo ""
echo "Access points:"
echo "  🌐 Website:  http://localhost:8000"
echo "  🔌 API:      http://localhost:5000"
echo "  ✅ Health:   http://localhost:5000/health"
echo ""
