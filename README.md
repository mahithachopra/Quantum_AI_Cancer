# ⚛️🧬 Quantum AI Cancer Platform

> **An AI + Quantum Machine Learning Powered Precision Oncology Clinical Decision Support System**

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-009688.svg)
![React](https://img.shields.io/badge/React-19-blue.svg)
![Material UI](https://img.shields.io/badge/Material_UI-MUI-blue.svg)
![Quantum Machine Learning](https://img.shields.io/badge/QML-QSVC%20%7C%20QNN-purple.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

---

# 📖 Overview

**Quantum AI Cancer Platform** is a full-stack **Artificial Intelligence (AI)** and **Quantum Machine Learning (QML)** powered precision oncology clinical decision support system designed to assist researchers and healthcare professionals in mutation-driven cancer therapy analysis.

The platform combines **classical AI**, **Quantum Machine Learning**, **Explainable AI (XAI)**, biomedical literature mining, and clinical trial matching into a unified intelligent platform for personalized oncology recommendations.

Unlike traditional AI systems, this project incorporates **Quantum Support Vector Classifiers (QSVC)** and **Quantum Neural Networks (QNN)** to investigate hybrid AI–Quantum approaches for precision medicine.

---

# 🎯 Objectives

- Analyze genomic mutations
- Identify actionable biomarkers
- Recommend targeted therapies
- Match clinical trials
- Mine biomedical literature
- Explain AI decisions using XAI
- Generate professional clinical reports
- Explore Quantum Machine Learning for precision oncology

---

# 🚀 Key Features

## 🧬 Mutation Analysis

- Gene mutation input
- Mutation summary
- Biomarker analysis
- Pathway analysis
- AI pipeline visualization

---

## 💊 Drug Recommendation Engine

- AI-powered targeted therapy recommendations
- Drug confidence scoring
- FDA evidence
- Recommendation ranking

---

## ⚛️ Quantum Machine Learning

Integrated Quantum AI modules include:

- Quantum Feature Maps
- Quantum Kernel Learning
- Quantum Support Vector Classifier (QSVC)
- Quantum Neural Networks (QNN)
- Hybrid AI–Quantum inference pipeline

These components complement classical AI models to explore quantum-enhanced predictive analytics for cancer precision medicine.

---

## 🔍 Explainable AI (XAI)

- AI reasoning pipeline
- Confidence breakdown
- Evidence scoring
- Decision workflow
- Supporting literature
- Supporting clinical trials

---

## 📚 Biomedical Literature Mining

- Literature retrieval
- Research evidence
- Publication summaries
- Scientific references

---

## 🧪 Clinical Trial Matching

- Ongoing trials
- Trial phases
- Recruitment status
- Matching based on genomic mutations

---

## 📄 Clinical Report Generation

Generate professional reports including:

- Executive Summary
- Patient mutation profile
- Drug recommendations
- Literature summary
- Clinical trials
- PDF Export
- CSV Export
- Print Support

---

## ⚙️ System Settings

- AI Configuration
- Pipeline Settings
- Appearance
- Notifications
- Security
- Database Connections
- System Information

---

# 🏗️ System Architecture

```
                    ┌──────────────────────┐
                    │   React Frontend     │
                    │  Material UI + Vite  │
                    └──────────┬───────────┘
                               │
                     REST API (FastAPI)
                               │
            ┌──────────────────┼──────────────────┐
            │                  │                  │
            ▼                  ▼                  ▼
      AI Pipeline       Quantum ML         Knowledge Base
     (ML Models)      QSVC / QNN           Literature
            │                  │
            └──────────┬───────┘
                       ▼
              Hybrid AI Decision Engine
                       │
        ┌──────────────┼──────────────┐
        ▼              ▼              ▼
 Drug Ranking    Clinical Trials   Literature
        │
        ▼
 Explainable AI
        │
        ▼
 Clinical Reports
```

---

# ⚛️ AI + Quantum Workflow

```
Patient Mutation Data
        │
        ▼
Mutation Detection
        │
        ▼
Feature Engineering
        │
        ├──────────────┐
        ▼              ▼
 Classical AI      Quantum ML
                    QSVC / QNN
        └──────┬───────┘
               ▼
 Hybrid AI–Quantum Ranking
               ▼
Drug Recommendation
               ▼
Evidence Aggregation
               ▼
Clinical Trials
               ▼
Literature Mining
               ▼
Explainable AI
               ▼
Clinical Report
```

---

# 💻 Technology Stack

## Frontend

- React
- Material UI
- React Router
- Axios
- Recharts
- jsPDF
- html2canvas

---

## Backend

- FastAPI
- Python
- Pandas
- NumPy
- Scikit-learn
- Pydantic

---

## Quantum Machine Learning

- Quantum Support Vector Classifier (QSVC)
- Quantum Neural Networks (QNN)
- Quantum Kernels
- Feature Maps
- Hybrid Quantum-Classical Learning

---

## AI Components

- Mutation Analysis
- Drug Ranking
- Knowledge Graph
- Literature Mining
- Clinical Trial Matching
- Explainable AI

---

# 📂 Project Structure

```
Quantum_AI_Cancer/

├── backend/
│   ├── app/
│   ├── api/
│   ├── models/
│   ├── services/
│   ├── qml/
│   │   ├── qsvc.py
│   │   ├── qnn.py
│   │   ├── feature_maps.py
│   │   ├── kernels.py
│   │   └── predictor.py
│   └── requirements.txt
│
├── frontend/
│   ├── src/
│   │
│   ├── pages/
│   │   ├── Dashboard
│   │   ├── Mutation Analysis
│   │   ├── Recommendations
│   │   ├── Clinical Trials
│   │   ├── Literature
│   │   ├── Explainability
│   │   ├── Reports
│   │   └── Settings
│   │
│   ├── components/
│   └── services/
│
└── README.md
```

---

# 📸 Application Modules

- Dashboard
- Mutation Analysis
- Drug Recommendations
- Explainable AI (XAI)
- Clinical Trials
- Literature Mining
- Clinical Reports
- Settings

---

# ⚡ Installation

## Clone Repository

```bash
git clone https://github.com/<your-username>/Quantum_AI_Cancer.git

cd Quantum_AI_Cancer
```

---

## Backend

```bash
cd backend

python -m venv venv

source venv/bin/activate

pip install -r requirements.txt

uvicorn app.main:app --reload
```

Backend runs at

```
http://localhost:8000
```

---

## Frontend

```bash
cd frontend

npm install

npm run dev
```

Frontend runs at

```
http://localhost:5173
```

---

# 📊 Implemented Modules

| Module | Status |
|---------|--------|
| Dashboard | ✅ |
| Mutation Analysis | ✅ |
| Drug Recommendation | ✅ |
| Explainable AI | ✅ |
| Literature Mining | ✅ |
| Clinical Trials | ✅ |
| Clinical Reports | ✅ |
| PDF Export | ✅ |
| CSV Export | ✅ |
| Print Support | ✅ |
| Settings | ✅ |
| Quantum ML | ✅ |

---

# 🔮 Future Enhancements

- Authentication & Authorization
- Patient Management
- Electronic Health Record (EHR) Integration
- Docker Deployment
- PostgreSQL Database
- Role-Based Access Control
- Cloud Deployment
- SHAP/LIME Explainability
- Real Clinical Data Integration
- Multi-Cancer Support

---

# 🎓 Research Significance

This project demonstrates the integration of **Artificial Intelligence**, **Quantum Machine Learning**, and **Explainable AI** for precision oncology.

It serves as a research prototype exploring hybrid AI–Quantum approaches for mutation-driven cancer treatment recommendation and evidence-supported clinical decision support.

---

# ⚠️ Disclaimer

This software is intended **only for educational and research purposes**.

It is **not a certified medical device** and should **not be used for clinical diagnosis, treatment decisions, or patient care**.

---

# 👩‍💻 Author

**Mahitha Chopra Lankapalli**

M.Sc. Artificial Intelligence & Data Science

Artificial Intelligence • Quantum Machine Learning • Precision Oncology • Healthcare AI

---

# 📜 License

This project is licensed under the **MIT License**.
