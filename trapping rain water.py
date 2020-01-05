
def waterTrapped(heights):

    # time - O(n)
    # space - O(n)

    if not heights:
        return 0

    length = len(heights)

    waterTrapped = 0

    left = [heights[0]] +[0] *(length-1)
    right = [0] *(length-1) + [heights[-1]]

    for i in range(1 ,length):
        left[i] = max(left[i-1] ,heights[i])

    for j in range(length -2 ,-1 ,-1):
        right[j] = max(right[j+1] ,heights[j])

    for i in range(length):
        waterTrapped += abs(heights[i] - min(left[i] ,right[i]))

    return waterTrapped



arr = [0,1,0,2,1,0,1,3,2,1,2,1]
print(waterTrapped(arr))







































