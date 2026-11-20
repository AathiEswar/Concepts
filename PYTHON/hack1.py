n = int(input())
for i in range(n):
    p_q = [int(x) for x in input().split()]
    px = p_q[0]
    py = p_q[1]
    qx = p_q[2]
    qy = p_q[3]

    rx = qx+(qx-px)

    ry = qy+(qy-py)

    print(f"{rx} {ry}")

    