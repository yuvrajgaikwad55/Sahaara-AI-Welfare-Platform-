# SAATHI - AI-Powered Personnel Stress & Welfare Intelligence Platform

**Tagline:** *Early support. Better welfare. Stronger readiness.*

## 🎯 Project Overview

SAATHI is a privacy-first, explainable AI platform designed to identify early indicators of occupational stress, fatigue, and welfare concerns in uniformed forces. The system enables authorized welfare teams to provide timely, evidence-based support.

### Key Philosophy
- **Welfare-focused**: Support, not surveillance
- **Explainable AI**: Personnel and officers understand why AI flags concerns
- **Human-in-the-loop**: AI recommends; humans decide
- **Privacy-first**: Minimal data collection, role-based access, audit logs
- **Trend-based**: Identifies patterns, not isolated incidents

## 🏗️ System Architecture

```
                    SAATHI Platform
                         │
            ┌────────────┼────────────┐
            │            │            │
       PERSONNEL      WELFARE       ADMIN
        PORTAL        OFFICER       PANEL
            │          DASHBOARD       │
            │            │            │
            └────────────┼────────────┘
                         │
                    API Gateway
                    (Auth, Rate Limit)
                         │
         ┌───────────────┼───────────────┐
         │               │               │
    ┌────▼─────┐  ┌─────▼──────┐  ┌────▼──────┐
    │ Personnel │  │  Wellness  │  │ Workload  │
    │ Management│  │  Analytics │  │ Analytics │
    └────┬─────┘  └─────┬──────┘  └────┬──────┘
         │               │              │
         └───────────────┼──────────────┘
                         │
            ┌────────────▼────────────┐
            │   AI ANALYTICS ENGINE   │
            │                         │
            │  • Stress Prediction    │
            │  • Fatigue Detection    │
            │  • Burnout Risk         │
            │  • Welfare Indicators   │
            │  • Explainable Results  │
            └────────────┬────────────┘
                         │
            ┌────────────┴────────────┐
            │                         │
       PostgreSQL                 Redis Cache
         Database                      │
         (Personnel,              (Sessions,
          Wellness,               Predictions,
          Predictions,            Trends)
          Interventions)
```

## 📱 Core Modules

### 1. Personnel Wellness Portal
- Personal dashboard with wellness status
- Daily wellness check-in (5 quick questions)
- Stress & burnout assessment
- Workload perception
- Sleep/recovery indicators
- Wellness trend visualization
- AI-generated recommendations
- Support request system
- Privacy settings
- Data access log

### 2. AI Prediction Engine
- Stress indicator (multi-factor)
- Fatigue indicator
- Burnout risk score
- Welfare support indicator
- Explainable AI (feature importance)
- Risk level classification (🟢🟡🟠🔴)
- Confidence scoring
- Trend analysis

### 3. Welfare Officer Dashboard
- Personnel monitoring (with authorization)
- Risk distribution analytics
- Trending concerns
- Support request queue
- Intervention management
- Outcome tracking
- Report generation
- Alert system

### 4. Commander Dashboard
- Unit-level aggregated trends
- Workload distribution analysis
- Deployment analytics
- Welfare planning
- Readiness indicators
- No individual personal data

### 5. Workload Intelligence
- Duty hour tracking
- Shift pattern analysis
- Rest interval monitoring
- Deployment duration
- Leave utilization
- Training load
- Workload recommendations
- Balancing suggestions

### 6. Support & Interventions
- Support request categorization
- Welfare officer assignment
- Intervention tracking
- Outcome recording
- Follow-up scheduling
- Effectiveness monitoring

## 🔐 Security & Privacy

✅ JWT-based authentication
✅ Role-Based Access Control (RBAC)
✅ Password hashing (bcrypt)
✅ HTTPS/TLS encryption
✅ Audit logging (all actions)
✅ Session management
✅ Input validation & sanitization
✅ Pseudonymous personnel IDs
✅ Data minimization principle
✅ No AI-based disciplinary action
✅ Explicit data access policies
✅ User privacy controls

## 🛠️ Technology Stack

