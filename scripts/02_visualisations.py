import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# ---------- PATHS ----------
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
file_path = os.path.join(BASE_DIR, "data", "clean_loan.csv")

OUTPUT_DIR = os.path.join(BASE_DIR, "output")
CHART_DIR = os.path.join(OUTPUT_DIR, "charts")
os.makedirs(OUTPUT_DIR, exist_ok=True)
os.makedirs(CHART_DIR, exist_ok=True)

df = pd.read_csv(file_path)

print(df.head())

def save_chart(name):
    path = os.path.join(CHART_DIR, f"{name}.png")
    plt.savefig(path, bbox_inches="tight", dpi=300)

# ---------- 1. GRADE ----------
grade_risk = df.groupby("grade")["default_flag"].mean().reset_index()
grade_risk = grade_risk.sort_values("grade")

plt.figure()
sns.barplot(data=grade_risk, x="grade", y="default_flag")
plt.title("Default Rate by Credit Grade")
plt.xlabel("Credit Grade")
plt.ylabel("Default Rate (%)")
plt.gca().yaxis.set_major_formatter(lambda x, _: f"{x:.0%}")

save_chart("grade_chart")
plt.show()
plt.close()


# ---------- 2. INCOME ----------
df["income_band"] = pd.cut(
    df["annual_inc"],
    bins=[0, 50000, 100000, 150000, 200000, 1000000],
    labels=["0-50k", "50k-100k", "100k-150k", "150k-200k", "200k+"]
)

income_risk = df.groupby("income_band")["default_flag"].mean().reset_index()

plt.figure()

sns.barplot(data=income_risk, x="income_band", y="default_flag")
plt.title("Default Rate by Income Band")
plt.xlabel("Income Band")
plt.ylabel("Default Rate (%)")

plt.gca().yaxis.set_major_formatter(lambda x, _: f"{x:.0%}")

save_chart("income_chart")
plt.show()
plt.close()

# ---------- 3. DTI ----------
df["dti_band"] = pd.cut(
    df["dti"],
    bins=[0, 10, 20, 30, 40, 100],
    labels=["0-10", "10-20", "20-30", "30-40", "40+"]
)

dti_risk = df.groupby("dti_band")["default_flag"].mean().reset_index()

plt.figure()
sns.barplot(data=dti_risk, x="dti_band", y="default_flag")
plt.title("Default Rate by DTI")
plt.xlabel("DTI Band")
plt.ylabel("Default Rate (%)")

plt.gca().yaxis.set_major_formatter(lambda x, _: f"{x:.0%}")

save_chart("dti_chart")
plt.show()
plt.close()

# ---------- 4. PURPOSE ----------
purpose_risk = df.groupby("purpose")["default_flag"].mean().reset_index()
purpose_risk = purpose_risk.sort_values("default_flag", ascending=False).head(10)

plt.figure()
sns.barplot(data=purpose_risk, y="purpose", x="default_flag")
plt.title("Default Rate by Loan Purpose")
plt.xlabel("Default Rate (%)")
plt.ylabel("Loan Purpose")
plt.gca().xaxis.set_major_formatter(lambda x, _: f"{x:.0%}")

save_chart("purpose_chart")
plt.show()
plt.close()

summary_path = os.path.join(OUTPUT_DIR, "report.txt")

with open(summary_path, "w") as f:
    f.write("CREDIT RISK ANALYSIS REPORT\n")
    f.write("===========================\n\n")

    f.write("1. Default Rate by Grade shows increasing risk as credit grade worsens.\n")
    f.write("2. Higher income bands generally show lower default risk.\n")
    f.write("3. Higher DTI bands are strongly associated with increased default risk.\n")
    f.write("4. Loan purpose varies significantly in risk profile.\n")
