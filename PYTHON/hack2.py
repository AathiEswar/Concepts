lst_s = []
lst_q = []
n = int(input())
for a in range(n):
    lst_s.append(input())
q = int(input())
for b in range(q):
    lst_q.append(input())

lst_ans = []

for i in lst_q:
    count = 0
    for j in lst_s:
        if len(i) == len(j):
            if i in j:
                count +=1
    lst_ans.append(count)

for k in lst_ans:
    print(k)