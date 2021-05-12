import random as r
import numpy as np
import sys

def main():
  INFTY = 100000
  prev = [0]*10
  T = [0]*10
  d = [0]*10  #the length of sortest path from source (s) to v
  n = int(input("Enter the number of vertices (2 to 10):"))
  c = np.zeros((n,n),int)

  if n < 2 or n > 10:
    sys.exit()

  print("Generate a cost matrix of an unidirected random graph ..")
  
  for i in range(n):
    for j in range(i,n):
      u = r.randint(1,10)/10 # 1 to 10 / 10

      if i==j :
        c[i][j] = 0 # cost to itself
      elif u < 0.4: # random num < 0.4, assign direct edge
        c[i][j] = r.randint(1,10)
        c[j][i] = c[i][j]
      else :
        c[i][j] = 1
        c[j][i] = -1
  print(c)

if __name__ == '__main__':
    main()