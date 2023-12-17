import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans, AgglomerativeClustering
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score

iris_data = pd.read_csv('iris_dataset.csv')  
X = iris_data.iloc[:, 1:4].values
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

def apply_clustering(X, n_clusters):
    
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    kmeans_labels = kmeans.fit_predict(X)

    
    hierarchical = AgglomerativeClustering(n_clusters=n_clusters)
    hierarchical_labels = hierarchical.fit_predict(X)

    return kmeans_labels, hierarchical_labels

def plot_clusters(X, labels, title):
    if X.shape[1] == 1:
        plt.scatter(X[:, 0], np.zeros_like(X[:, 0]), c=labels, cmap='viridis')
    elif X.shape[1] == 2:
        plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis')
    else:
        raise ValueError("Unsupported number of features for plotting.")

    plt.title(title)
    plt.xlabel('Feature 1')
    plt.ylabel('Feature 2')
    plt.show()

def evaluate_clustering_quality(X, labels):
    silhouette_avg = silhouette_score(X, labels)
    print(f'Silhouette Score: {silhouette_avg}')


for n_clusters in range(2, 6):
    kmeans_labels, hierarchical_labels = apply_clustering(X_scaled, n_clusters)
    plot_clusters(X_scaled, kmeans_labels, f'k-Means Clustering (k={n_clusters})')
    plot_clusters(X_scaled, hierarchical_labels, f'Hierarchical Clustering (k={n_clusters})')

    print(f'\nResults for {n_clusters} clusters:')
    print('k-Means Clustering:')
    evaluate_clustering_quality(X_scaled, kmeans_labels)

    print('Hierarchical Clustering:')
    evaluate_clustering_quality(X_scaled, hierarchical_labels)

    print('\n------------------------------------\n')
