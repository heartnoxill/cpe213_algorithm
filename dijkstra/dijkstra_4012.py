# Dijkstra Algorithm
import random as r
import sys
__author__ = "Pattarapon Buathong 62070504012"

global vertices
global nodes

def random_graph(vertices):
    # Generate zero matrix (vertices x vertices)
    matrix_random = [[0 for m in range(vertices)] for n in range(vertices)]

    for i in range(vertices):
        for j in range(vertices):
            u = r.random()
            if i != j and u < 0.4:
                u = r.randint(1,10)
            elif i==j:
                u = 0
            else:
                u = 0
            matrix_random[i][j] = u
            matrix_random[j][i] = u

    print("Generate an cost matrix of an undirected random graph ...")
    # Print the matrix
    for row in matrix_random:
        for col in row:
            print(col, end=" ")
        print()
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
    distance = [sys.maxsize] * vertices
    distance[nodes] = 0 # Distance fron itself = 0
    shrtPath = [False] * vertices
    path = []
    path.append(nodes)
    for foo in range(vertices):
        min_d = shortDist(distance, shrtPath)
        shrtPath[min_d] = True
        for idx in range(vertices):
            if (matrix_random[min_d][idx] > 0) and (shrtPath[idx] == False) and (distance[idx] > distance[min_d] + matrix_random[min_d][idx]):
                distance[idx] = distance[min_d] + matrix_random[min_d][idx]
                path.append(idx)


    print("Vertex \t Distance from source" )
    for j in range(vertices):
        print("{}          {}".format(j, distance[j]))
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
