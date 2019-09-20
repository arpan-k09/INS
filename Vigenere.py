s=input("enter the msg=")
s1=input("enter the key=")
k=""
for i in range(0,len(s)):
    if s[i].islower():
        k+=chr(((ord(s[i])+ord(s1[i])-97-97)%26)+97)

    elif s[i].isupper():
        k += chr(((ord(s[i]) + ord(s1[i]) - 65 - 65) % 26) + 65)

    else:
        k += s[i]
print(k)
