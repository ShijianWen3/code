from array_link_list import LinkList


class LinkListStack(LinkList.LinkList):
    def __init__(self):
        super().__init__()

    def push(self,value):
        tmp=self.start
        self.start=LinkList.listnode(value)
        self.start.next=tmp
        self.size+=1

    def pop(self):
        self.start=self.start.next
        self.size-=1

    def peak(self):
        return self.start.value
    


class ArrayStack(list):
    def __init__(self):
        super().__init__()
        self.size:int=0
    def push(self,value):
        self.append(value)
    def pop(self):
        self[len(self)-1]=None
        self.size-=1
    def peak(self):
        return self[len(self)-1]
    def printf(self):
        for _ in range(len(self)-1,-1,-1):
            print(self[_],end='->')
        print()


if __name__=='__main__':
    stack=LinkListStack()
    # stack=ArrayStack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.printf()
    stack.pop()
    stack.printf()
