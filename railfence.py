s=input("enter the msg : - ")
k=int(input("enter the key : - "))
# s="helloworld"
# k=4
l=[[] for j in range(k)]
flag=0
for _ in range(0,len(s),(k-1)*2):
    for __ in range(0,k):
        if(_+__>=len(s)):
            flag=1
            break
        l[__].append(s[__+_])
    if(flag==1):
        break
    else:
        pass
    p=k-1
    for ___ in range(k,2*k-2):
        if(_+___>=len(s)):
            flag=1
            break
        l[p-1].append(s[___+_])
        p=p-1
        
    if(flag==1):
        break
    else:
        pass
e=""
for _ in range(len(l)):
    for __ in range(len(l[_])):
        e+=str(l[_][__])
            
print(e)
