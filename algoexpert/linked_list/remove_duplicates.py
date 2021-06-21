#   PSEUDOCODE

#   this code assumes that the linkedList is sorted and we have to remove duplicates in place (without need for an extra space)
#   if the list is not sorted, we can use an auxillary data structure like a set to keep unique values while we go through the List

#   to solve this problem:
#   loop (while-loop) through the linkedList and every time we hit a node, check if there is a node that has the same value as it afterwards.
#   if they do, we use the steps below to remove the node.
#   currentNode = head
#   temp = currentNode.next.next (keep the node after the next node)
#   currentNode.next = temp
#   we keep a nextDistinct node that has a different value from the current node

#   Runs in 0(n) time because we only have to look through all of the nodes once 
#   and 0(1) space because we don't need to use any external space

#   this algorithm works because we know that this linkedList is sorted in ascending order and we know that all of the nodes that come after the
#   current node are going to be duplicate values, if duplicate values exist. And if there is no duplicate value after the current node,  then it
#   means nowhere in the entire linkedList is there a duplicate value of whatever the current value is of the current node.


# represents each of the nodes
class LinkedList:
     
    def __init__(self, value) -> None:
        self.value = value
        self.next = None


# the linkedList parameter will be the head/ first node of our linkedList
def removeDuplicatesFromLinkedList(linkedList):
    currentNode = linkedList

    while currentNode is not None:
        nextDistinctNode = currentNode.next

        # while the next node value equals that of the current node value, move to the next node 
        while nextDistinctNode is not None and nextDistinctNode.value == currentNode.value:
            nextDistinctNode = nextDistinctNode.next

        # we set the next pointer of the current node equal to the node that is the next distinct
        # any other nodes are removed by removing the pointer to them
        currentNode.next = nextDistinctNode

        # move pointer to this next node
        currentNode = currentNode.next

    # return the head of the linkedList again
    return linkedList