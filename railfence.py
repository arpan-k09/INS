s = "helloworld"

n = int(input("Enter depth : - "))
de = 2
diff = n - 2
step = 2*diff + de

rem =  len(s)/step

re = len(s)-rem

l = re/step


li = []
m = 0
for _ in range(0,int(l)):
    stri = ""
    for __ in range(0,step):
        stri = stri + s[m]
        m = m + 1
    li = li + [stri]
sir = ""
for _ in range(0,int(rem)):
    sir = sir + s[m]
    m = m + 1
li = li + [sir]

print(li)

