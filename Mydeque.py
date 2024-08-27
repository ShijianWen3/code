from array_link_list.LinkList import listnode



class LinkDeque():
    def __init__(self) -> None:
        self.size:int=0
        self.start:listnode=None
        self.end:listnode=None
    #添加节点
    def push(self,value,dir:bool):
        if not(self.start or self.end):
            self.start=self.end=listnode(value)#将双向链表的两个方向联系起来，若无此行命令则相当于创建了两个单独的链表
        elif dir:
            tmp=self.start
            self.start=listnode(value)
            self.start.next=tmp
            self.start.next.previous=self.start

        else:
            tmp=self.end
            self.end=listnode(value)
            self.end.previous=tmp
            self.end.previous.next=self.end

        self.size+=1

    def pop(self,dir:bool):
        if dir:
            if self.start:
                self.start.value=None
                self.start=self.start.next
            else:
                raise IndexError('访问越界')
        else:
            if self.end:
                self.end.value=None
                self.end=self.end.previous
            else:
                raise IndexError('访问越界')
        self.size-=1
    
    def peak(self,dir:bool):
        if dir:
            return self.start.value
        else:
            return self.end.value
        
    def printf(self):
        current_node=self.start
        while current_node:
            print(current_node.value,end='->')
            current_node=current_node.next
        print(None)

class ArrayDqueue(list):
    def __init__(self)->None:
        super().__init__()
        self.size:int=0
        self.start:int=None
    def list_index(self,index:int):
        #使用取模方式实现数组索引首尾相接
        #由于此处并不算是严格意义上的数组，而是继承的列表，所以未使用到此方法
        return (index+self.size)%(self.size)
    def push(self,value,dir:bool):
        #继承了列表类，避免了动态扩容问题
        if dir:
            if self.size:
                if self.start:
                    self[self.start-1]=value
                    self.start-=1
                else:
                    self.append(value)
            else:
                self.append(value)
                self.start=0
        else:
            self.append(value)
        self.size+=1

    def pop(self,dir:bool):
        if dir:
            self[self.start]=None
            self.start+=1
        else:
            super().pop()
        self.size-=1

    def printf(self):
        for _ in range(self.start,self.start+self.size):
            print(self[_],end='->')
        print()
        
        
if __name__=='__main__':
    # deque=LinkDeque()
    deque=ArrayDqueue()
    deque.push(1,True)
    deque.push(2,True)
    deque.push(3,False)
    deque.printf()
    deque.pop(True)
    deque.printf()
    deque.pop(False)
    deque.printf()