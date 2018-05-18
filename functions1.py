import numpy as np


def softmax(vector):
    exp_vector = np.exp(vector)
    return exp_vector / np.sum(exp_vector)


# v = np.array([1, 10, 0]).reshape((3, 1))
# print(v)
# print(softmax(v))
