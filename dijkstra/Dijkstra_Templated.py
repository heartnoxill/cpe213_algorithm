# Dijkstra algorithm with given template
import random as r
import numpy as np
import sys
__author__ = "Pattarapon Buathong 62070504012"

global INFTY
global MAX_VERTICES
global FALSE
global TRUE

INFTY = 100000 # value for infinity
MAX_VERTICES = 10 
FALSE = 0
TRUE = 1
#c = np.zeros((MAX_VERTICES+1, MAX_VERTICES+1))  #Cost matrix
T=[0]*10            #A set of nodes already in the tree
# prev = [0]*10       #Previous node to source
d=[0]*10            #Distance to source
u = FALSE

def shortPath(d, n):
  m = 0 # number of vertices already in the tree
  mincost = INFTY
  for i in range(n):
    if d[i] < mincost and T[i] == u:
      mincost = d[i]
      m = i
  return m

def Dijkstra(c, n):
  print("Enter the source node (1 to {}): ".format(n))
  s = int(input())
  if s < 1 or s > n:
    print("Input out of range")
    sys.exit()
  for i in range(n):
    T[i] = FALSE
    if i == s:  # Distance from node itself = 0
      d[i] = 0
    else:  # Initial distance to other  = inf
      d[i] = INFTY

  prev = []
  prev.append(s) # First is node
  for v in range(n):
    m = shortPath(d, n)
    T[m] = TRUE
    for idx in range(n):
      if (c[m][idx] > 0) and (T[idx] == u) and (d[idx] > d[m] + c[m][idx]):
        d[idx] = d[m] + c[m][idx]
        print(d)
        if d[idx] != INFTY:
          if len(prev) == n:
            break
          else:
            prev.append(idx)

  print("Shortest path from {} to every node ... ".format(s) )
  print("Vertex \t Distance from source")
  for j in range(n):
    print("{}                    {}".format(j, d[j]))
  print("Shortest Distance")
  for p in prev:
    print(p, end="->")

def main():
  n = int(input("Enter the number of vertices (2 to 10): "))
  c = np.zeros((n, n), int)

  if n < 2 or n > MAX_VERTICES:
    sys.exit()
  print("Generate a cost matrix of an unidirected random graph ...")
  for i in range(n):
    for j in range(i, n):
      u = r.randint(1,10)/10
      if i==j:
        c[i][j] = 0
      elif u < 0.4:
        c[i][j] = 1+r.randint(1,10)%10
        c[j][i] = c[i][j]
      else:
        c[i][j] = 1
        c[j][i] = -1
  print(c)
  Dijkstra(c, n)

if __name__ == '__main__':
  main()