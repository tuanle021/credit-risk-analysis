import pandas as pd

# load raw dataset 
df = pd.read_csv(r"C:\Users\le654\OneDrive\Documents\workspace\credit-risk-analysis\data\loan.csv")

print(df.columns.tolist())

print("Original shape:", df.shape)

existing_cols = df.columns

# Select only relevant columns
columns_needed = [
    'loan_amnt',
    'term',
    'int_rate',
    'grade',
    'emp_length',
    'annual_inc',
    'dti',
    'fico_range_low',
    'fico_range_high',
    'purpose',
    'issue_d',
    'loan_status'
]

columns_available = [col for col in columns_needed if col in existing_cols]
df = df[columns_available]

# Clean interest rate
df['int_rate'] = df['int_rate'].astype(str).str.replace('%','')
df['int_rate'] = pd.to_numeric(df['int_rate'], errors='coerce')

# Create default flag (target variable for credit risk modeling)

df['default_flag'] = df['loan_status'].isin(['Charged Off', 'Default']).astype(int)

# check distribution
print("\nDefault distribution:")
print(df['default_flag'].value_counts(normalize=True))

# Save cleaned dataset
df.to_csv(r"C:\Users\le654\OneDrive\Documents\workspace\credit-risk-analysis\data\clean_loan.csv", index=False)

print("Clean dataset saved successfully")
print("Final shape:", df.shape)


