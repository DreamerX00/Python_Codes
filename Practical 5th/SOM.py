import numpy as np
from minisom import MiniSom
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.preprocessing import StandardScaler

iris = datasets.load_iris()
X = iris.data
y = iris.target
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

som_shape = (10, 10)  
input_len = X.shape[1]  


som = MiniSom(som_shape[0], som_shape[1], input_len, sigma=1.0, learning_rate=0.5)
som.train_random(X_scaled, 100)
winners = np.array([som.winner(x) for x in X_scaled])

plt.figure(figsize=(10, 10))
for i, (x, w) in enumerate(zip(X_scaled, winners)):
    plt.text(w[0], w[1], str(y[i]), color=plt.cm.Dark2(y[i] / 3.), fontdict={'weight': 'bold', 'size': 11})

plt.xticks(np.arange(som_shape[0] + 1) - 0.5)
plt.yticks(np.arange(som_shape[1] + 1) - 0.5)
plt.grid()
plt.show()
