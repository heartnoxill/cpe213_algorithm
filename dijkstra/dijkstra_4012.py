# Dijkstra Algorithm
import random as r
import numpy as np
import sys

__author__ = "Pattarapon Buathong 62070504012"

global vertices
global nodes

def random_graph(vertices):
    # Generate zero matrix (vertices x vertices)
    matrix_random = np.zeros((vertices,vertices), int)
    print("Generate an cost matrix of an undirected random graph ...")

    for i in range(vertices):
        for j in range(i, vertices):
            u = r.randint(1,10)/10
            if i==j:
                matrix_random[i][j] = 0
            elif u < 0.4:
                matrix_random[i][j] = 1+r.randint(1,10)%10
                matrix_random[j][i] = matrix_random[i][j]
            else:
                matrix_random[i][j] = 1
                matrix_random[j][i] = -1
    print(matrix_random)
    return matrix_random

def shortDist(distance, shrtPath):
    # Minimum distance for next node (infinity at first)
    minsize = sys.maxsize
    min_idx = 0
    for i in range(vertices):
        if distance[i] < minsize and shrtPath[i] == False:
            minsize = distance[i]
            min_idx = i
    return min_idx

def Dijkstra(nodes, vertices):
    matrix_random = random_graph(vertices)
    distance = [sys.maxsize] * vertices # At first, distance = inf
    distance[nodes] = 0 # Distance fron itself = 0
    shrtPath = [0] * vertices
    path = []
    path.append(nodes)
    for foo in range(vertices):
        min_d = shortDist(distance, shrtPath)
        shrtPath[min_d] = True
        for idx in range(vertices):
            if (matrix_random[min_d][idx] > 0) and (shrtPath[idx] == False) and (distance[idx] > distance[min_d] + matrix_random[min_d][idx]):
                distance[idx] = distance[min_d] + matrix_random[min_d][idx]
                if distance[idx] != sys.maxsize:
                    if len(path) == vertices:
                        break
                    else:
                        path.append(idx)


    print("Vertex \t Distance from source" )
    for j in range(vertices):
        print("{}          {}".format(j, distance[j]))
    print("Shortest distance")
    for p in path:
        print(p, end=" -> ")


if __name__ == "__main__":
    vertices = int(input("Input number of vertices between 2 to 10: "))
    if vertices < 2 or vertices > 10:
        print("Please input number between 2 to 10 \n")
        sys.exit()
    nodes = int(input("Input the source node (1 to 10): "))
    if nodes < 1 or nodes > 10:
        print("Please input number between 1 to 10 \n")
        sys.exit()
    Dijkstra(nodes, vertices)
