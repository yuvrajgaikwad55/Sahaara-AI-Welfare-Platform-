from flask import Flask, jsonify, request
from flask_cors import CORS
from datetime import datetime, timedelta
import json
import random
import uuid

app = Flask(__name__)
CORS(app)

# In-memory database
users = {}
personnel = {}
wellness_data = []
risk_predictions = []
alerts = []
support_requests = []
interventions = []

# ==================== HEALTH CHECK ====================
@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({
        'status': 'healthy',
        'service': 'SAATHI API',
        'version': '2.0.0',
        'timestamp': datetime.now().isoformat()
    }), 200

# ==================== AUTHENTICATION ====================
@app.route('/api/v1/auth/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    
    if not email or not password:
        return jsonify({'error': 'Email and password required'}), 400
    
    # Determine role from email
    if 'personnel' in email:
        role = 'personnel'
    elif 'officer' in email:
        role = 'welfare_officer'
    elif 'commander' in email:
        role = 'commander'
    else:
        role = 'user'
    
    token = str(uuid.uuid4())
    users[token] = {'email': email, 'role': role, 'created_at': datetime.now()}
    
    return jsonify({
        'success': True,
        'data': {
            'token': token,
            'user': {
                'id': str(uuid.uuid4()),
                'email': email,
                'role': role,
                'name': email.split('@')[0].title()
            },
            'message': f'Welcome {email}'
        }
    }), 200

@app.route('/api/v1/auth/profile', methods=['GET'])
def get_profile():
    token = request.headers.get('Authorization', '').replace('Bearer ', '')
    if token not in users:
        return jsonify({'error': 'Unauthorized'}), 401
    
    user = users[token]
    return jsonify({
        'success': True,
        'data': {
            'id': str(uuid.uuid4()),
            'email': user['email'],
            'role': user['role'],
            'name': user['email'].split('@')[0].title()
        }
    }), 200

# ==================== WELLNESS ====================
@app.route('/api/v1/wellness/checkin', methods=['POST'])
def wellness_checkin():
    token = request.headers.get('Authorization', '').replace('Bearer ', '')
    data = request.get_json()
    
    checkin = {
        'id': str(uuid.uuid4()),
        'timestamp': datetime.now().isoformat(),
        'energy': data.get('energy', 5),
        'workload': data.get('workload', 5),
        'recovery': data.get('recovery', 5),
        'duty_demand': data.get('duty_demand', 5),
        'support_need': data.get('support_need', 'no')
    }
    wellness_data.append(checkin)
    
    return jsonify({
        'success': True,
        'data': checkin,
        'message': 'Wellness check-in recorded'
    }), 201

@app.route('/api/v1/wellness/dashboard', methods=['GET'])
def wellness_dashboard():
    if not wellness_data:
        return jsonify({
            'success': True,
            'data': {
                'current_status': 'Good',
                'energy': 7,
                'workload': 5,
                'recovery': 6,
                'trend': 'improving'
            }
        }), 200
    
    latest = wellness_data[-1]
    return jsonify({
        'success': True,
        'data': {
            'current_status': 'Good' if latest['energy'] > 5 else 'Needs Attention',
            'energy': latest['energy'],
            'workload': latest['workload'],
            'recovery': latest['recovery'],
            'duty_demand': latest['duty_demand'],
            'last_checkin': latest['timestamp'],
            'trend': 'improving' if latest['energy'] > 5 else 'declining'
        }
    }), 200

# ==================== PREDICTIONS ====================
@app.route('/api/v1/predictions/explain', methods=['GET'])
def predict_with_explanation():
    stress_level = random.randint(30, 80)
    
    if stress_level < 40:
        risk_level = 'LOW'
        color = 'green'
    elif stress_level < 60:
        risk_level = 'MODERATE'
        color = 'yellow'
    elif stress_level < 75:
        risk_level = 'ELEVATED'
        color = 'orange'
    else:
        risk_level = 'HIGH'
        color = 'red'
    
    prediction = {
        'id': str(uuid.uuid4()),
        'timestamp': datetime.now().isoformat(),
        'stress_level': stress_level,
        'risk_level': risk_level,
        'color': color,
        'confidence': round(random.uniform(0.80, 0.99), 2),
        'factors': [
            {'name': 'Workload Pattern', 'impact': random.randint(10, 30)},
            {'name': 'Recovery Time', 'impact': random.randint(10, 25)},
            {'name': 'Deployment Duration', 'impact': random.randint(5, 20)},
            {'name': 'Sleep Quality', 'impact': random.randint(5, 15)}
        ],
        'recommendation': f'Personnel shows {risk_level} stress indicators. Recommend monitoring and supportive measures.',
        'explanation': f'Based on recent wellness data and workload patterns, the AI model predicts {risk_level} stress risk with {round(random.uniform(0.80, 0.99), 2)*100}% confidence.'
    }
    
    risk_predictions.append(prediction)
    
    return jsonify({
        'success': True,
        'data': prediction
    }), 200

# ==================== SUPPORT & INTERVENTIONS ====================
@app.route('/api/v1/support/request', methods=['POST'])
def create_support_request():
    data = request.get_json()
    
    support_req = {
        'id': str(uuid.uuid4()),
        'category': data.get('category', 'general'),
        'description': data.get('description', ''),
        'status': 'pending',
        'created_at': datetime.now().isoformat(),
        'assigned_to': None
    }
    support_requests.append(support_req)
    
    return jsonify({
        'success': True,
        'data': support_req,
        'message': 'Support request created. Welfare officer will review soon.'
    }), 201

@app.route('/api/v1/support/requests', methods=['GET'])
def get_support_requests():
    return jsonify({
        'success': True,
        'data': support_requests,
        'count': len(support_requests)
    }), 200

@app.route('/api/v1/support/resources', methods=['GET'])
def get_resources():
    resources = [
        {
            'id': '1',
            'title': 'Stress Management Guide',
            'category': 'wellness',
            'url': '#',
            'description': 'Comprehensive guide for managing occupational stress'
        },
        {
            'id': '2',
            'title': 'Mental Health Awareness',
            'category': 'training',
            'url': '#',
            'description': 'Understanding mental health in uniformed services'
        },
        {
            'id': '3',
            'title': 'Meditation & Mindfulness',
            'category': 'wellness',
            'url': '#',
            'description': 'Daily exercises for stress relief'
        },
        {
            'id': '4',
            'title': 'Physical Fitness Program',
            'category': 'physical',
            'url': '#',
            'description': 'Fitness activities and routines'
        },
        {
            'id': '5',
            'title': 'Sleep and Recovery',
            'category': 'wellness',
            'url': '#',
            'description': 'Improving sleep quality and recovery'
        },
        {
            'id': '6',
            'title': 'Counseling Services',
            'category': 'support',
            'url': '#',
            'description': 'Professional counseling support available 24/7'
        }
    ]
    
    return jsonify({
        'success': True,
        'data': resources,
        'count': len(resources)
    }), 200

@app.route('/api/v1/support/counselors', methods=['GET'])
def get_counselors():
    counselors = [
        {
            'id': '1',
            'name': 'Dr. Anita Sharma',
            'specialization': 'PTSD & Trauma',
            'experience': '12 years',
            'availability': 'Mon-Wed 10:00-18:00',
            'rating': 4.8,
            'phone': '+91-XXXXXXX001'
        },
        {
            'id': '2',
            'name': 'Mr. Rajesh Kumar',
            'specialization': 'Stress Management',
            'experience': '8 years',
            'availability': 'Tue-Thu 14:00-20:00',
            'rating': 4.6,
            'phone': '+91-XXXXXXX002'
        },
        {
            'id': '3',
            'name': 'Ms. Priya Gupta',
            'specialization': 'Work-Life Balance',
            'experience': '10 years',
            'availability': 'Mon,Wed,Fri 09:00-17:00',
            'rating': 4.9,
            'phone': '+91-XXXXXXX003'
        }
    ]
    
    return jsonify({
        'success': True,
        'data': counselors,
        'count': len(counselors)
    }), 200

# ==================== DASHBOARD ====================
@app.route('/api/v1/dashboard/overview', methods=['GET'])
def dashboard_overview():
    return jsonify({
        'success': True,
        'data': {
            'total_personnel': random.randint(1000, 5000),
            'wellness_score': random.randint(65, 85),
            'at_risk': random.randint(10, 100),
            'support_requests': len(support_requests),
            'completed_interventions': random.randint(5, 50),
            'trends': {
                'stress_level': random.randint(30, 70),
                'improvement': '+5-8%',
                'risk_reduction': '+3-5%'
            }
        }
    }), 200

# ==================== WORKLOAD ====================
@app.route('/api/v1/workload/current', methods=['GET'])
def get_workload():
    return jsonify({
        'success': True,
        'data': {
            'duty_hours_today': random.randint(6, 12),
            'shift_type': random.choice(['morning', 'afternoon', 'night']),
            'rest_period': random.randint(4, 8),
            'consecutive_days': random.randint(1, 10),
            'deployment_duration': random.randint(1, 30),
            'workload_status': random.choice(['normal', 'elevated', 'high'])
        }
    }), 200

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
    ║              SAATHI - AI Welfare Intelligence Platform              ║
    ║                     API Server v2.0                                  ║
    ║════════════════════════════════════════════════════════════║
    ║  Local: http://localhost:5000                                      ║
    ║  Health: http://localhost:5000/health                               ║
    ║  Docs: Check API_DOCS.md for endpoints                              ║
    ║════════════════════════════════════════════════════════════║
    ║  Key Endpoints:                                                      ║
    ║  • POST   /api/v1/auth/login                                       ║
    ║  • POST   /api/v1/wellness/checkin                                ║
    ║  • GET    /api/v1/wellness/dashboard                             ║
    ║  • GET    /api/v1/predictions/explain                            ║
    ║  • POST   /api/v1/support/request                                ║
    ║  • GET    /api/v1/dashboard/overview                             ║
    ╚════════════════════════════════════════════════════════════╝
    """)
    app.run(debug=True, host='0.0.0.0', port=5000)
