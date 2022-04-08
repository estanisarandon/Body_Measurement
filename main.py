import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
cmap = ListedColormap(['#FF0000','#00FF00', '#0000FF'])
from collections import Counter
import pandas as pd



def euclidean_distance(x1, x2):
    return np.sqrt(np.sum((x1-x2)**2))


class KNN:

    def __init__(self, k=3):
        self.k = k

    def fit(self, X, y):
        self.X_train = X
        self.y_train = y

    def predict(self, X):
        predicted_labels = [self._predict(x) for x in X]
        return np.array(predicted_labels)

    def _predict(self, x):
        # Compute the distances
        distances = [euclidean_distance(x, x_train) for x_train in self.X_train]
        # Get K-nearest samples and labels
        k_indices = np.argsort(distances)[:self.k]
        k_nearest_labels = [self.y_train[i] for i in k_indices]
        # Majority vote, based on the most common class label
        most_common = Counter(k_nearest_labels).most_common(1)


def main():
    female_tshirt = pd.read_csv('female_tshirt.csv')
    X, y = female_tshirt['Height'], female_tshirt['Weight']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1234)

    print(X_train.shape)
    print(X_train[0])

    print(y_train.shape)
    print(y_train)

    plt.figure()
    plt.scatter(X, y, c=y, cmap=cmap, edgecolor='k', s=20)
    plt.show()



if __name__ == '__main__':
    main()

