import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

X, y = make_classification(
    n_samples=100,      
    n_features=2,       
    n_informative=2,    
    n_redundant=0,      
    n_classes=2,        
    random_state=42
)

df = pd.DataFrame(data=X, columns=['Feature1', 'Feature2'])
df['Target'] = y

X_train, X_test, y_train, y_test = train_test_split(
    df[['Feature1', 'Feature2']],
    df['Target'],
    test_size=0.2,
    random_state=42
)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

classifiers = {
    'Decision Tree': DecisionTreeClassifier(random_state=42),
    'SVM': SVC(random_state=42),
    'Random Forest': RandomForestClassifier(random_state=42),
    'KNN': KNeighborsClassifier(),
    'Logistic Regression': LogisticRegression(random_state=42)
}

for name, clf in classifiers.items():
    clf.fit(X_train_scaled, y_train)
    y_pred = clf.predict(X_test_scaled)
    
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)
  
    print(f'{name} Classifier:')
    print(f'Accuracy: {accuracy:.2f}')
    print(f'Precision: {precision:.2f}')
    print(f'Recall: {recall:.2f}')
    print(f'F1 Score: {f1:.2f}\n')

labels = list(classifiers.keys())
accuracy_values = [accuracy_score(y_test, clf.predict(X_test_scaled)) for clf in classifiers.values()]

plt.barh(labels, accuracy_values, color='skyblue')
plt.xlabel('Accuracy')
plt.title('Comparison of Supervised Learning Algorithms')
plt.show()
