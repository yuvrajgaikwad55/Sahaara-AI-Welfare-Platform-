# SAATHI AI Model Documentation

## Model Overview

SAATHI uses ensemble machine learning models to predict welfare indicators from personnel data.

## Input Features

### Wellness Data (from check-ins)
- Energy level (1-10)
- Workload perception (1-10)
- Recovery quality (1-10)
- Duty demand (1-10)
- Support need (binary)

### Work Data
- Duty hours
- Shift type
- Rest period
- Consecutive duty days
- Deployment duration
- Leave usage
- Training load

### Historical Data
- Previous wellness trends
- Historical workload patterns
- Deployment history
- Leave patterns
- Risk trend

## Output Indicators

### Stress Indicator
- Range: 0-100
- 🟢 Low: <40
- 🟡 Moderate: 40-60
- 🟠 Elevated: 60-75
- 🔴 High: >75

### Fatigue Indicator
- Range: 0-100
- Based on: Rest periods, consecutive duty, recovery quality

### Burnout Risk
- Range: 0-100
- Based on: Long-term stress, recovery, deployment duration

### Welfare Support Indicator
- Range: 0-100
- Combined factor of all above
- Triggers interventions when >70

## Model Architecture

```
Input Features
      │
      ▼
Data Validation
      │
      ▼
Feature Engineering
  • Normalize
  • Create interactions
  • Temporal features
      │
      ▼
Ensemble Models
  • Random Forest
  • XGBoost
  • Neural Network
      │
      ▼
Prediction Aggregation
      │
      ▼
Explainability (SHAP)
      │
      ▼
Risk Level Classification
      │
      ▼
Recommendation Engine
```

## Explainability

Using SHAP (SHapley Additive exPlanations):
- Feature importance ranking
- Individual feature contribution
- Why indicator is at this level
- Main contributing factors

Example output:
```
Stress Indicator: 65 (Elevated)

Top Contributing Factors:
1. High workload (↑ +25)
2. Reduced recovery (↑ +18)
3. Extended duty (↑ +15)
4. Recent trend (↑ +7)

Confidence: 82%
```

## Model Training

### Data
- Simulated synthetic dataset
- 5000+ personnel records
- 30+ features per record
- Multiple time series per personnel

### Process
1. Data collection
2. Feature engineering
3. Train-test split (80-20)
4. Cross-validation
5. Hyperparameter tuning
6. Model evaluation
7. SHAP explanation generation
8. Production deployment

### Metrics
- Accuracy: >85%
- Precision: >80%
- Recall: >85%
- F1-Score: >82%

## Prediction Workflow

```
Personnel Submits Data
      │
      ▼
Data Validation
      │
      ▼
Fetch Historical Data
      │
      ▼
Feature Engineering
      │
      ▼
Run Prediction Models
      │
      ▼
Aggregate Predictions
      │
      ▼
Generate Explanations
      │
      ▼
Classify Risk Level
      │
      ▼
Generate Recommendations
      │
      ▼
Alert if Risk > Threshold
      │
      ▼
Store Results
      │
      ▼
Update Dashboard
```

## Important Notes

**NOT A DIAGNOSIS TOOL**
- Does not diagnose mental health conditions
- Identifies welfare support indicators
- Complements professional assessment
- Requires human review

**EXPLAINABLE BY DESIGN**
- All predictions include explanations
- Personnel can understand why flagged
- Officers can review reasoning
- Transparent decision-making

**ETHICAL CONSIDERATIONS**
- No discriminatory bias testing needed
- Used for support, not punishment
- Human-in-loop decision-making
- Data minimization principle
- Privacy-first architecture

## Model Updates

- Retrained: Monthly
- Evaluation: Continuous
- Drift detection: Automatic
- Version control: Git-based
