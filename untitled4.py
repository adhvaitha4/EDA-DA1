# -*- coding: utf-8 -*-


import pandas as pd
df=pd.read_csv('/content/stolenvehicles.csv')
df

df.describe()

df.head()

df.info()

mean=df.mean()
mean

median=df.median()
median

mode=df.mode()
mode

df.isnull().sum()

df['Color'].fillna(df['Color'].mode()[0], inplace=True)
df['VehicleModel'].fillna(df['VehicleModel'].mode()[0], inplace=True)
df['VehicleDesc'].fillna(df['VehicleDesc'].mode()[0], inplace=True)
df['ModelYear'].fillna(df['ModelYear'].median(), inplace=True)
df['VehicleType'].fillna(df['VehicleType'].mode()[0], inplace=True)
df['DateStolen'].fillna(method='ffill', inplace=True)
df['Location'].fillna(df['Location'].mode()[0], inplace=True)
df.isnull().sum()

import matplotlib.pyplot as plt
import seaborn as sns
# Plotting the distribution of vehicle colors
plt.figure(figsize=(10, 6))
sns.countplot(df['Color'])
plt.title('Distribution of Vehicle Colors')
plt.xlabel('Color')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.show()

# Histogram for Model Year
plt.figure(figsize=(10, 6))
plt.hist(df['ModelYear'], bins=20, color='skyblue', edgecolor='black')
plt.title('Histogram of Model Year')
plt.xlabel('Model Year')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()

# Boxplot for Model Year
plt.figure(figsize=(10, 6))
sns.boxplot(df['ModelYear'], color='lightgreen')
plt.title('Boxplot of Model Year')
plt.xlabel('Model Year')
plt.grid(True)
plt.show()

# Bar graph for Vehicle Types
plt.figure(figsize=(10, 6))
vehicle_type_counts = df['VehicleType'].value_counts()
vehicle_type_counts.plot(kind='bar', color='orange')
plt.title('Bar Graph of Vehicle Types')
plt.xlabel('Vehicle Type')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.show()

#clustering and ouliers
#kmean and dbscan method
# Select numerical features for clustering
numerical_data = df[['ModelYear']]
numerical_data

# Standardize the numerical features

import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

scaler = StandardScaler()
scaler
scaled_data = scaler.fit_transform(numerical_data)
scaled_data

# Applying PCA for dimensionality reduction
# Applying PCA for dimensionality reduction
pca = PCA(n_components=1)
principal_components = pca.fit_transform(scaled_data)
principal_components

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans, DBSCAN
from sklearn.preprocessing import StandardScaler

# Fill null values in the 'ModelYear' column with the median year
median_model_year = df['ModelYear'].median()
df['ModelYear'].fillna(median_model_year, inplace=True)

# Select numerical features for clustering
numerical_features = df[['ModelYear']]

# Standardize the numerical features
scaler = StandardScaler()
numerical_features_scaled = scaler.fit_transform(numerical_features)

# K-means clustering
kmeans = KMeans(n_clusters=3, random_state=42)
kmeans_labels = kmeans.fit_predict(numerical_features_scaled)

# DBSCAN clustering
dbscan = DBSCAN(eps=0.5, min_samples=5)
dbscan_labels = dbscan.fit_predict(numerical_features_scaled)

# Add cluster labels to the DataFrame
df['KMeansCluster'] = kmeans_labels
df['DBSCANCluster'] = dbscan_labels

# Visualize K-means clusters
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='ModelYear', y='VehicleType', hue='KMeansCluster', palette='viridis', legend='full')
plt.title('K-means Clustering')
plt.xlabel('Model Year')
plt.ylabel('Vehicle Type')
plt.legend(title='Cluster')
plt.show()

# Visualize DBSCAN clusters
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='ModelYear', y='VehicleType', hue='DBSCANCluster', palette='viridis', legend='full')
plt.title('DBSCAN Clustering')
plt.xlabel('Model Year')
plt.ylabel('Vehicle Type')
plt.legend(title='Cluster')
plt.show()

import numpy as np

covariance = np.cov(df.select_dtypes(include=np.number), rowvar=False)
covariance

#calculate corerelation matrix
correlation_matrix = df.corr()
correlation_matrix

import seaborn as sns
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f", square=True)
plt.title("Correlation Matrix")
plt.show()
threshold = 0.5
high_correlation_features = correlation_matrix[(correlation_matrix > threshold) & (correlation_matrix < 1.0)].stack().index.tolist()

print("Highly correlated features:")
for feature_pair in high_correlation_features:
    print(f"{feature_pair[0]} - {feature_pair[1]}: {correlation_matrix.loc[feature_pair]}")

import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import LocalOutlierFactor


# Drop rows with missing values
data.dropna(inplace=True)

# Drop non-numeric columns for LOF analysis
numeric_data = data.drop(['Color', 'VehicleModel', 'VehicleDesc', 'Location', 'DateStolen'], axis=1)

# Encode categorical variables
label_encoder = LabelEncoder()
for column in ['VehicleType']:
    numeric_data[column] = label_encoder.fit_transform(numeric_data[column])

# Initialize the LOF model
lof_model = LocalOutlierFactor(n_neighbors=20, contamination=0.1)

# Fit the model and predict outliers
outlier_labels = lof_model.fit_predict(numeric_data)

# Identify outliers (outlier_label=-1)
outliers = data[outlier_labels == -1]

# Display outliers
print("Outliers:")
print(outliers)
