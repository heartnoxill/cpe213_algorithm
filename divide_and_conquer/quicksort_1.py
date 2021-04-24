# Alphabetically QuickSort
__author__ = "Samkok"

def quick_sort(unsorted_list):

    # Initiate the hold lists
    less = []
    equal = []
    greater = []

    # if list has more than one element then
    if len(unsorted_list) > 1:
        print("------------------------------")
        pivot = unsorted_list[0]
        print("Pivot: {}".format(pivot))
        for x in unsorted_list:
            if x < pivot:
                less.append(x)
            elif x == pivot:
                equal.append(x)
            elif x > pivot:
                greater.append(x)
        print("Less: {}".format(less))
        print("Equal: {}".format(equal))
        print("Greater: {}".format(greater))
        return quick_sort(less) + equal + quick_sort(greater)
    else:
        return unsorted_list

if __name__ == '__main__':
    test_list = ['S','O','R','T','I','N','G']
    print("Unsorted list: {}".format(test_list))
    print("Sorted list: {}".format(quick_sort(test_list)))
