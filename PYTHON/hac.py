inp = input()
inp_split = inp.split()
n = int(inp_split[0])
m = int(inp_split[1])
mu = int(m/3)
nu = int(n/2)

dash = "---"
sym = ".|."
wel = "WELCOME"
we_len = len(wel)

for i in range(nu):
    for j in range(nu-i):
        print(dash,end = "")

    print(sym*(i+1),end = "")


    for l in range(i):
        print(sym,end = "")
    print(dash*(nu-i))

print(wel.center(m,"-"))

for i in range(nu):
    for j in range(i+1):
        print(dash,end = "")
    print(sym*(nu-i),end = "")

    for k in range(nu-i-1):
        print(sym,end = "")

    print(dash*(i+1))