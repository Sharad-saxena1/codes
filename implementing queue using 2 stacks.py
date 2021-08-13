class stq:
    def __init__(self):
        self.st1=[]
        self.st2=[]
    def enque(self,item):
        return self.st1.append(item)
    def deq(self):
        if not self.st2:
            while self.st1:
                self.st2.append(self.st1.pop())
        return self.st2.pop()

sq=stq
sq.enque(2)
sq.enque(3)
sq.enque(4)
sq.enque(5)
sq.enque(6)
print(sq.deq())