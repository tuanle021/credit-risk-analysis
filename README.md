# Credit Risk Analysis – Loan Default Prediction Pipeline

## 📊 Project Overview

This project is an end-to-end credit risk analytics pipeline built using a large-scale LendingClub dataset. It simulates a real-world banking workflow by transforming raw loan data into an analysis-ready dataset and identifying key drivers of loan default risk.

---

## 🧠 Executive Summary

This project analyses a large-scale loan dataset to identify key drivers of credit risk and loan default. Using SQL and Excel, the analysis reveals that default rates increase significantly with lower credit grades, higher debt-to-income ratios, and lower income levels. 

The findings highlight that borrower financial health and loan characteristics are strong indicators of default risk. In particular, high DTI borrowers and certain loan purposes (e.g., small business loans) represent higher-risk segments.

An Excel-based dashboard was developed to present these insights in a clear, business-friendly format, enabling easy identification of risk patterns within the loan portfolio.

---

## 🎯 Business Problem

Financial institutions need to assess borrower creditworthiness and understand the factors that contribute to loan defaults. These insights help improve lending decisions, reduce financial losses, and optimise credit risk strategies.

---

## 📁 Dataset

- **Source:** LendingClub Loan Dataset  
- **Size:** ~2.2 million records  
- **Initial Features:** 145 columns  
- **Final Features Used:** 11 key variables  

---

## 🛠️ Tools & Technologies

- Python (Pandas)
- PostgreSQL
- SQL
- pgAdmin
- Microsoft Excel
- VS Code

---

## ⚙️ Project Workflow

Raw LendingClub Dataset (CSV)
↓
Python Data Processing (Pandas)
↓
Schema Exploration & Validation
↓
Feature Selection (145 → 11 columns)
↓
Target Engineering (default_flag)
↓
Clean Dataset Export
↓
PostgreSQL Data Load
↓
SQL-Based Analysis
↓
Excel Visualisation & Dashboard

---

## 🧹 Data Preparation & Feature Engineering

- Selected key variables relevant to credit risk analysis
- Reduced dataset dimensionality from 145 to 11 columns
- Created a binary target variable (`default_flag`) to identify loan defaults:
  - 1 → Charged Off / Default  
  - 0 → Non-default  
- Prepared dataset for structured analysis in PostgreSQL

---

## 📊 Key Insights

- The overall loan default rate is approximately **11.6%**, indicating a moderately risky loan portfolio with a typical class imbalance between defaulting and non-defaulting borrowers.

- **Credit grade is a strong predictor of default risk**, with default rates increasing consistently from Grade A (lowest risk) to Grade G (highest risk).

- **Income level is inversely related to default risk**, with lower income borrowers showing higher likelihood of default.

- **Debt-to-income (DTI) ratio is a key risk driver**, where higher DTI levels correspond to increased default rates.

- **Loan purpose impacts default behaviour**, with certain categories such as small business and personal loans showing higher risk.

- Overall, borrower financial health and credit grading are critical factors in predicting loan performance.

---

## 📊 Dashboard

An Excel-based dashboard was created to visualise key credit risk metrics, including default rates by credit grade, income level, debt-to-income ratio, and loan purpose.  

The dashboard provides a clear, business-friendly view of the loan portfolio and highlights high-risk borrower segments.

---

## 📁 SQL Analysis

All SQL queries used for analysis can be found in the `sql/analysis.sql` file.

---

## 🚀 How to Run This Project

1. Run the Python preprocessing script: python scripts/01_clean_data.py

2. Load the cleaned dataset (`clean_loans.csv`) into PostgreSQL using pgAdmin

3. Execute queries from `sql/analysis.sql` to reproduce analysis

---

## 🧾 Future Improvements

- Build interactive dashboards (Excel slicers / Power BI)
- Develop predictive models (logistic regression, XGBoost)
- Automate the ETL pipeline
- Optimise database performance for large-scale queries

---