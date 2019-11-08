
def binarySearch(arr,target):
    targetRange = [-1, -1]
    if not arr or target < arr[0] or target > arr[len(arr) - 1]:
        return []
    binarySearchHelper(arr,0,len(arr)-1,target,targetRange,True)
    binarySearchHelper(arr,0,len(arr)-1,target,targetRange,False)
    return  targetRange

def binarySearchHelper(arr,left,right,target,targetRange,goLeft):

    while left<= right:

        mid = (left+right)//2
        current = arr[mid]

        if current < target:
            left = mid + 1
        elif current > target:
            right = mid - 1
        elif current == target:
            if goLeft:
                if mid == 0 or arr[mid-1] != target:
                    targetRange[0] = mid
                    return
                else:
                    right = mid-1
            else:
                if mid == len(arr)-1 or arr[mid+1] != target:
                    targetRange[1] = mid
                    return
                else:
                    left = mid+1


arr = [2,3,4,4,4,5,22,34,55,55,55,55,55,65,67,89,90,90,90]
target = 90


print(binarySearch(arr,target))




#
# def getRange(arr,target):
#
#     finalRange = [-1,-1]
#     binarySearch(arr, target, 0, len(arr)-1, finalRange, True)
#     binarySearch(arr, target, 0, len(arr)-1, finalRange, False)
#     return finalRange
#
# def binarySearch(arr,target,left,right,finalRange,goLeft):
#
#     if left > right:
#         return
#
#     mid = (left+right)//2
#
#     if arr[mid] < target:
#         binarySearch(arr, target, mid+1, right, finalRange, goLeft)
#     elif arr[mid] > target:
#         binarySearch(arr, target, left, mid-1, finalRange, goLeft)
#     else:
#         if goLeft:
#             if mid == 0 or arr[mid] != arr[mid-1]:
#                 finalRange[0] = mid
#                 return
#             else:
#                 binarySearch(arr, target, left, mid - 1, finalRange, goLeft)
#         else:
#             if mid == len(arr)-1 or arr[mid] != arr[mid+1]:
#                 finalRange[1] = mid
#                 return
#             else:
#                 binarySearch(arr, target, mid+1, right, finalRange, goLeft)
