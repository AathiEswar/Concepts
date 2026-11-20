n = int(input())
country = []
for i in range(n):
    ele = input()
    country.append(ele)

print(len(set(country)))