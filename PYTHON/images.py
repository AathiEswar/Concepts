n = int(input())
lst_names = []
lst_marks = []
lst_all = []
lst_minnames = []
for i in range(n):
    name = input()
    mark = float(input())
    lst_names.append(name)
    lst_marks.append(mark)
    lst_all.append([name,mark])

needed_mark = list(set(sorted(lst_marks)))[1]

for i in lst_all:
    if i[1] == needed_mark:
        lst_minnames.append(i[0])

sorted_lst = sorted(lst_minnames)
 
for k in sorted_lst:
    print(k)



