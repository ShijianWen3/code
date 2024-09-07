

#归并排序，合并环节
def merge(goal:list,left:int=0,right:int=None):
    mid=left+(right-left)//2
    tmp=[0]*(right-left+1)
    i,j,k=left,mid+1,0
    while i<=mid and j<=right:
        if goal[i]<=goal[j]:
            tmp[k]=goal[i]
            i+=1
        else:
            tmp[k]=goal[j]
            j+=1
        k+=1

    while i<=mid:
        tmp[k]=goal[i]
        i+=1
        k+=1
    while j<=right:
        tmp[k]=goal[j]
        j+=1
        k+=1
    for _ in range(len(tmp)):
        goal[left+_]=tmp[_]

#归并排序，递归环节
#与二叉树中dfs后序遍历顺序一致
def merge_sort(goal:list,left:int=0,right:int=None):
    if right is None:
        right=len(goal)-1
    if left>=right:
        return
    mid=left+(right-left)//2
    merge_sort(goal,left,mid)
    merge_sort(goal,mid+1,right)
    merge(goal,left,right)

if __name__=='__main__':
    tmp=[1,2,6,5,7,3,5,1,9,4]
    merge_sort(tmp)
    print(tmp)
    