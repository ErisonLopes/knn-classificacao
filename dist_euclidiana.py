import math
import numpy as np

v1 = [1.2, 2, 3.8, 4.5]
v2 = [0.5, 4.5, 9.6, 3.4]

def dist_euclidiana(v1, v2):
    dim = len(v1)
    soma = 0
    for i in range(dim - 1):
        soma += math.pow(v1[i] - v2[i], 2)
    return math.sqrt(soma)

print('%.2f' % dist_euclidiana(v1, v2))

#distancia euclidiana com numpy
def dist_euclidiana_np(v1, v2):
    v1, v2 = np.array(v1), np.array(v2)
    diff = v1 - v2
    quad_dist = np.dot(diff, diff)
    return math.sqrt(quad_dist)

print('%.2f' % dist_euclidiana_np(v1, v2))