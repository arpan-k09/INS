import random
def gcd_com(x, y):

    for i in range(1,min(x,y) + 1):
        if ((x % i == 0) and (y % i == 0)):
            gcd = i
    return gcd

def pri_root(q):
    alpha = 0
    li = []
    for _ in range(1,q):
        if gcd_com(_,q) == 1:
            li = li + [_]
    #print(li)
    for _ in range(1,len(li)):
        temp = set()
        for __ in range(1,len(li)+1):
            val = ((li[_]**__)%q)
            #print(val)
            temp.add(val)
        #print(temp)
        if len(temp) == len(li):
            #return temp
            alpha = li[_]
            break
    return alpha

q = int(input("Enter prime number : - "))
alpha = pri_root(q)
print("Alpha is : - ",alpha)
xa = random.randrange(2,q-1)
print("XA is : - ",xa)
xb = random.randrange(2,q-1)
print("XB is : - ",xb)
ya = (alpha**xa)%q
print("YA is : - ",ya)
yb = (alpha**xb)%q
print("YB is : - ",yb)

k1 = (ya**xb)%q
k2 = (yb**xa)%q
if k1 == k2:
    print("Key value is : - ",k2)
else:
    print("something incorrect")

#Enter prime number : - 23
#Alpha is : -  5
#XA is : -  17
#XB is : -  6
#YA is : -  15
#YB is : -  8
#Key value is : -  13
    
 
