



# time - O(n)
# space - O(n)

def firstMissingPositive(nums):

    if not nums:
        return 1

    ls = set(nums)
    mx = max(nums)

    for i in range(0, mx + 1):          #the missing element should be between 0 --- max(ls)+1
        if i > 0 and i not in ls:
            return i

    if mx > 0:
        return mx + 1
    else:
        return 1



nums = [3,4,-1,1]
print(firstMissingPositive(nums))