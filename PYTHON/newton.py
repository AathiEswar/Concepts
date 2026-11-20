import re

n = int(input())
string = input()


pattern = "http://www./w{3,}.com"



for i in re.finditer(pattern,string):
    print(i)