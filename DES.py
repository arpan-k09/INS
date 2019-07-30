def he(msg):
    hex={"0":"0000","1":"0001","2":"0010","3":"0011","4":"0100","5":"0101","6":"0110","7":"0111","8":"1000","9":"1001","a":"1010","b":"1011","c":"1100","d":"1101","e":"1110","f":"1111"}
    f = ""
    l = len(msg)
    for i in range(0,l):
        f = f + hex[msg[i]]
    #print(f)
    return f



def first_ini(msg):
    IPC = [58, 50, 42, 34, 26, 18, 10, 2, 60, 52, 44, 36, 28, 20, 12, 4,62, 54, 46, 38, 30, 22, 14, 6,64,54,48,40,32,24,16,8,57, 49, 41, 33, 25, 17, 9, 1,  59, 51, 43, 35, 27, 19, 11, 3,61, 53, 45, 37, 29, 21, 13, 5,63, 55, 47, 39, 31, 23, 15, 7]
    #print(len(PC1))
    #dec = int(msg, 16)
    #print(dec)
    #bi = bin(dec)
    #print(bi)
    #print(len(bi))
    #bi = bi.lstrip("0b")
    #print(bi)
    #if len(bi) != 64:
    #    bi = '0'+bi
    le = len(msg)
    bi = he(msg)

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
    #print(r)
    final_s = he(r)
    le = len(r)

    #print(final_s)

    count = 0
    en_tab = [32,1,2,3,4,5,4,5,6,7,8,9,8,9,10,11,12,13,12,13,14,15,16,17,16,17,18,19,20,21,20,21,22,23,24,25,24,25,26,27,28,29,28,29,30,31,32,1]
    l_f = len(en_tab)
    ret = ""
    for i in range(0,l_f):
        ret = ret + final_s[en_tab[i]-1]
    return ret


def xor(first,second):
    fi_s = ""
    l = len(first)
    for i in range(0,l):
        if (first[i]=='0' and second[i]=='0'):
            fi_s = fi_s + '0'
        elif (first[i]=='1' and second[i]=='1'):
            fi_s = fi_s + '0'
        elif (first[i]=='0' and second[i]=='1'):
            fi_s = fi_s + '1'
        elif (first[i]=='1' and second[i]=='0'):
            fi_s = fi_s + '1'
    return fi_s




msg = "675a69675e5a6b5a"
#msg = "ffab213ab98acb42"
#getting initial per.....................
in1 = first_ini(msg)


s = "20ba134cdf35"
s = he(s)
b = enco(in1)
x = xor(b,s)
print(x)
