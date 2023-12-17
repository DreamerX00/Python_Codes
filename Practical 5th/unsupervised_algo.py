import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans, AgglomerativeClustering, DBSCAN
from sklearn.metrics import silhouette_score


iris = load_iris()
X = iris.data
y = iris.target


scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)


algorithms = {
    'K-Means': KMeans(n_clusters=3, random_state=42),
    'Hierarchical Agglomerative': AgglomerativeClustering(n_clusters=3),
    'DBSCAN': DBSCAN(eps=0.5, min_samples=5)
}


for name, algorithm in algorithms.items():
    
    if name == 'DBSCAN':
        labels = algorithm.fit_predict(X_scaled)
    else:
        labels = algorithm.fit_predict(X)

    
    silhouette = silhouette_score(X_scaled, labels)
    
    
    print(f'{name} Clustering:')
    print(f'Silhouette Score: {silhouette:.2f}\n')

    
    if name in ['K-Means', 'Hierarchical Agglomerative']:
        plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis', edgecolors='k')
        plt.title(f'{name} Clustering')
        plt.xlabel('Sepal Length (cm)')
        plt.ylabel('Sepal Width (cm)')
        plt.show()
