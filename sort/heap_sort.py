

#存放在数组中的堆(完全二叉树)的堆化
def heapify(goal:list,index:int,len:int):
    while True:
        left=2*index+1
        right=2*index+2
        max=index
        if left<len and goal[left]>goal[max]:
            max=left
        if right<len and goal[right]>goal[max]:
            max=right
        if max == index:
            break
        goal[max],goal[index]=goal[index],goal[max]
        index=max


def heap_sort(goal:list):
    #建堆
    for _ in range((len(goal)-1-1)//2,-1,-1):
        heapify(goal,_,len(goal))
    #依次取出堆顶元素放在堆底位置，然后对变小的堆进行堆化
    for _ in range(len(goal)-1):
        goal[0],goal[len(goal)-1-_]=goal[len(goal)-1-_],goal[0]
        heapify(goal,0,len(goal)-_-1)


if __name__=='__main__':
    tmp=[1,2,6,5,7,3,5,1,9,4]
    heap_sort(tmp)
    print(tmp)

