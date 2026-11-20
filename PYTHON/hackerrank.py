s=input()
t1=int(s[:2])
t2=int(s[3:5])
t3=int(s[6:8])
t=s[8:]
if(t=="AM"):
    if(t1==12):
        res = "00:"+str(t2).zfill(2)+":"+str(t3).zfill(2)
    else:
        res = str(t1).zfill(2)+":"+str(t2).zfill(2)+":"+str(t3).zfill(2)
elif(t=="PM"):
    if(t1==12):
        res = str(t1).zfill(2)+":"+str(t2).zfill(2)+":"+str(t3).zfill(2)
    else:
        res = str(t1+12).zfill(2)+":"+str(t2).zfill(2)+":"+str(t3).zfill(2)

print(res)

