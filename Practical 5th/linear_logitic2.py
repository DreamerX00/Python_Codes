import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import make_classification
import matplotlib.pyplot as plt


X, y = make_classification(n_samples=100, n_features=1, n_informative=1, n_redundant=0, n_clusters_per_class=1, random_state=42)


model = LogisticRegression()
model.fit(X, y)


X_new = np.linspace(-3, 3, 300).reshape(-1, 1)
y_proba = model.predict_proba(X_new)


plt.scatter(X, y, alpha=0.5, label='Data')
plt.plot(X_new, y_proba[:, 1], color='red', label='Logistic Regression')
plt.xlabel('X')
plt.ylabel('Probability')
plt.legend()
plt.show()
