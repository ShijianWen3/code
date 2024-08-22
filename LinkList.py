import random as ra

class listnode:
    def __init__(self,value) -> None:
        self.value=value
        self.next:listnode=None

class LinkList:
    def __init__(self) -> None:
        self.start:LinkList=None
        self.size:int=0

    def append(self,value):
        if  not self.start:
            self.start=listnode(value)
        else:
            current_node=self.start
            while current_node.next:
                current_node=current_node.next
            else:
                current_node.next=listnode(value)
        self.size+=1

    def printf(self):
        current_node=self.start
        while current_node:
            print(current_node.value,end='->')
            current_node=current_node.next
        print(None)

if __name__=='__main__':
    MyLinkList=LinkList()
    for _ in range(10):
        MyLinkList.append(ra.randint(0,9))
    else:
        MyLinkList.printf()        

