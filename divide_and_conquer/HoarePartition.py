# Hoare Partition
__author__ = "Samkok"

# Input Array A[l ... r]

def hoare_partition(unsorted_list, low, high):
    p = unsorted_list[low] # choose pivot at arr[0]
    i = low
    j = high
    print(p, i, j)
    while True:
        while (unsorted_list[i] < p):
            i += 1
        while (unsorted_list[j] > p):
            j -= 1
        if i >= j:
            return j
        print(p, i, j)
        unsorted_list[i], unsorted_list[j] = unsorted_list[j], unsorted_list[i]        
        # unsorted_list[low], unsorted_list[j] = unsorted_list[j], unsorted_list[low]
        print(unsorted_list)

def quick_sort(unsorted_list, low, high):
    if len(unsorted_list) == 1:
        return unsorted_list
    elif(low<high):
        parti = hoare_partition(unsorted_list, low, high)
        print("Partition at element: {}".format(parti))
        quick_sort(unsorted_list, low, parti)
        quick_sort(unsorted_list, parti+1, high)
        
if __name__ == '__main__':
    test_list = ['S','O','R','T','I','N','G']
    quick_sort(test_list, 0 , len(test_list)-1)
    print("Sorted list is {}".format(test_list))