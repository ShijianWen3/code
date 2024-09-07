

#计数排序，实质上是桶排序，将数组索引作为桶，索引自带的顺序即为桶的顺序
#只能对非负整数或者可以映射到非负整数的元素排序
def counting_sort(goal:list):
    max=0
    for item in goal:
        if item>max:
            max=item
    count=[0]*(max+1)
    for item in goal:
        count[item]+=1
    i=0
    for index in range(max+1):
        for _ in range(count[index]):
            goal[i]=index
            i+=1


#计数排序拓展，若输入列表元素为对象
def counting_sort_expand(goal:list):
    max=0
    result=[0]*len(goal)
    for item in goal:
        if item>max:
            max=item
    counts=[0]*(max+1)
    for item in goal:
        counts[item]+=1
    for i in range(max+1):
        if i!=0:
            counts[i]=counts[i-1]+counts[i]
    for i in range(len(goal)-1,-1,-1):
        result[counts[goal[i]]-1]=goal[i]
        counts[goal[i]]-=1
    return result


if __name__=='__main__':
    tmp=[1,2,6,5,7,3,5,1,9,4]
    # counting_sort(tmp)
    # print(tmp)
    print(counting_sort_expand(tmp))