# Warshall Algorithm
import random as r
import sys
__author__ = "Pattarapon Buathong 62070504012"

global vertices

def random_graph(vertices):
    # Generate zero matrix (vertices x vertices)
    matrix_random = [[0 for m in range(vertices)] for n in range(vertices)]

    for i in range(vertices):
        for j in range(vertices):
            u = r.random()
            if i != j and u < 0.3:
                u = 1
            else:
                u = 0
            matrix_random[i][j] = u
    print("Generate an adjacency matrix of a random graph ... \n")
    # Print the matrix
    for row in matrix_random:
        for col in row:
            print(col, end=" ")
        print()
    return matrix_random

def Warshall_algo(vertices):
    matrix_random = random_graph(vertices)
    R_k = matrix_random

    for k in range(vertices):
        for i in range(vertices):
            for j in range(vertices):
                R_k[i][j] = R_k[i][j] or (R_k[i][k] and R_k[k][j])
    print("Transitive closure of the graph ... \n")
    for r in R_k:
        for c in r:
            print(c, end=" ")
        print()
    return R_k

if __name__ == "__main__":
    vertices = int(input("Input number of vertices between 4 to 9: "))
    if vertices < 4 or vertices > 9:
        print("Please input number between 4 to 9 \n")
        sys.exit()
    Warshall_algo(vertices)
