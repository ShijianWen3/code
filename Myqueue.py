from array_link_list.LinkList import LinkList
from array_link_list.LinkList import listnode
class Linkque(LinkList):
    def __init__(self) -> None:
        super().__init__()
        self.size:int=0

    def push(self,value):
        tmp=self.start
        self.start=listnode(value)
        self.start.next=tmp
        self.size+=1
    
    def pop(self):
        tmp=self.start
        while tmp.next.next:
            tmp=tmp.next
        tmp.next=None
    def peak(self):
        tmp=self.start
        while tmp.next:
            tmp=tmp.next
        return tmp.value


class Arrayque(list):
    def __init__(self):
        super().__init__()
        self.size:int=0
        self.start:int=0
        #引入start属性指向队列首元素，避免了在pop()时移动剩下的元素(O(n))，而是改变start的值实现出队列(O(1))

    def push(self,value):
        self.append(value)
        self.size+=1

    def pop(self):
        self[self.start]=None
        self.start+=1
        self.size-=1

    def peak(self):
        return self[self.start]
    
    def printf(self):
        for _ in range(len(self)-1,self.start-1,-1):
            print(self[_],end='->')
        print()
        
        

if __name__=='__main__':
    # queue=Linkque()
    queue=Arrayque()
    queue.push(1)
    queue.push(2)
    queue.push(3)
    queue.printf()
    queue.pop()
    queue.printf()
    print(queue.peak())

        