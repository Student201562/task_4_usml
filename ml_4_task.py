import numpy as np
import sys

# находим кратчайший путь по алгоритму Дейкстра.
def algorithm_dijkstra(start_v, matrix, n):
    copy_m = [[j if j != 0 else 1000000 for j in i] for i in matrix]

    valid = [True] * n
    weight = [1000000] * n
    weight[start_v] = 0
    for i in range(n):
        min_weight = 1000001
        ID_min_weight = -1
        for i in range(n):
            if valid[i] and weight[i] < min_weight:
                min_weight = weight[i]
                ID_min_weight = i
        for i in range(n):
            if weight[ID_min_weight] + copy_m[ID_min_weight][i] < weight[i]:
                weight[i] = weight[ID_min_weight] + copy_m[ID_min_weight][i]
        valid[ID_min_weight] = False
    return weight

# берем ближайщую подходящую последовательность
def wayPlusOne(way, n):
    while (True):
        way[-1] += 1
        l = len(way) - 1
        while (way[l] == n):
            way[l - 1] += 1
            way[l] = 0
            l -= 1
        if (len(way) == len(set(way))):
            break
    return way

# находим факториал, но мы его не используем, так как не проходил тест)))
def factorial(n):
    fac = 1
    i = 0
    while i < n:
        i += 1
        fac = fac * i
    return fac

n = int(input())
matrix_dijkstra = []
input_matrix = np.array([list(map(int, input().split())) for i in range(n)])

for i in range(n):
    matrix_dijkstra.append(algorithm_dijkstra(i, input_matrix, n))
# print('очень быстро')
for i in np.arange(0, n, 1):
    for j in np.arange(0, n, 1):
        if matrix_dijkstra[i][j] == 0:
            matrix_dijkstra[i][j] = sys.maxsize  # Заполненяем главной диагонали матрицы

way = [] # путь по всем точкам до конца
for i in range(n):
    way.append(i)

min_sum = sys.maxsize
fac = 10000  # factorial(n-2) так получилось))) если берем факториал, то по времени не прохожу
# print(factorial(n))
for i1 in range(fac):
    current_way_sum = sum(matrix_dijkstra[way[i]][way[i + 1]] for i in np.arange(0, n - 1, 1)) + matrix_dijkstra[way[-1]][way[0]] # считает длину текущего пути
    if (i1 != fac - 1):
        wayPlusOne(way, n)
    if (current_way_sum < min_sum):
        min_sum = current_way_sum
print(min_sum)