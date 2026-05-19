import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# =========================
# LOAD DATASET
# =========================

df = pd.read_csv(r"C:\Users\Asus\Downloads\interview_dirty_dataset(2).csv")

# =========================
# BASIC INFORMATION
# =========================

print(df.head(10))
print(df.info())
print(df.shape)
print(df.describe())
print(df.isnull().sum())
print(df.duplicated().sum())

# =========================
# DATA VISUALIZATION
# =========================

# Boxplot for Salary
df.boxplot(column="Salary")
plt.show()

# Histogram for Salary Distribution
sns.histplot(df["Salary"], bins=10, kde=True)
plt.show()

# =========================
# HANDLE MISSING VALUES
# =========================

df["Employee_ID"] = df["Employee_ID"].fillna(df["Employee_ID"].mode()[0])

df["Department"] = df["Department"].fillna("Unknown")

df["Salary"] = df["Salary"].fillna(df["Salary"].mean())

df["Name"] = df["Name"].fillna("Unknown")

df["Age"] = pd.to_numeric(df["Age"], errors="coerce")
df["Age"] = df["Age"].fillna(df["Age"].median())

df["Joining_Date"] = df["Joining_Date"].fillna("Not Mentioned")

df["Email"] = df["Email"].fillna("Not Given")

df["Performance_Score"] = pd.to_numeric(df["Performance_Score"], errors="coerce")
df["Performance_Score"] = df["Performance_Score"].fillna(
    df["Performance_Score"].mean()
)

print(df.isnull().sum())

# =========================
# REMOVE DUPLICATES
# =========================

df = df.drop_duplicates()

df.reset_index(drop=True, inplace=True)

print(df.shape)

# =========================
# EXPORT CLEANED DATASET
# =========================

df.to_csv(
    r"C:\Users\Asus\Downloads\cleaned_dataset.csv",
    index=False
)

print("Dataset cleaned successfully!")