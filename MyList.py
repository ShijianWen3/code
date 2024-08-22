import random as ra


class Mylist:
    def __init__(self) -> None:
        self.capacity=10
        self.size=0
        self.array=[0]*self.capacity
        self.extend_ratio=2

    def list_extend(self):
        self.array=self.array+[0]*self.capacity*(self.extend_ratio-1)
        self.capacity*=self.extend_ratio

    def get(self,index):
        if index<0 or index>=self.size:
            raise IndexError("访问越界")
        return self.array[index]
    
    def insert(self,index,value):
        if index<0 or index>=self.size:
            raise IndexError("访问越界")
        if self.size==self.capacity:
            self.list_extend()
        for _ in range(self.size-1,index-1,-1):
            self.array[_+1]=self.array[_]
        else:
            self.array[index]=value
            self.size+=1

    def pop(self,index):
        if index<0 or index>=self.size:
            raise IndexError("访问越界")
        for _ in range(index,self.size):
            self.array[_]=self.array[_+1]
        else:
            self.size-=1

    def append(self,value):
        if self.size==self.capacity:
            self.list_extend()
        self.array[self.size]=value
        self.size+=1

    def set(self,index,value):
        if index<0 or index>=self.size:
            raise IndexError("访问越界")
        self.array[index]=value


if __name__=='__main__':
    mylist=Mylist()
    for _ in range(15):
        mylist.append(ra.randint(0,9))
    print(mylist.array)


        



