import numpy as np
from math import ceil

def train_test_split(X, y, test_ratio=0.7, seed= None):
    assert X.shape[0] == y.shape[0], 'X y 的行数要一样'
    if seed:
        np.random.seed(seed)
    shuffle_index = np.random.permutation(len(X))
    test_size = ceil(len(X) * test_ratio)
    test_index = shuffle_index[:test_size]
    train_index = shuffle_index[test_size:]
    X_train = X[train_index]
    X_test = X[test_index]
    y_train = y[train_index]
    y_test = y[test_index]
    return X_train, X_test, y_train, y_test
    
