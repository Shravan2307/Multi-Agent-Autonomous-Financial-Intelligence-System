# 🤖 Multi-Agent Autonomous Financial Intelligence System

> **An AI-powered financial intelligence platform that transforms live market data, financial documents, and user risk profiles into transparent, personalized investment intelligence.**

## 📌 Overview

The **Multi-Agent Autonomous Financial Intelligence System** is a multi-agent AI platform designed for retail investors.

Instead of relying on a single AI model to analyze an investment, the system distributes financial reasoning across multiple specialized agents. Each agent independently analyzes a different dimension of the investment, and a central synthesis layer combines their outputs while considering the investor's personal risk profile.

The system is designed around four principles:

* **Multi-Agent Reasoning** — Multiple specialized agents analyze the same financial situation independently.
* **Personalization** — Recommendations adapt to the user's risk tolerance, investment horizon, and volatility tolerance.
* **Evidence-Based Intelligence** — Financial reasoning is grounded in market data and retrieved financial documents.
* **Graceful Degradation** — Missing data, unavailable feeds, and conflicting agent signals are handled safely without crashing the pipeline.

---

# 🎯 Problem

Retail investors often face several problems when making investment decisions:

* Financial information is scattered across multiple sources.
* Market data changes continuously.
* Regulatory filings are difficult to understand.
* Different financial indicators can provide conflicting signals.
* Generic investment advice does not consider an individual's risk profile.
* AI-generated financial explanations can lack transparent evidence.

Our system addresses these problems by creating an **autonomous financial reasoning pipeline** that combines multiple specialized agents, financial data retrieval, user profiling, conflict resolution, and evidence-based synthesis.

---

# 🧠 System Architecture

```text
                    ┌─────────────────────┐
                    │     User / UI       │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │      API Layer      │
                    └──────────┬──────────┘
                               │
                               ▼
                 ┌────────────────────────────┐
                 │   Financial Data Layer     │
                 │                            │
                 │  Market Data + RAG Data    │
                 └─────────────┬──────────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │    Orchestrator     │
                    └──────────┬──────────┘
                               │
                ┌──────────────┼──────────────┐
                │              │              │
                ▼              ▼              ▼
        ┌─────────────┐ ┌─────────────┐ ┌─────────────┐
        │ Fundamental │ │    Risk     │ │  Sentiment  │
        │    Agent    │ │    Agent    │ │    Agent    │
        └──────┬──────┘ └──────┬──────┘ └──────┬──────┘
               │               │               │
               └───────────────┼───────────────┘
                               ▼
                    ┌─────────────────────┐
                    │ Conflict Detection  │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │  Profile Weighting  │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │  Synthesis Engine   │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ Evidence + Reasoning│
                    │      Trace          │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ Final Intelligence  │
                    │     Response        │
                    └─────────────────────┘
```

---

# 🤖 Multi-Agent System

The system uses specialized agents instead of asking one model to perform every financial analysis task.

## 1. Fundamental Analysis Agent

Analyzes the company's underlying financial health.

It considers information such as:

* Revenue
* Revenue growth
* Earnings
* EPS
* Debt
* Cash
* Financial filings
* Earnings information
* Retrieved regulatory documents

The agent produces a structured financial signal together with supporting factors, risks, reasoning, and evidence.

---

## 2. Risk Analysis Agent

Evaluates the risk associated with the investment.

It considers:

* Volatility
* Debt exposure
* Market conditions
* Downside risks
* User risk tolerance
* Investment horizon

The output follows the same structured contract used by the other agents.

---

## 3. Sentiment / Market Agent

Analyzes market and news-related signals.

It considers:

* Price movement
* Market momentum
* Trading activity
* Recent news
* Market context
* Sentiment indicators

The agent produces an independent signal and confidence score.

---

# ⚙️ Multi-Agent Orchestration

The orchestrator executes the specialized agents **concurrently**.

Instead of:

```text
Agent 1 → Agent 2 → Agent 3
```

the system uses:

```text
             ┌─ Agent 1 ─┐
Input ───────┼─ Agent 2 ─┼──→ Synthesis
             └─ Agent 3 ─┘
```

This reduces unnecessary sequential waiting and allows each agent to independently reason over the same financial state.

Every agent follows a strict structured output schema so the synthesis layer can reliably consume their results.

---

# 👤 User Profiling

The system does not treat every investor the same.

A user profile can contain:

```json
{
  "risk_tolerance": "CONSERVATIVE",
  "investment_horizon": "LONG_TERM",
  "volatility_tolerance": "LOW"
}
```

These parameters influence the synthesis stage.

For example, the same market situation may produce different final intelligence for:

### Conservative Investor

```text
Low risk tolerance
+
Low volatility tolerance
+
Long-term horizon
        ↓
More defensive interpretation
```

### Aggressive Investor

