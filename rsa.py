def gcd_com(x, y):

    for i in range(1,min(x,y) + 1):
        if ((x % i == 0) and (y % i == 0)):
            gcd = i
    return gcd


#print(e)

def find_e(fin):
    e = 0
    for i in range(2, fin):
        if gcd_com(i, fin) == 1:
            e = i
            break
    return e

def find_d(fin,e):
    for i in range(1, 100000):
        d = int((1 + i * fin) / e)
        if (d < fin and d > 0 and (d * e) % fin == 1):
            break
        else:
            pass

    return d


p = int(input("Enter p value : - "))
q = int(input("Enter q value : - "))
m = int(input(("Enter msg : - ")))
n = p * q
fin = (p - 1) * (q - 1)
e = find_e(fin)
d = find_d(fin,e)
print("encryption is ")
c=(m**e)%n
print(c)
print("decryption is")
M=(c**d)%n
print(M)