### Frontend
- **Next.js** + React + TypeScript
- **Tailwind CSS** + shadcn/ui
- **Recharts** for analytics
- **Lucide Icons**
- **React Query** for data fetching

### Backend
- **Node.js** + Express.js
- **TypeScript**
- **PostgreSQL** (primary database)
- **Redis** (caching)
- **JWT** (authentication)
- **Winston** (logging)

### ML/AI Engine
- **Python** + FastAPI
- **Pandas** (data processing)
- **scikit-learn** (ML models)
- **XGBoost/Random Forest** (predictions)
- **SHAP** (explainability)
- **joblib** (model serialization)

### Deployment
- **Docker** + Docker Compose
- **GitHub Actions** (CI/CD)
- **AWS/Azure** ready

## 📊 Database Schema

```sql
Tables:
- users (authentication, roles)
- personnel (basic info, unit)
- wellness_checkins (daily responses)
- workload_records (duty tracking)
- risk_predictions (AI outputs)
- support_requests (welfare requests)
- interventions (actions taken)
- audit_logs (all system actions)
```

## 🚀 Quick Start

```bash
# Setup
chmod +x start.sh
./start.sh

# Run
./run.sh

# Access
# Website: http://localhost:3000
# API: http://localhost:5000
# ML Engine: http://localhost:8000
```

## 📖 Documentation

- [QUICKSTART.md](QUICKSTART.md) - 5-minute setup
- [DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md) - Production deployment
- [ARCHITECTURE.md](ARCHITECTURE.md) - Detailed system design
- [API_DOCS.md](API_DOCS.md) - API reference
- [AI_MODEL_DOCS.md](AI_MODEL_DOCS.md) - ML model documentation

## ✨ Unique SIH Features

### 1. Explainable AI
Not just a risk score, but clear explanation of contributing factors

### 2. Trend-Based Detection
Identifies patterns over time, not just single responses

### 3. What-If Workload Simulator
Test impact of workload adjustments on wellness indicators

### 4. Privacy-First Design
Minimal data collection, explicit access controls, audit trails

### 5. Intervention Effectiveness Tracking
Measure impact of welfare interventions

### 6. Workload Balancing
Connect welfare analytics to operational planning

### 7. Human-in-Loop
AI recommends; authorized humans decide

### 8. Non-Disciplinary
Explicit guarantee: system for support, not punishment

## 🎯 Use Cases

### For Personnel
1. Track personal wellness trends
2. Request confidential support
3. Understand wellness factors
4. Access wellness resources
5. Control data privacy

### For Welfare Officers
1. Identify personnel needing support
2. Understand underlying factors
3. Plan targeted interventions
4. Track support outcomes
5. Generate welfare reports

### For Commanders
1. Monitor unit welfare trends
2. Understand workload impact
3. Plan deployment rotation
4. Assess readiness
5. Allocate welfare resources

## 📈 Expected Outcomes

✅ Early identification of welfare concerns
✅ Reduced stress-related incidents
✅ Improved personnel retention
✅ Better workload planning
✅ Enhanced organizational readiness
✅ Data-driven welfare decisions
✅ Prevention of crisis situations
✅ Improved personnel satisfaction

## 🔄 Development Status

- ✅ Architecture design
- ✅ Frontend framework setup
- ✅ Backend API structure
- ✅ Database schema
- ⏳ UI/UX implementation
- ⏳ API endpoints
- ⏳ ML model development
- ⏳ Authentication system
- ⏳ Testing & QA
- ⏳ Deployment automation

## 📝 Important Notes

**PROTOTYPE NOTICE**: This is a demonstration prototype using simulated data. Not for production use with real personnel information without proper security audit and institutional approval.

**ETHICAL AI**: This system is explicitly designed as a welfare-support platform, not a surveillance or disciplinary system.

**PRIVACY**: No personal data is unnecessarily collected or exposed. Role-based access ensures appropriate information sharing.

## 🤝 Contributing

This is a Smart India Hackathon (SIH) project. Contributions welcome for enhancement.

## 📞 Support

For questions or issues, refer to documentation files or open an issue.

---

**Version**: 2.0 (SAATHI Edition)
**Status**: Active Development
**Last Updated**: September 2026
