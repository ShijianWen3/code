#分组基准数优化，避免传入数组有序时选取到最值使得快排算法退化
def median(goal:list,left:int=0,right:int=None):
    if right is None:
        right=len(goal)-1
    median=left if goal[left]>goal[right] else right
    mid=left+(right-left)//2
    if goal[median] <= goal[mid]:
        return median
    else:
        if median==right:
            return left if goal[left]>=goal[mid] else mid
        else:
            return right if goal[right]>=goal[mid] else mid
#分组函数，以数组最左侧值作为基准值   
def seperation(goal:list,left:int=0,right:int=None):
    if right is None:
        right=len(goal)-1
    base=median(goal,left,right)
    goal[left],goal[base]=goal[base],goal[left]
    i,j=left,right
    while i<j:
        while i<j and goal[j]>=goal[left]:
            j-=1
        while i<j and goal[i]<=goal[left]:
            i+=1
        goal[i],goal[j]=goal[j],goal[i]
    goal[left],goal[i]=goal[i],goal[left]
    return i
#快排递归，并在在递归前判断子数组大小，只对长度更小的子数组递归，避免输入数据有序时导致递归深度达到O(n)降低时间效率
def quick_sort(goal:list,left:int=0,right:int=None):
    if right is None:
        right=len(goal)-1
    while left<right:
        base=seperation(goal,left,right)
        if base-left<right-base:
            quick_sort(goal,left,base-1)
            left=base+1
        else:
            quick_sort(goal,base+1,right)
            right=base-1
    
if __name__=='__main__':
    goal=[1,2,6,5,7,3,5,1,9,4]
    quick_sort(goal)
    print(goal)
    