# SAATHI API Documentation

## Base URL
```
http://localhost:5000/api/v1
```

## Authentication
All endpoints require JWT token in Authorization header:
```
Authorization: Bearer <token>
```

## Endpoints

### Auth
```
POST   /auth/login              # Login
GET    /auth/profile            # Get user profile
POST   /auth/logout             # Logout
```

### Personnel Wellness
```
POST   /wellness/checkin        # Submit wellness check-in
GET    /wellness/history        # Get wellness history
GET    /wellness/dashboard      # Get wellness dashboard
GET    /wellness/trends         # Get wellness trends
```

### AI Predictions
```
GET    /predictions/latest      # Get latest prediction
GET    /predictions/explain     # Get explanation
GET    /predictions/trends      # Get prediction trends
```

### Support & Interventions
```
POST   /support/request         # Create support request
GET    /support/requests        # Get support requests
GET    /support/resources       # Get welfare resources
GET    /support/counselors      # Get counselor list
```

### Workload
```
GET    /workload/current        # Current workload
GET    /workload/history        # Workload history
GET    /workload/analytics      # Workload analytics
```

### Officer Dashboard (Welfare Officers Only)
```
GET    /officer/dashboard       # Officer dashboard
GET    /officer/cases           # Assigned cases
GET    /officer/analytics       # Welfare analytics
POST   /officer/interventions   # Create intervention
```

### Commander Dashboard (Commanders Only)
```
GET    /commander/dashboard     # Commander dashboard
GET    /commander/unit-trends   # Unit trends
GET    /commander/workload      # Unit workload
```

## Example Requests

### Login
```bash
curl -X POST http://localhost:5000/api/v1/auth/login \
  -H "Content-Type: application/json" \
  -d '{
    "email": "personnel@saathi.local",
    "password": "demo123"
  }'
```

### Submit Wellness Check-in
```bash
curl -X POST http://localhost:5000/api/v1/wellness/checkin \
  -H "Authorization: Bearer <token>" \
  -H "Content-Type: application/json" \
  -d '{
    "energy": 7,
    "workload": 6,
    "recovery": 5,
    "duty_demand": 8,
    "support_need": "no"
  }'
```

### Get Wellness Dashboard
```bash
curl -X GET http://localhost:5000/api/v1/wellness/dashboard \
  -H "Authorization: Bearer <token>"
```

### Get AI Prediction with Explanation
```bash
curl -X GET http://localhost:5000/api/v1/predictions/explain \
  -H "Authorization: Bearer <token>"
```

## Response Format

### Success
```json
{
  "success": true,
  "data": { ... },
  "timestamp": "2026-09-07T12:00:00Z"
}
```

### Error
```json
{
  "success": false,
  "error": "Error message",
  "code": "ERROR_CODE",
  "timestamp": "2026-09-07T12:00:00Z"
}
```

## Status Codes
- 200: Success
- 201: Created
- 400: Bad Request
- 401: Unauthorized
- 403: Forbidden
- 404: Not Found
- 500: Server Error
