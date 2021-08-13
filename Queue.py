class queue(object):
    def __init__(self):
        self.item=[]
    def isempty(self):
        return self.item == []
    def enqueue(self,item):
        return self.item.insert(0,item)
    def dequeue(self):
        return self.item.pop()
    def size(self):
        return len(self.item)
q=queue()
q.enqueue(1)
q.enqueue('Two')
q.enqueue(True)
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())