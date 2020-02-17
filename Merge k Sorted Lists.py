# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

def mergeKLists(self, lists: List[ListNode]) -> ListNode:
    if not lists or not any(lists):
        return

    def getList(head):
        ls = []
        while head:
            ls.append(head.val)
            head = head.next
        return ls

    res = []
    for head in range(len(lists)):
        ls = getList(lists[head])
        for i in ls:
            res.append(i)

    res.sort()

    first = head = ListNode(res[0])
    for i in range(1, len(res)):
        head.next = ListNode(res[i])
        head = head.next

    head.next = None
    return first

