# O(n) time
# O(1) space

# code walthrough:
#     1. find the elements which are not in correct order
#     2. find the min and max in those elements (which are not in order)
#     3. find the correct index of the min and max elements in the original array
#     4. answer is, range = index(min) to index(max)

#        this range needs to be sorted

def subArray_sort(array):

    minOutOfOrder = float("inf")
    maxOutOfOrder = float("-inf")

    for i in range(len(array)):
        num = array[i]
        if outOfOrder(i, num, array):
            minOutOfOrder = min(minOutOfOrder, num)
            maxOutOfOrder = max(maxOutOfOrder, num)

    if minOutOfOrder == float("inf"):
        return [-1, -1]

    leftIdx = 0
    rightIdx = len(array)-1
    while minOutOfOrder >= array[leftIdx]:
        leftIdx += 1
    while maxOutOfOrder <= array[rightIdx]:
        rightIdx -= 1

    return [leftIdx, rightIdx]


def outOfOrder(i, num, array):
    if i == 0:
        return num > array[i + 1]
    elif i == len(array) - 1:
        return num < array[i - 1]
    else:
        return array[i - 1] > num or array[i + 1] < num


arr = [1,2,3,5,8,7,6,9,12,15]

print(subArray_sort(arr))


# 2

# O(nlogn) time
# O(1) space

#
# def getAnswer(arr):
#
#     sortedArr = arr[:]
#     sortedArr.sort()
#
#     left = 0
#     right = len(arr)-1
#
#     while arr[left] == sortedArr[left]:
#         left+=1
#         if left == len(arr)-1:
#             break
#
#     while arr[right] == sortedArr[right]:
#         right-=1
#         if right == 0:
#             break
#
#     if left > right:
#         return "array is already sorted"
#
#     return [left,right]
#
# arr = [1,2,4,7,10,11,7,12,6,7,16,18,19]
# print(getAnswer(arr))
