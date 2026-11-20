def querry_1(n,arr,x,y,last_answer):
    idx = ((x^last_answer)%n)
    arr[idx].append(y)
    


def querry_2(n,arr,x,y,last_answer):
    idx = ((x^last_answer)%n)
    arr_idx = arr[idx]
    last_answer = arr_idx[y%len(arr_idx)]
    print(last_answer)
    return (last_answer)


n,m = [a for a in input().split()]
n,m = int(n),int(m)
arr = []
qur = []
last_answer = 0
for j in range(n):
    arr.append([])

for i in range(m):
    qur_inp = [int(a) for a in input().split()]
    if qur_inp[0] == 1:
        querry_1(n,arr,qur_inp[1],qur_inp[2],last_answer)

    else:
        last_answer = querry_2(n,arr,qur_inp[1],qur_inp[2],last_answer)


