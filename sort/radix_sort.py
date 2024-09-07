


def digit_get(num:int,exp,digit:int=10):
    return  (num//exp)%digit

def counting_sort(goal:list,exp,digit:int=10):
    result=[0]*len(goal)
    counts=[0]*digit
    for item in goal:
        counts[digit_get(item,exp)]+=1
    for i in range(digit):
        if i!=0:
            counts[i]=counts[i]+counts[i-1]
    for i in range(len(goal)-1,-1,-1):
        index=counts[digit_get(goal[i],exp)]-1
        result[index]=goal[i]
        counts[digit_get(goal[i],exp)]-=1
    return result

def radix_sort(goal:list,digit:int=10):
    max_element=max(goal)
    exp=1
    while exp<=max_element:
        goal=counting_sort(goal,exp)
        exp*=digit
    return goal
    

if __name__=="__main__":
    tmp=[205,156,211,428,348,118,]
    print(radix_sort(tmp))
    