```text
High risk tolerance
+
High volatility tolerance
+
Long-term horizon
        ↓
Greater tolerance for market risk
```

Therefore:

> **Same market data + different user profile = different personalized intelligence**

This is one of the core capabilities of the system.

---

# ⚖️ Conflict Resolution

Financial signals do not always agree.

For example:

```text
Fundamental Agent → BULLISH
Risk Agent        → BEARISH
Sentiment Agent   → BULLISH
```

The system detects this conflict rather than blindly selecting one result.

The synthesis pipeline considers:

* Agent signals
* Agent confidence
* User profile weights
* Available evidence
* Data quality
* Conflict severity

The system can then produce a qualified final result while preserving the conflict information in the reasoning trace.

---

# 📚 RAG & Financial Knowledge

The financial intelligence layer can retrieve relevant information from regulatory and financial documents.

The RAG pipeline is designed to support documents such as:

* Regulatory filings
* Corporate disclosures
* Earnings transcripts
* Financial reports

Retrieved chunks contain attribution metadata such as:

```text
Document Title
Document Date
Page Number
Clause / Section
Source
```

This allows the system to connect financial reasoning back to the underlying evidence.

---

# 📊 Market Data Layer

The market data layer provides quantitative information required by the agents.

The internal interface follows the concept of:

```python
get_market_snapshot(ticker)
```

The snapshot can contain:

```text
Open
High
Low
Close
Volume
Price Change
Volatility
Technical Indicators
```

The architecture supports live or near-real-time market data providers and simulated data for hackathon testing.

---

# 🛡️ Graceful Degradation

The system is designed not to fail when individual data sources become unavailable.

### Market Feed Failure

Instead of crashing:

```text
Market API Timeout
       ↓
DATA_UNAVAILABLE
       ↓
Agent receives degraded state
       ↓
Pipeline continues safely
```

### Missing Filing

Instead of generating unsupported information:

```text
No relevant filing found
       ↓
MISSING_FILING
       ↓
Agent reports insufficient evidence
       ↓
No unsupported citation is generated
```

### Conflicting Agents

```text
Agent A → BULLISH
Agent B → BEARISH
       ↓
Conflict detected
       ↓
Synthesis + confidence weighting
       ↓
Qualified final intelligence
```

---

# 🔎 Reasoning Transparency

The system maintains a structured reasoning trace throughout the pipeline.

The interface can expose:

```text
Input
  ↓
Data Retrieved
  ↓
Agent Analysis
  ↓
Agent Evidence
  ↓
Detected Conflicts
  ↓
User Profile Weighting
  ↓
Synthesis
  ↓
Final Intelligence
```

This allows users and judges to understand **why** the system reached its result instead of receiving only a final prediction.

---

# 🚀 End-to-End Flow

A typical request follows this path:

```text
User selects a stock
        ↓
Frontend sends analysis request
        ↓
API validates request
        ↓
Financial data is collected
        ↓
Relevant documents are retrieved
        ↓
Three agents execute concurrently
        ↓
Agent outputs are validated
        ↓
Conflicts are detected
        ↓
User profile weights are applied
        ↓
Synthesis engine generates final intelligence
        ↓
Evidence and reasoning trace are attached
        ↓
Final result returned to frontend
```

---

# 🧪 Testing

The project includes automated tests for:

* Agent output schemas
* Agent execution
* Concurrent execution
* API endpoints
* User profile validation
* Profile weighting
* Conflict detection
* Weighted synthesis
* Personalization
* Missing agent handling
* Graceful degradation
* Confidence and score bounds
* Evidence validation
* API integration

Run the backend tests:

```bash
cd backend
python -m pytest -v
```

A successful build should report all tests passing.

---

# 🛠️ Technology Stack

## Backend

* Python
* FastAPI
* Pydantic
* AsyncIO
* Pytest

## AI / Intelligence

* Multi-Agent Architecture
* Agent Orchestration
* Structured AI Outputs
* RAG
* Vector Search
* Evidence-Based Synthesis

## Data

* Market Data APIs
* Financial Filings
* Regulatory Documents
* Earnings Information
* Vector Database

## Frontend

* React
* JavaScript / TypeScript
* Modern component-based UI

## Deployment

The architecture is designed to be containerized and deployment-ready for PaaS environments.

---

# 📁 Project Structure

```text
Multi-Agent-Autonomous-Financial-Intelligence-System/
│
├── backend/
│   ├── app/
│   │   ├── agents/
│   │   │   ├── base.py
│   │   │   ├── fundamental.py
│   │   │   ├── risk.py
│   │   │   └── sentiment.py
│   │   │
│   │   ├── api/
│   │   │   └── routes/
│   │   │
│   │   ├── decision/
│   │   │   ├── conflict_detector.py
│   │   │   ├── profile_weighting.py
│   │   │   └── synthesis_engine.py
│   │   │
│   │   ├── orchestration/
│   │   │   ├── orchestrator.py
│   │   │   └── state.py
│   │   │
│   │   ├── schemas/
│   │   │
│   │   ├── services/
│   │   │
│   │   └── main.py
│   │
│   ├── tests/
│   ├── requirements.txt
│   ├── Dockerfile
│   └── README.md
│
├── frontend/
│   ├── src/
│   ├── public/
│   ├── package.json
│   └── ...
│
└── README.md
```

