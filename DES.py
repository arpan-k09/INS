def first_ini(msg):
    IPC = [58, 50, 42, 34, 26, 18, 10, 2, 60, 52, 44, 36, 28, 20, 12, 4,62, 54, 46, 38, 30, 22, 14, 6,64,54,48,40,32,24,16,8,57, 49, 41, 33, 25, 17, 9, 1,  59, 51, 43, 35, 27, 19, 11, 3,61, 53, 45, 37, 29, 21, 13, 5,63, 55, 47, 39, 31, 23, 15, 7]
    #print(len(PC1))
    dec = int(msg, 16)
    #print(dec)
    bi = bin(dec)
    #print(bi)
    #print(len(bi))
    bi = bi.lstrip("0b")
    #print(bi)

    if len(bi) != 64:
        bi = '0'+bi
    le = len(IPC)
    final_s = ""
    #count = 0
    for i in range(0,le):
        #print(IPC[i]-1)
        final_s = final_s + str(bi[IPC[i]-1])
        #print(final_s)
    tem = int(final_s, 2)
    h = hex(tem).lstrip('0x')
    return h

def enco(msg):
    l = msg[:8]
    #print(l)
    r = msg[8:]
    print(r)





msg = "675a69675e5a6b5a"
#msg = "ffab213ab98acb42"
in1 = first_ini(msg)
enco(in1)
