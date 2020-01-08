import numpy as np

def accuracy_score(y_test, y_predict):
    assert y_test.shape[0] == y_predict.shape[0], "预测的y值和测试集的y值行数要一样"
    return sum(y_test == y_predict) / len(y_predict)