class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Solution:
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

    def insert(self,head,data):
    #Complete this method

        # newnode = Node(data)
        #
        # print("Newnode data: {}".format(newnode.data))
        # if head == None:
        #     head = newnode
        #     print("Came in head none: {}".format(head.data))
        # else:
        #     newnode.next = head.next
        #     head.next = newnode
        #     head = head.next
        #     print("Came in head not none: {}".format(head.data))
        #
        # print("Outside: Head: {}; Data: {}".format(head, head.data))
        newnode = Node(data)
        if head is None:
            head = newnode
            self.tail = head
        else:
            self.tail.next = newnode
            self.tail = newnode
        return head

mylist= Solution()
# T=int(input())
T=4
head=None
for i in [2,3,4,5]:
    # data=int(input())
    data = i
    head=mylist.insert(head,data)
mylist.display(head);