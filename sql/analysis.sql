-- ============================================
-- CREDIT RISK ANALYSIS - SQL QUERIES
-- ============================================

-- 1. Overall Portfolio Default Rate
SELECT
    COUNT(*) AS total_loans,
    SUM(default_flag) AS total_defaults,
    ROUND(AVG(default_flag::numeric), 4) AS default_rate
FROM loans_clean;


-- ============================================
-- 2. Default Rate by Credit Grade
-- ============================================
SELECT
    grade,
    COUNT(*) AS total_loans,
    SUM(default_flag) AS total_defaults,
    ROUND(AVG(default_flag::numeric), 4) AS default_rate
FROM loans_clean
GROUP BY grade
ORDER BY grade;


-- ============================================
-- 3. Income Segmentation Analysis
-- ============================================
SELECT
    CASE
        WHEN annual_inc < 50000 THEN 'Low Income'
        WHEN annual_inc BETWEEN 50000 AND 100000 THEN 'Medium Income'
        ELSE 'High Income'
    END AS income_band,
    COUNT(*) AS total_loans,
    ROUND(AVG(default_flag::numeric), 4) AS default_rate
FROM loans_clean
GROUP BY income_band
ORDER BY default_rate DESC;


-- ============================================
-- 4. Debt-to-Income (DTI) Risk Analysis
-- ============================================
SELECT
    CASE
        WHEN dti < 10 THEN 'Low DTI'
        WHEN dti BETWEEN 10 AND 20 THEN 'Medium DTI'
        ELSE 'High DTI'
    END AS dti_band,
    COUNT(*) AS total_loans,
    ROUND(AVG(default_flag::numeric), 4) AS default_rate
FROM loans_clean
GROUP BY dti_band
ORDER BY default_rate DESC;


-- ============================================
-- 5. Loan Purpose Risk Analysis
-- ============================================
SELECT
    purpose,
    COUNT(*) AS total_loans,
    ROUND(AVG(default_flag::numeric), 4) AS default_rate
FROM loans_clean
GROUP BY purpose
ORDER BY default_rate DESC
LIMIT 10;