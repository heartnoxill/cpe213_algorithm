import random as r

while(True):
    n = int(input("Enter the size of elements: "))

    if n<=0:
        break
    A = [0]*n
    print("Element of array before sorting: ")
    for i in range(n):
        A[i] = r.randint(1,1000)
    print(A)
    print("Elements of the array after sorting")