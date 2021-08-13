class deque(object):
    def __init__(self):
        self.item=[]
    def isEmpty(self):
        return self.item == []
    def addFront(self,item):
        return self.item.append(item)
    def addRear(self,item):
        return self.item.insert(0,item)
    def removefront(self):
        return self.item.pop()
    def removeBack(self):
        return self.item.pop(0)
    def size(self):
        return len(self.item)

dq= deque
dq.addRear('hello')
#dq.addRear('rear two')
#dq.addRear(True)
#dq.addFront(52)
#dq.addFront('front two')
#dq.addFront(False)
print(dq.removefront())
print(dq.removefront())
print(dq.removefront())
print(dq.removefront())
print(dq.removefront())
#print(dq.removeBack())
