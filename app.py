import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv(r"dataset path (Indian_Climate_Dataset_2024_2025.csv)")
df.columns = df.columns.str.strip()
print(df.columns)
# ----------------------------
# 1. BASIC CHECK
# ----------------------------
print(df.head())
print(df.info())

# ----------------------------
# 2. HANDLE MISSING VALUES
# ----------------------------
print("\nMissing values:\n", df.isnull().sum())

df.fillna(method='ffill', inplace=True)

# ----------------------------
# 3. DESCRIPTIVE STATS
# ----------------------------
print("\nStatistics:\n")
print(df.describe())

# ----------------------------
# 4. CORRELATION HEATMAP
# ----------------------------
plt.figure(figsize=(10,6))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm')
plt.title("Correlation Between Weather Variables")
plt.show()

# ----------------------------
# 5. VISUALIZATIONS
# ----------------------------

# Temperature comparison
plt.figure(figsize=(8,5))
plt.plot(df['City'], df['Temperature_Max'], label='Max Temp')
plt.plot(df['City'], df['Temperature_Min'], label='Min Temp')
plt.plot(df['City'], df['Temperature_Avg'], label='Avg Temp')
plt.xticks(rotation=45)
plt.title("Temperature Comparison Across Cities")
plt.legend()
plt.show()

# Rainfall comparison
plt.figure(figsize=(8,5))
sns.barplot(x='City', y='Rainfall', data=df)
plt.xticks(rotation=45)
plt.title("Rainfall Across Cities")
plt.show()

# Humidity vs Rainfall
plt.figure(figsize=(8,5))
sns.scatterplot(x='Humidity', y='Rainfall', data=df)
plt.title("Humidity vs Rainfall")
plt.show()

# AQI distribution
plt.figure(figsize=(8,5))
sns.histplot(df['AQI'], bins=10, kde=True)
plt.title("AQI Distribution")
plt.show()

# Wind Speed vs Temperature
plt.figure(figsize=(8,5))
sns.scatterplot(x='Wind_Speed', y='Temperature_Avg', data=df)
plt.title("Wind Speed vs Average Temperature")
plt.show()

# Pressure vs Cloud Cover
plt.figure(figsize=(8,5))
sns.scatterplot(x='Pressure', y='Cloud_Cover', data=df)
plt.title("Pressure vs Cloud Cover")
plt.show()
