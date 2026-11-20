n = int(input())
m = int(input())
mu = int(m/3)
nu = int(n/2)

dash = "---"
sym = ".|."

print(nu,mu)
for i in range(nu):
    for j in range(i+1):
        print(dash,end = "")
    print(sym*(nu-i),end = "")

    for k in range(nu-i-1):
        print(sym,end = "")

    print(dash*(i+1))

