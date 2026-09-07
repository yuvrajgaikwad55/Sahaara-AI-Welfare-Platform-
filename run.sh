#!/bin/bash

echo "🚀 Starting Sahaara AI Welfare Platform"
echo "=========================================="
echo ""

# Activate virtual environment
if [ ! -d "venv" ]; then
    echo "❌ Virtual environment not found. Run ./start.sh first"
    exit 1
fi

source venv/bin/activate

echo "📂 Starting Backend Server..."
echo "   🔗 API URL: http://localhost:5000"
echo "   📚 Health Check: http://localhost:5000/health"
echo ""

cd backend
python app.py &
BACKEND_PID=$!

echo "📂 Starting Frontend Server..."
echo "   🌐 Website URL: http://localhost:8000"
echo ""

cd ../website
python -m http.server 8000 &
FRONTEND_PID=$!

echo "=========================================="
echo "✅ Sahaara Platform is Running!"
echo "=========================================="
echo ""
echo "📊 Dashboard: http://localhost:8000"
echo "🔌 API Server: http://localhost:5000"
echo ""
echo "🛑 To stop: Press Ctrl+C (or kill PIDs: $BACKEND_PID, $FRONTEND_PID)"
echo ""

wait
