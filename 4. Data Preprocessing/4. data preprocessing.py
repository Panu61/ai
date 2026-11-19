
# --------------------------------------------------
# 1. Import Required Libraries
# --------------------------------------------------

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import statistics as s

from sklearn.model_selection import train_test_split

# --------------------------------------------------
# 2. Set Visualization Styles
# --------------------------------------------------

sns.set_style("whitegrid")
plt.style.use("fivethirtyeight")

# --------------------------------------------------
# 3. Load Dataset
# --------------------------------------------------

file_path = r"E:\aiml\4. Data Preprocessing\heart.csv"

df = pd.read_csv(file_path)

print("\nFirst Five Records:")
print(df.head())

# --------------------------------------------------
# 4. Information of Dataset
# --------------------------------------------------

print("\nDataset Information:")
df.info()

print("\nColumn Names:")
print(df.columns)

print("\nData Types:")
print(df.dtypes)

print("\nData Type Count:")
print(df.dtypes.value_counts())

print("\nStatistical Description:")
print(df.describe())

print("\nFirst Five Rows:")
print(df.head())

# --------------------------------------------------
# 5. Missing Values
# --------------------------------------------------

print("\nMissing Values:")
print(df.isnull().sum())

# Select numeric columns
numeric_columns = df.select_dtypes(include=np.number).columns

# Fill missing numeric values with median
for column in numeric_columns:
    df[column] = df[column].fillna(df[column].median())

# Fill missing categorical values with mode
categorical_columns = df.select_dtypes(
    include=["object", "category"]
).columns

for column in categorical_columns:
    if df[column].notna().any():
        df[column] = df[column].fillna(df[column].mode()[0])

print("\nMissing Values After Handling:")
print(df.isnull().sum())

# --------------------------------------------------
# 6. Remove Duplicate Records
# --------------------------------------------------

df = df.drop_duplicates()

print("\nShape After Removing Duplicates:")
print(df.shape)

# --------------------------------------------------
# 7. Dataset Size and Shape
# --------------------------------------------------

size = df.size
print("\nSize of Dataset:", size)

shape = df.shape
print("\nShape of Dataset:", shape)

# --------------------------------------------------
# 8. Statistical Analysis
# --------------------------------------------------

print("\nStatistical Summary:")
print(df.describe())

print("\nMean:")
print(df.mean(numeric_only=True))

print("\nMedian:")
print(df.median(numeric_only=True))

print("\nStandard Deviation:")
print(df.std(numeric_only=True))

print("\nCorrelation Matrix:")
print(df.corr(numeric_only=True))

# --------------------------------------------------
# 9. Data Visualization
# --------------------------------------------------

# Histogram of Age
if "age" in df.columns:
    plt.figure(figsize=(8, 5))
    plt.hist(df["age"].dropna(), bins=20, edgecolor="black")
    plt.title("Histogram of Age")
    plt.xlabel("Age")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.show()

# Histogram of Cholesterol
if "chol" in df.columns:
    plt.figure(figsize=(8, 5))
    plt.hist(df["chol"].dropna(), bins=15, edgecolor="black")
    plt.title("Histogram of Cholesterol")
    plt.xlabel("Cholesterol")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.show()

# Boxplot of Age
if "age" in df.columns:
    plt.figure(figsize=(8, 5))
    sns.boxplot(x=df["age"])
    plt.title("Boxplot of Age")
    plt.tight_layout()
    plt.show()

# Boxplot of Cholesterol
if "chol" in df.columns:
    plt.figure(figsize=(8, 5))
    sns.boxplot(x=df["chol"])
    plt.title("Boxplot of Cholesterol")
    plt.tight_layout()
    plt.show()

# --------------------------------------------------
# 10. Finding Mean Age of Patients
# --------------------------------------------------

if "age" in df.columns:
    average = df["age"].mean()
    print("\nAverage Age of Patients:", average)

# --------------------------------------------------
# 11. Extracting Particular Columns
# --------------------------------------------------

print("\nParticular Columns:")

for column in ["age", "sex", "trestbps", "chol"]:
    if column in df.columns:
        print("\n", column)
        print(df[column])

# --------------------------------------------------
# 12. Split Data into Training and Testing
# --------------------------------------------------

if "target" not in df.columns:
    raise ValueError("Target column is missing from the dataset.")

X = df.drop("target", axis=1)
y = df["target"]

print("\nFeature Data Shape:")
print(X.shape)

print("\nTarget Data Shape:")
print(y.shape)

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=56
)

print("\nTraining Data:")
print(X_train)

print("\nTraining Data Shape:")
print(X_train.shape)

print("\nTesting Data Shape:")
print(X_test.shape)

print("\nTraining Target Shape:")
print(y_train.shape)

print("\nTesting Target Shape:")
print(y_test.shape)

# --------------------------------------------------
# 13. Final Output
# --------------------------------------------------

print("\nData Preprocessing Completed Successfully!")
