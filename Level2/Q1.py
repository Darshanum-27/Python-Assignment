
def returnSameElements(arr1,arr2):
    return [i for i in arr1 if i in arr2]
print("Common elements:", returnSameElements([1, 2, 3, 4, 5], [4, 5, 6, 7, 8]))