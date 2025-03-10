# -*- coding: utf-8 -*-
"""Assignment_23113022.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1JI1fAwYdF6-Q5BpvqEKffuqmzohAwIwS
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv("coffee_shop_revenue.csv")  # Update with actual file name

# Display the first few rows
print(df.head())

# Check for missing values
print(df.isnull().sum())

# Summary statistics for numerical columns
print(df.describe())

# Univariate Analysis
numerical_vars = df.select_dtypes(include=['number']).columns
for var in numerical_vars:
    plt.figure(figsize=(8, 4))
    sns.histplot(df[var].dropna(), kde=True)
    plt.title(f'Distribution of {var}')
    plt.xlabel(var)
    plt.ylabel('Frequency')
    plt.show()

categorical_vars = df.select_dtypes(include=['object']).columns
for var in categorical_vars:
    plt.figure(figsize=(8, 4))
    sns.countplot(data=df, x=var)
    plt.title(f'Count of {var}')
    plt.xlabel(var)
    plt.ylabel('Count')
    plt.xticks(rotation=45)
    plt.show()

# Multivariate Analysis
sns.pairplot(df, diag_kind='kde')
plt.show()

# Heatmap of correlation between numerical variables
plt.figure(figsize=(10, 6))
corr_matrix = df.corr()
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
plt.title('Correlation Matrix')
plt.show()