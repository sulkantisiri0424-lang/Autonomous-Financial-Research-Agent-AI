# Autonomous Financial Research Agent AI

## 📌 Project Overview

The Autonomous Financial Research Agent AI is an agentic AI-based financial research system that automatically researches a company, analyzes financial information, evaluates potential risks, and generates a final financial research report.

The system uses multiple specialized agents that work together to complete the financial research workflow.

---

## 🎯 Objectives

- Automate financial research
- Collect company financial information
- Analyze important financial indicators
- Identify potential financial risks
- Generate an automated research report
- Provide a simple web-based dashboard
- Demonstrate an autonomous multi-agent workflow

---

## 🤖 Agentic AI Workflow

The system contains four specialized agents:

### 1. Research Agent

Collects financial information such as:

- Company name
- Stock symbol
- Sector
- Industry
- Current price
- Market capitalization
- P/E ratio
- 52-week high
- 52-week low

### 2. Analysis Agent

Analyzes the collected financial information and evaluates:

- Company valuation
- P/E ratio
- Current market price
- Market capitalization

### 3. Risk Assessment Agent

Identifies potential financial risks based on available indicators.

It evaluates:

- High valuation risk
- Price variation
- Overall risk level

### 4. Report Agent

Combines the results from all agents and generates a final financial research report.

---

## 🔄 System Architecture

User
↓
Web Dashboard
↓
Research Agent
↓
Analysis Agent
↓
Risk Assessment Agent
↓
Report Agent
↓
Final Financial Research Report

---

## 🛠️ Technologies Used

- Python
- Flask
- yfinance
- HTML
- CSS
- JavaScript
- Pandas
- NumPy
- REST API

---

## 📁 Project Structure

```text
Autonomous-Financial-Research-Agent-AI/
│
├── app.py
├── requirements.txt
├── .gitignore
├── README.md
│
├── agents/
│   ├── __init__.py
│   ├── research_agent.py
│   ├── analysis_agent.py
│   ├── risk_agent.py
│   └── report_agent.py
│
├── data/
│   └── sample_data.csv
│
├── templates/
│   └── index.html
│
└── static/
    ├── style.css
    └── script.js
