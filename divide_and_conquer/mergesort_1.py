# Alphabetically merge sort
__author__ = "Samkok"

def merge_sort(unsorted_list):
    # if list has more than one element then
    if len(unsorted_list) > 1:

        # find middle of the list
        middle = len(unsorted_list)//2 # // is floor division
        # print(middle)

        # Divide the list into 2 half, left and right
        left = unsorted_list[:middle] # from 0 to middle-1
        right = unsorted_list[middle:] # from middle to end of list
        print("Split left: {}".format(left))
        print("Split right: {}".format(right))
        print("-------------------------------------")
        # recursive
        merge_sort(left)
        merge_sort(right)

        # initiate the buffer
        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                unsorted_list[k] = left[i]
                i += 1
            else:
                unsorted_list[k] = right[j]
                j += 1
            k += 1
            print(unsorted_list)

        # Copying list (copy each elements to unsorted_list)
        if i == len(left):
            while j < len(right):
                unsorted_list[k] = right[j]
                j += 1
                k += 1
                print(unsorted_list)
        else:
            while i < len(left):
                unsorted_list[k] = left[i]
                i += 1
                k += 1
                print(unsorted_list)
        

if __name__ == '__main__':
    unsorted_list_ex = ['S','O','R','T','I','N','G']
    num_test = [12,4,5,2,7,15]

    # print("Given list is", end="\n")
    # print(num_test)
    # merge_sort(num_test)
    # print("Sorted list is: ", end="\n")
    # print(num_test)
    
    print("Unsorted list is {}".format(unsorted_list_ex))
    merge_sort(unsorted_list_ex) # sort the unsorted list
    print("Sorted list is {}".format(unsorted_list_ex))