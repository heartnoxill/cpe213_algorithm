# Quicksort random
# Hoare Partition
import random as r
__author__ = "Pattarapon Buathong 62070504012"

# Input Array A[l ... r]

def hoare_partition(unsorted_list, low, high):
    p = unsorted_list[low] # choose pivot at arr[0]
    i = low
    j = high
    # print(p, i, j)
    while True:
        while (unsorted_list[i] < p):
            i += 1
        while (unsorted_list[j] > p):
            j -= 1
        if i >= j:
            return j
        # print(p, i, j)
        unsorted_list[i], unsorted_list[j] = unsorted_list[j], unsorted_list[i]        
        # unsorted_list[low], unsorted_list[j] = unsorted_list[j], unsorted_list[low]
        # print(unsorted_list)

def quick_sort(unsorted_list, low, high):
    if len(unsorted_list) == 1:
        return unsorted_list
    elif(low<high):
        parti = hoare_partition(unsorted_list, low, high)
        # print("Partition at element: {}".format(parti))
        quick_sort(unsorted_list, low, parti)
        quick_sort(unsorted_list, parti+1, high)
        
if __name__ == '__main__':
    # test_list = ['S','O','R','T','I','N','G']
    n = int(input("Enter the size of elements: "))
    test_list = [0]*n
    for i in range(n):
        test_list[i] = r.randint(1,1000)
    print("Element of array before sorting: {}".format(test_list))
    quick_sort(test_list, 0 , len(test_list)-1)
    print("Sorted list is {}".format(test_list))