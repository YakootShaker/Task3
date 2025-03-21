# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1C5KPiV31VEhPUJcNqWLovXumPgV_cdoX
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = "heart_data.csv"
data = pd.read_csv(file_path)

# Display dataset info
print("First 5 rows of the dataset:")
print(data.head())

print("\nDataset Info:")
print(data.info())

print("\nDescriptive Statistics:")
print(data.describe())

# Check for missing values and handle with mean imputation
print("\nMissing values before imputation:")
print(data.isnull().sum())

data.fillna(data.mean(numeric_only=True), inplace=True)

print("\nMissing values after imputation:")
print(data.isnull().sum())

# Remove outliers using the IQR method for cholesterol
Q1 = data["chol"].quantile(0.25)
Q3 = data["chol"].quantile(0.75)
IQR = Q3 - Q1
data = data[~((data["chol"] < (Q1 - 1.5 * IQR)) | (data["chol"] > (Q3 + 1.5 * IQR)))]

print("\nNumber of rows after removing outliers:", data.shape[0])

# Compute basic statistics for cholesterol
chol_mean = np.mean(data["chol"])
chol_median = np.median(data["chol"])
chol_std = np.std(data["chol"])

print("\nCholesterol Statistics:")
print(f"Mean: {chol_mean:.2f}, Median: {chol_median:.2f}, Standard Deviation: {chol_std:.2f}")

# Calculate mean blood pressure for healthy and diseased patients
mean_bp_healthy = data[data["target"] == 0]["trestbps"].mean()
mean_bp_disease = data[data["target"] == 1]["trestbps"].mean()

print(f"\nMean Blood Pressure (Healthy): {mean_bp_healthy:.2f}")
print(f"Mean Blood Pressure (Heart Disease): {mean_bp_disease:.2f}")

# Find min and max heart rate
max_hr = data["thalach"].max()
min_hr = data["thalach"].min()

print(f"\nMax Heart Rate: {max_hr}, Min Heart Rate: {min_hr}")

# Find patients with cholesterol greater than 300 mg/dL
high_chol_patients = data[data["chol"] > 300]
print("\nNumber of patients with cholesterol > 300:", high_chol_patients.shape[0])

# Find patients older than 60 with abnormal ECG
abnormal_ecg = data[(data["age"] > 60) & (data["restecg"] > 0)]
print("\nNumber of patients over 60 with abnormal ECG:", abnormal_ecg.shape[0])

# Data Visualization
plt.figure(figsize=(12, 6))
sns.histplot(data["chol"], bins=30, kde=True, color='blue')
plt.title("Histogram of Cholesterol Levels")
plt.xlabel("Cholesterol Level")
plt.ylabel("Frequency")
plt.show()

plt.figure(figsize=(10, 6))
sns.scatterplot(x=data["age"], y=data["thalach"], hue=data["target"], palette="coolwarm")
plt.title("Age vs. Maximum Heart Rate")
plt.xlabel("Age")
plt.ylabel("Max Heart Rate")
plt.show()

plt.figure(figsize=(8, 5))
sns.countplot(x=data["target"], palette="pastel")
plt.title("Number of Patients by Heart Disease Status")
plt.xlabel("Patient Status")
plt.ylabel("Count")
plt.xticks(ticks=[0, 1], labels=["Healthy", "Diseased"])
plt.show()

from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(data["chol"], data["age"], data["target"], c=data["target"], cmap="coolwarm")
ax.set_xlabel("Cholesterol")
ax.set_ylabel("Age")
ax.set_zlabel("Heart Disease")
ax.set_title("3D Plot: Cholesterol, Age, and Heart Disease")
plt.show()

plt.figure(figsize=(7, 7))
cp_counts = data["cp"].value_counts()
plt.pie(cp_counts, labels=cp_counts.index, autopct='%1.1f%%', colors=['red', 'blue', 'green', 'yellow'])
plt.title("Distribution of Chest Pain Types among Patients")
plt.show()