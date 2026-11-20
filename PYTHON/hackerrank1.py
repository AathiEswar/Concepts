def check_all_higher(lst,k):
    for i in lst:
        if i<k:
            return 0

    return 1

def after_formula(x,y):
    return x+(2*y)

n,k = tuple(map(int, input().split()))  
lst= list(map(int,input().split()))
loop_on = 0
count=0
while(loop_on==0):
    sorted(lst)
    appending_ele = after_formula(lst[0],lst[1])
    lst.append(appending_ele)
    count+=1
    loop_on =check_all_higher(lst,k)
    if (loop_on==1):
        breakz

print(count)


