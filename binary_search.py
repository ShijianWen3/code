

#查找goal在列表中插入的位置(返回索引)
def binary_search(array:list,goal)->int:
    left=0
    right=len(array)-1
    while left<=right:
        middle=left+(right-left)//2
        if array[middle]<goal:
            left=middle+1
        elif array[middle]>goal:
            right=middle-1
        else:
            #已存在相同元素，插入到其左边则插入位置即为相同元素原位置
            return middle
    else:
        return left
#存在重复元素，若找到相同元素，则继续向左边遍历直到区间中无元素(即找到在列表中小于重复值的值的最大值)
def binary_search_repetition(array:list,goal)->int:
    left=0
    right=len(array)-1
    while left<=right:
        middle=left+(right-left)//2
        if array[middle]<goal:
            left=middle+1
        elif array[middle]>=goal:
            right=middle-1
    else:
        return left
    
#查找边界时可以借助二分查找查找后索引性质，查找右边界时就查找goal+k(goal+k应不存在于列表中)
def binary_search_leftedge(array:list,goal):
    result=binary_search_repetition(array,goal)
    if result==len(array) or array[result]!=goal:
        return -1
    return result
def binary_search_rightedge(array:list,goal):
    result=binary_search_repetition(array,goal+1)
    if result==len(array) and array[result-1]!=goal:
        return -1
    return result-1
if __name__=='__main__':
    temp=[1,2,3,4,5,6,6,6,6,6]
    print(binary_search_leftedge(temp,6))
    print(binary_search_rightedge(temp,7))       
