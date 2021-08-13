class singleLinkedList(object):
    def __init__(self,value):
        self.value=value
        self.next_node=None
a=singleLinkedList(1)
b=singleLinkedList(2)
c=singleLinkedList(3)
a.next_node = b
b.next_node=c
print(b.next_node)