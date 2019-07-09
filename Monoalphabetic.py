def mono():

    plaintext_small = "abcdefghijklmnopqrstuvwxyz"
    #key_small = input("Enter 26 char key for small char: - ")
    plaintext_cap = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    #key_cap = input("Enter 26 char key for cap char: - ")
    key_small = "defghijklmnopqrstuvwxyzabc"
    key_cap = "GHIJKLMNOPQRSTUVWXYZABCEDF"
    leng_small = len(key_small)
    leng_cap = len(key_cap)
    final = ""
    msg = input("Enter msg to encrypt: - ")

    leng = len(msg)
    count = 0
    while count != leng:
        if msg[count].isupper():
            count1 = 0
            while plaintext_cap[count1] != msg[count]:
                count1 = count1 + 1
            final = final + key_cap[count1]

        elif msg[count].islower():
            count1 = 0
            while plaintext_small[count1] != msg[count]:
                count1 = count1 + 1
            final = final + key_small[count1]

        else:
            final = final + msg[count]

        count = count + 1

    return final

final = mono()
print(final)









