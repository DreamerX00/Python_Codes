import pandas as pd
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, classification_report

data = pd.read_csv('test.csv')  

print("NaN values in the dataset:")
print(data.isnull().sum())

data = data.dropna()
X = data.iloc[:, :-1]
y = data.iloc[:, -1]

classifier = GaussianNB()
classifier.fit(X, y)

y_pred = classifier.predict(X)
accuracy = accuracy_score(y, y_pred)

print(f'Accuracy: {accuracy:.2f}')
print('\nClassification Report:')
print(classification_report(y, y_pred))
