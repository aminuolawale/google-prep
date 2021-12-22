from typing import List 


def merge(array1: List[int], array2: List[int]) -> List[int]:
    """ """
    iterator1 = iterator2 = 0
    result = [0 for _ in range(len(array1) + len(array2))]
    k = 0
    while iterator1 < len(array1) or iterator2 < len(array2):
        if iterator1  < len(array1):
            val1 = array1[iterator1]
        else:
            val1 = float("inf")
        if iterator2 < len(array2):
            val2 = array2[iterator2]
        else:
            val2 = float("inf")
        if val1 < val2:
            result[k]= val1
            iterator1 += 1
        else:
            result[k] = val2
            iterator2 += 1
        k += 1
    return result



def merge_sort(array: List[int]) -> List[int]:
    """ """
    if len(array) == 1:
        return array
    array_midpoint = len(array)//2
    left = array[:array_midpoint]
    right = array[array_midpoint:]
    return merge(merge_sort(left), merge_sort(right))




if __name__ == "__main__":
    array = [3,3,6,1,6,3,-1,45, 2,64,4,-9]
    result = merge_sort(array)
    print(result)