msg = str(input("Enter msg : - "))
k = str(input("Enter key : - "))
#print(len(msg))
rem = len(msg)%len(k)
r = len(k)-rem
for _ in range(0,r):
    msg += 'x'
#print(msg)

final_str = ''
in_li = []
for _ in range(1,len(k)+1):
    #print(str(k[_]))
    index = k.index(str(_))
    in_li += [index]
    #print(index)

i = 0
mi = in_li[i]
final_str = msg[mi]
#print(len(msg))
for _ in range(0,len(msg)-1):
    mi = mi + len(k)
    if mi < len(msg):
        final_str += msg[mi]
        #print(mi)
    else:
        mi = in_li[i+1]
        final_str += msg[mi]
        i = i + 1
print(final_str)

#Enter msg : - attackpostponeduntiltwoam
#Enter key : - 4312567
