# Selection Sort
__author__ = "Pattarapon Buathong 62070504012"


# Example of list
list_in = [12, 784, 20, 1, 78]

for ct_i in range(len(list_in)-1):
    min_index = ct_i
    for ct_j in range(ct_i+1, len(list_in)):
        if list_in[ct_j] < list_in[min_index]:
            min_index = ct_j
    # Swap
    list_in[ct_i], list_in[min_index] = list_in[min_index], list_in[ct_i]

print("Sorted List using Selection Sort")
print(list_in)


