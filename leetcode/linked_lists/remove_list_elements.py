# 203. Remove Linked List Elements

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def remove_elements_1(self, head: ListNode, val: int) -> ListNode:
    refHead = ListNode(val=-1, next=head)
    currentNode = refHead
    
    while currentNode.next is not None:
        if currentNode.next.val == val:
            currentNode.next = currentNode.next.next
        else:
            currentNode = currentNode.next

    return refHead.next


def remove_elements_2(self, head: ListNode, val: int) -> ListNode:
    while head is not None and head.val == val:
        head = head.next

    currentNode = head
    while currentNode is not None:
        if currentNode.next is not None and currentNode.next.val == val:
            currentNode.next = currentNode.next.next
        else:
            currentNode = currentNode.next

    return head


if __name__ == '__main__':
        # 203
        test_case_1 = [1,2,6,3,4,5,6]
        test_case_2 = [7,7,7,7]
        test_case_3 = []
        print(remove_elements_1(test_case_3))
