n = int(input())
m = int(input())
mu = int(m/3)
nu = int(n/2)

dash = "---"
sym = ".|."

print(nu,mu)
for i in range(nu):
    for j in range(nu-i):
        print(dash,end = "")

    print(sym*(i+1),end = "")


    for l in range(i):
        print(sym,end = "")
    print(dash*(nu-i))

