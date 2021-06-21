# 83. Remove Duplicates from Sorted List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def deleteDuplicates(self, head: ListNode) -> ListNode:
    currentNode = head
    while currentNode is not None:
        nextDistinctNode = currentNode.next
        while nextDistinctNode is not None and nextDistinctNode.val == currentNode.val:
            nextDistinctNode = nextDistinctNode.next
        currentNode.next = nextDistinctNode
        currentNode = nextDistinctNode
    
    return head


if __name__ == '__main__':
        # 83
        test_case_1 = [1,1,2]
        test_case_2 = [1,1,2,3,3]
        print(deleteDuplicates(test_case_2))