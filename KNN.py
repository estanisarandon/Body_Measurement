import math

import numpy as np
from collections import Counter

from sklearn.metrics import accuracy_score


def euclidean_distance(x1, x2):
    x1, y1 = x1
    x2, y2 = x2
    delta_X = x1-x2
    delta_y = y1-y2
    return math.sqrt((delta_X**2) + (delta_y**2))

class KNN:

    def __init__(self, k):
        self.k = k

    def fit(self, X, y):
        self.X_dataset = X
        self.y_dataset = y

    def predict(self, x):
        predicted_labels = [self._predict(x) for x in self.X_dataset]
        return np.array(predicted_labels)

    def _predict(self, x_test):
        # Compute the distances
        distances = []
        for i, ds_data in enumerate(self.X_dataset):
            dist = euclidean_distance(ds_data, x_test)
            distances.append({'dist': dist, 'size': self.y_dataset[i]})
        # Get K-nearest samples and labels
        distances.sort(key=lambda data: data['dist'])
        distances = distances[:self.k]
        counter = Counter([d['size'] for d in distances])
        most_common = counter.most_common(1)[0][1]
        # Calculate accuracy
        acc = round((most_common / self.k) *100)
        size = counter.most_common(1)[0][0]
        return [size, acc]