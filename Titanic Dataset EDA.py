# Import necessary libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
titanic_data = pd.read_csv("titanic.csv")

# Check the first few rows of the dataset
print(titanic_data.head())

# Show the basic information about the dataset
titanic_data.info()

# Check for any missing values
print(titanic_data.isnull().sum())

# Fill missing values in the 'Age' column with the median age
titanic_data['Age'].fillna(titanic_data['Age'].median(), inplace=True)

# Drop the 'Cabin' column because many values are missing
titanic_data.drop('Cabin', axis=1, inplace=True)

# Drop rows where 'Embarked' is missing
titanic_data.dropna(subset=['Embarked'], inplace=True)

# Show basic statistics for numerical columns
print(titanic_data.describe())

# Countplot to visualize survival based on gender
plt.figure(figsize=(8, 5))
sns.countplot(x='Survived', hue='Sex', data=titanic_data)
plt.title('Survival Rate by Gender')
plt.show()

# Histogram to visualize the distribution of ages
plt.figure(figsize=(10, 6))
sns.histplot(titanic_data['Age'], bins=20, kde=True)
plt.title('Age Distribution of Passengers')
plt.show()

# Countplot for survival based on Passenger class (Pclass)
plt.figure(figsize=(8, 5))
sns.countplot(x='Pclass', hue='Survived', data=titanic_data)
plt.title('Survival Rate by Passenger Class')
plt.show()

# Select only numeric columns for correlation matrix
numeric_columns = titanic_data.select_dtypes(include=[np.number])

# Generate the heatmap with only numeric data
plt.figure(figsize=(8, 6))
sns.heatmap(numeric_columns.corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Between Numerical Features')
plt.show()