---

# ⚡ Running the Project Locally

## 1. Clone the repository

```bash
git clone https://github.com/Shravan2307/Multi-Agent-Autonomous-Financial-Intelligence-System.git
```

```bash
cd Multi-Agent-Autonomous-Financial-Intelligence-System
```

---

## 2. Backend Setup

```bash
cd backend
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the backend:

```bash
python -m uvicorn app.main:app --reload
```

Backend:

```text
http://127.0.0.1:8000
```

Swagger API documentation:

```text
http://127.0.0.1:8000/docs
```

---

# 💻 Frontend Setup

Open another terminal:

```bash
cd frontend
```

Install dependencies:

```bash
npm install
```

Run the frontend:

```bash
npm run dev
```

Open the URL displayed by Vite, usually:

```text
http://localhost:5173
```

---

# 🔐 Environment Variables

Create a `.env` file based on:

```text
.env.example
```

Never commit API keys or other secrets to GitHub.

Example:

```env
MARKET_DATA_API_KEY=
LLM_API_KEY=
VECTOR_DB_URL=
```

The exact variables depend on the configured data and AI providers.

---

# 🔌 API Example

The core intelligence endpoint is:

```text
POST /api/intelligence/analyze
```

Example request:

```json
{
  "symbol": "RELIANCE",
  "company_name": "Reliance Industries",
  "current_price": 1450,
  "price_change": 1.8,
  "revenue": 100000,
  "revenue_growth": 8.5,
  "earnings": 12000,
  "eps": 25.4,
  "debt": 50000,
  "cash": 30000,
  "volatility": 12.5,
  "recent_news": [
    "Company reports strong quarterly revenue growth",
    "Investors remain positive about future expansion"
  ],
  "filing_summary": "The company reported stable financial performance.",
  "market_context": "Indian equity market is moderately positive.",
  "user_profile": {
    "risk_tolerance": "CONSERVATIVE",
    "investment_horizon": "LONG_TERM",
    "volatility_tolerance": "LOW"
  }
}
```

The response contains structured agent analysis and the resulting financial intelligence.

---

# ⚠️ Disclaimer

This project is a **hackathon / research prototype** intended for demonstrating autonomous financial intelligence and multi-agent reasoning.

It does **not constitute financial advice**, investment advice, or a guarantee of future market performance.

Users should independently verify financial information and consult qualified financial professionals before making investment decisions.

---

# 🏆 Hackathon Objective

The project demonstrates how autonomous AI agents can collaborate to transform complex financial information into personalized, explainable intelligence for retail investors.

The core innovation is not simply predicting whether a stock will rise or fall.

It is the combination of:

```text
Live / Financial Data
        +
Regulatory Knowledge
        +
Specialized AI Agents
        +
Parallel Orchestration
        +
User Profiling
        +
Conflict Resolution
        +
Evidence
        +
Transparent Reasoning
        ↓
Personalized Financial Intelligence
```

---

# 👥 Team

Built collaboratively as a multi-engineer hackathon project.

### Engineering Responsibilities

* **AI & Multi-Agent Orchestration**

  * Agent architecture
  * Parallel execution
  * State management
  * Synthesis
  * Profile weighting
  * Conflict resolution

* **RAG & Financial Data Engineering**

  * Market data ingestion
  * Financial document ingestion
  * Vector search
  * Evidence retrieval
  * Source attribution
  * Data degradation handling

* **Backend / API Integration**

  * API contracts
  * Endpoint integration
  * Backend services
  * Persistence
  * WebSocket / telemetry integration

* **Frontend**

  * Investor dashboard
  * Agent analysis visualization
  * Reasoning trace
  * Evidence presentation
  * User interaction

---

# 📄 Project Status

**Status: Final Hackathon Prototype**

The system includes:

* ✅ Multi-agent architecture
* ✅ Concurrent agent execution
* ✅ Structured agent outputs
* ✅ User profiling
* ✅ Profile-based synthesis
* ✅ Conflict detection
* ✅ Graceful degradation
* ✅ Evidence handling
* ✅ API integration
* ✅ Frontend integration
* ✅ Automated testing
* ✅ Containerization / deployment preparation

---

## ⭐ Key Differentiator

> **One market. Multiple perspectives. One personalized intelligence layer.**

The system transforms independent financial reasoning into a transparent, profile-aware decision-support experience for retail investors.
