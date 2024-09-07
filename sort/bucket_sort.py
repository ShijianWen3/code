
#将数据尽量平均分配至每个桶，然后对每个桶排序，最后按桶的顺序合并
#对[0,1)的浮点数进行排序
def bucket_sort(goal:list):
    k=len(goal)//2
    buckets=[[] for _ in range(k)]
    for element in goal:
        index=int(element*k)
        buckets[index].append(element)
    for bucket in buckets:
        bucket.sort()
    i=0
    for bucket in buckets:
        for element in bucket:
            goal[i]=element
            i+=1



if __name__=='__main__':
    floatdata=[0.49, 0.96, 0.82, 0.09, 0.57, 0.43, 0.91, 0.75, 0.15, 0.37]
    bucket_sort(floatdata)
    print(floatdata)