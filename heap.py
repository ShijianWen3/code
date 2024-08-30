from Tree import bfs

class Myheap:
    def __init__(self,data:list) -> None:
        self.max_heap=data
        #将所有元素全部放进堆里
        for _ in range(self.parent(len(self.max_heap)-1),-1,-1):
            self.heapify(_)
        #从堆底(最底层最右侧节点)节点的父节点开始向根节点(堆顶)循环堆化，即堆的构建从下至上，同时从堆底的父节点开始循环可以减少对叶节点的堆化，因为叶节点本身是合法堆
        

    def right(self,index:int):
        return index*2+2
    def left(self,index:int):
        return index*2+1
    def parent(self,index:int):
        return (index-1)//2
    def peak(self):
        return self.max_heap[0]
    def heapify(self,root_index:int):
        index:int=root_index
        while True:
            current=index
            if self.left(index)>=len(self.max_heap):
                break
            if self.max_heap[index]<self.max_heap[self.left(index)]:
                tmp=self.max_heap[index]
                self.max_heap[index]=self.max_heap[self.left(index)]
                self.max_heap[self.left(index)]=tmp
                index=self.left(index)
            if self.right(index)>=len(self.max_heap):
                break
            if self.max_heap[index]<self.max_heap[self.right(index)]:
                tmp=self.max_heap[index]
                self.max_heap[index]=self.max_heap[self.right(index)]
                self.max_heap[self.right(index)]=tmp
                index=self.right(index)
            if index==current:
                break
            # if self.left(index)>=len(self.max_heap) or self.right(index)>=len(self.max_heap):
            #     break
            #待解决，当把越界访问判断限定放在此处时仍会产生越界访问
    def insert(self,value):
        self.max_heap.append(value)
        for _ in range(self.parent(len(self.max_heap)-1),-1,-1):
            self.heapify(_)
    def pop(self):
        tmp=self.max_heap[0]
        self.max_heap[0]=self.max_heap[len(self.max_heap)-1]
        self.max_heap.pop()
        for _ in range(self.parent(len(self.max_heap)-1),-1,-1):
            self.heapify(_)
        return tmp


            
        



if __name__=='__main__':
    tmp=[1,2,6,5,7,3,5,1,9,4]
    myheap=Myheap(tmp)
    for _ in range(len(myheap.max_heap)):
        print(myheap.max_heap[_])

            
            

    
