# Credit Risk Analysis – Loan Default Prediction Pipeline

## 📊 Project Overview

This project is an end-to-end credit risk analytics pipeline built using a large-scale LendingClub loan dataset. The goal is to simulate a real-world banking analytics workflow by identifying key drivers of loan default and preparing data for risk analysis.

The project covers the full data lifecycle:
- Data ingestion and exploration
- Data cleaning and feature selection
- Feature engineering (credit risk target creation)
- Data storage in PostgreSQL
- SQL-based exploratory risk analysis

---

## 🎯 Business Problem

Financial institutions need to assess borrower creditworthiness and predict the likelihood of loan default. Understanding default risk helps banks:
- Reduce financial losses
- Improve lending decisions
- Optimize credit policies
- Segment borrowers by risk level

This project focuses on building a structured dataset to support credit risk analysis and decision-making.

---

## 📁 Dataset

- **Source:** LendingClub Loan Dataset  
- **Size:** ~2.2 million records  
- **Initial Features:** 145 columns  
- **Final Features Used:** 11 core variables  

The dataset contains historical loan performance data, borrower profiles, and repayment outcomes.

---

## 🛠️ Tools & Technologies

- Python (Pandas)
- PostgreSQL
- pgAdmin
- SQL
- VS Code

---

## ⚙️ Project Workflow

The project follows a structured data pipeline:
Raw LendingClub Dataset (CSV)
↓
Python Data Ingestion (Pandas)
↓
Schema Exploration & Data Understanding
↓
Feature Selection (145 → 11 columns)
↓
Target Variable Engineering (default_flag)
↓
Clean Dataset Export (CSV)
↓
PostgreSQL Database Load
↓
SQL-Based Credit Risk Analysis


---

## 🧹 Data Cleaning & Preparation

Key preprocessing steps:
- Inspected dataset schema and identified relevant variables
- Reduced dimensionality from 145 to 11 key features
- Handled inconsistent and irrelevant columns
- Ensured dataset was analysis-ready for SQL operations

---

## 🧠 Feature Engineering

A binary target variable was created to define credit risk:

- `default_flag = 1` → Loan is "Charged Off" or "Default"
- `default_flag = 0` → All other loan statuses

This transformation enables supervised credit risk analysis.

---

## 📊 Key Insights (Initial Analysis)

- Overall default rate: ~11.6%
- Dataset shows class imbalance (typical in credit risk modeling)
- Majority of borrowers are non-default (low-risk category)
- Suitable for risk segmentation and predictive modeling

---

## 🗄️ PostgreSQL Integration

The cleaned dataset was loaded into PostgreSQL to enable structured querying and scalable analysis.

This allows for:
- Aggregated risk reporting
- Segment-based analysis
- Portfolio-level insights

---

## 📈 Example SQL Analyses

Planned/implemented analyses include:

- Default rate by loan grade
- Income level vs default risk
- Debt-to-income ratio risk segmentation
- Borrower profile risk categorization

---

## 🚀 How to Run This Project

1. Run Python preprocessing script:
python 01_clean_data.py

2. Load `clean_loans.csv` into PostgreSQL using pgAdmin:
- Create table schema
- Import CSV with header enabled

3. Run SQL queries in pgAdmin for analysis

---

## 📌 Key Learning Outcomes

- Built an end-to-end data pipeline for credit risk analysis
- Applied feature selection and data cleaning at scale
- Engineered a binary classification target variable
- Integrated Python preprocessing with SQL-based analysis
- Gained experience working with large financial datasets

---

## 🧾 Future Improvements

- Add Tableau/Power BI dashboards for visualization
- Build predictive machine learning model (logistic regression / XGBoost)
- Automate ETL pipeline
- Improve data type optimization and performance tuning in PostgreSQL

---

## 📎 Author

Data Analyst Project Portfolio – Credit Risk Analysis