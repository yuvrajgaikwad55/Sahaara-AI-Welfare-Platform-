from flask import Flask, jsonify, request
from flask_cors import CORS
from datetime import datetime
import json

app = Flask(__name__)
CORS(app)

# Simulated database
staff_data = {}
alerts = []
wellness_records = {}

# ==================== HEALTH CHECK ====================
@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({
        'status': 'healthy',
        'service': 'Sahaara API',
        'timestamp': datetime.now().isoformat(),
        'version': '1.0.0'
    }), 200

# ==================== AUTHENTICATION ====================
@app.route('/api/auth/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    
    if not email or not password:
        return jsonify({'error': 'Email and password required'}), 400
    
    # Simulated authentication
    if email and password:
        return jsonify({
            'success': True,
            'token': f'token_{email}_{datetime.now().timestamp()}',
            'user': {
                'id': '12345',
                'name': 'John Doe',
                'email': email,
                'role': 'personnel'
            }
        }), 200
    
    return jsonify({'error': 'Invalid credentials'}), 401

@app.route('/api/auth/profile', methods=['GET'])
def get_profile():
    token = request.headers.get('Authorization')
    if not token:
        return jsonify({'error': 'Token required'}), 401
    
    return jsonify({
        'id': '12345',
        'name': 'John Doe',
        'email': 'john@example.com',
        'role': 'personnel',
        'department': 'CRPF',
        'designation': 'Constable'
    }), 200

# ==================== WELLNESS ====================
@app.route('/api/wellness/submit', methods=['POST'])
def submit_wellness():
    data = request.get_json()
    personnel_id = data.get('personnel_id', 'default')
    
    wellness_data = {
        'id': f'wellness_{len(wellness_records)}',
        'personnel_id': personnel_id,
        'timestamp': datetime.now().isoformat(),
        'stress_level': data.get('stress_level', 5),
        'sleep_quality': data.get('sleep_quality', 5),
        'mood': data.get('mood', 'neutral'),
        'physical_activity': data.get('physical_activity', 30),
        'notes': data.get('notes', '')
    }
    
    wellness_records[f'wellness_{len(wellness_records)}'] = wellness_data
    
    return jsonify({
        'success': True,
        'message': 'Wellness data recorded',
        'data': wellness_data
    }), 201

@app.route('/api/wellness/history/<personnel_id>', methods=['GET'])
def get_wellness_history(personnel_id):
    records = [v for v in wellness_records.values() if v.get('personnel_id') == personnel_id]
    
    return jsonify({
        'personnel_id': personnel_id,
        'count': len(records),
        'records': records
    }), 200

@app.route('/api/wellness/latest/<personnel_id>', methods=['GET'])
def get_latest_wellness(personnel_id):
    records = [v for v in wellness_records.values() if v.get('personnel_id') == personnel_id]
    
    if not records:
        return jsonify({'message': 'No wellness data found'}), 404
    
    latest = records[-1]
    return jsonify(latest), 200

# ==================== STRESS PREDICTION ====================
@app.route('/api/stress/predict/<personnel_id>', methods=['GET'])
def predict_stress(personnel_id):
    import random
    
    stress_level = random.randint(20, 85)
    
    if stress_level < 40:
        risk_category = 'LOW'
        recommendation = 'Personnel is in good mental health. Continue regular wellness activities.'
    elif stress_level < 60:
        risk_category = 'MODERATE'
        recommendation = 'Recommended: Increase physical activity and consider counseling sessions.'
    elif stress_level < 75:
        risk_category = 'HIGH'
        recommendation = 'Recommended: Schedule counseling session with welfare officer.'
    else:
        risk_category = 'CRITICAL'
        recommendation = 'URGENT: Contact welfare officer immediately. Consider temporary duty adjustment.'
    
    return jsonify({
        'personnel_id': personnel_id,
        'prediction': {
            'stress_level': stress_level,
            'risk_category': risk_category,
            'confidence': round(random.uniform(0.85, 0.99), 2),
            'timestamp': datetime.now().isoformat(),
            'recommendation': recommendation,
            'factors': [
                'Leave pattern changes',
                'Deployment frequency',
                'Work-life balance',
                'Recent incidents'
            ]
        }
    }), 200

@app.route('/api/stress/risk-level/<personnel_id>', methods=['GET'])
def get_risk_level(personnel_id):
    import random
    
    risk_level = random.choice(['LOW', 'MODERATE', 'HIGH', 'CRITICAL'])
    
    return jsonify({
        'personnel_id': personnel_id,
        'risk_level': risk_level,
        'last_updated': datetime.now().isoformat(),
        'next_assessment': '2026-09-14'
    }), 200

# ==================== ALERTS ====================
@app.route('/api/alerts', methods=['GET'])
def get_alerts():
    return jsonify({
        'count': len(alerts),
        'alerts': alerts
    }), 200

@app.route('/api/alerts/create', methods=['POST'])
def create_alert():
    data = request.get_json()
    
    alert = {
        'id': f'alert_{len(alerts)}',
        'personnel_id': data.get('personnel_id'),
        'type': data.get('type', 'stress_alert'),
        'severity': data.get('severity', 'medium'),
        'message': data.get('message', ''),
        'created_at': datetime.now().isoformat(),
        'status': 'active'
    }
    
    alerts.append(alert)
    
    return jsonify({
        'success': True,
        'alert': alert
    }), 201

# ==================== RESOURCES ====================
@app.route('/api/resources', methods=['GET'])
def get_resources():
    resources = [
        {
            'id': '1',
            'title': 'Mental Health Awareness',
            'category': 'training',
            'url': '#',
            'description': 'Understanding stress and mental health'
        },
        {
            'id': '2',
            'title': 'Meditation & Mindfulness',
            'category': 'wellness',
            'url': '#',
            'description': 'Daily meditation exercises for stress relief'
        },
        {
            'id': '3',
            'title': 'Fitness Program',
            'category': 'physical',
            'url': '#',
            'description': 'Physical fitness activities and routines'
        },
        {
            'id': '4',
            'title': 'Counseling Services',
            'category': 'support',
            'url': '#',
            'description': 'Professional counseling support'
        }
    ]
    
    return jsonify({
        'count': len(resources),
        'resources': resources
    }), 200

@app.route('/api/resources/counselors', methods=['GET'])
def get_counselors():
    counselors = [
        {
            'id': '1',
            'name': 'Dr. Anita Sharma',
            'specialization': 'PTSD & Trauma',
            'availability': 'Mon-Wed 10:00-18:00',
            'phone': '+91-XXXXXXX001',
            'rating': 4.8
        },
        {
            'id': '2',
            'name': 'Mr. Rajesh Kumar',
            'specialization': 'Stress Management',
            'availability': 'Tue-Thu 14:00-20:00',
            'phone': '+91-XXXXXXX002',
            'rating': 4.6
        },
        {
            'id': '3',
            'name': 'Ms. Priya Gupta',
            'specialization': 'Work-Life Balance',
            'availability': 'Mon,Wed,Fri 09:00-17:00',
            'phone': '+91-XXXXXXX003',
            'rating': 4.9
        }
    ]
    
    return jsonify({
        'count': len(counselors),
        'counselors': counselors
    }), 200

# ==================== DASHBOARD ====================
@app.route('/api/dashboard/overview', methods=['GET'])
def dashboard_overview():
    import random
    
    return jsonify({
        'total_personnel': 1250,
        'wellness_score': random.randint(65, 85),
        'at_risk_count': random.randint(10, 50),
        'recent_alerts': len(alerts),
        'counseling_sessions': random.randint(5, 25),
        'trends': {
            'stress_level': random.randint(30, 70),
            'improvement': '+5%',
            'risk_reduction': '+8%'
        },
        'timestamp': datetime.now().isoformat()
    }), 200

@app.route('/api/dashboard/alerts', methods=['GET'])
def dashboard_alerts():
    critical_alerts = [a for a in alerts if a.get('severity') == 'high']
    
    return jsonify({
        'critical_count': len(critical_alerts),
        'total_count': len(alerts),
        'recent_alerts': alerts[-5:] if alerts else []
    }), 200

# ==================== INTERVENTIONS ====================
@app.route('/api/interventions', methods=['POST'])
def create_intervention():
    data = request.get_json()
    
    intervention = {
        'id': f'intervention_{len(alerts)}',
        'personnel_id': data.get('personnel_id'),
        'type': data.get('type', 'counseling'),
        'description': data.get('description', ''),
        'status': 'scheduled',
        'created_at': datetime.now().isoformat(),
        'scheduled_date': data.get('scheduled_date')
    }
    
    return jsonify({
        'success': True,
        'intervention': intervention
    }), 201

# ==================== ERROR HANDLERS ====================
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Endpoint not found'}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    print("""
    ╔════════════════════════════════════════════════════════════╗
    ║        Sahaara AI Welfare Platform - Backend API            ║
    ║════════════════════════════════════════════════════════════║
    ║  🔗 Local: http://localhost:5000                            ║
    ║  📚 Docs: http://localhost:5000/api/docs                   ║
    ║  ✅ Health: http://localhost:5000/health                   ║
    ║════════════════════════════════════════════════════════════║
    ║  Endpoints Available:                                       ║
    ║  • POST   /api/auth/login                                  ║
    ║  • GET    /api/auth/profile                                ║
    ║  • POST   /api/wellness/submit                             ║
    ║  • GET    /api/wellness/history/<id>                       ║
    ║  • GET    /api/stress/predict/<id>                         ║
    ║  • GET    /api/alerts                                      ║
    ║  • GET    /api/resources                                   ║
    ║  • GET    /api/dashboard/overview                          ║
    ╚════════════════════════════════════════════════════════════╝
    """)
    app.run(debug=True, host='0.0.0.0', port=5000)
