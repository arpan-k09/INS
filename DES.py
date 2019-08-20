def he2bin(msg):
    hex = {"0": "0000", "1": "0001", "2": "0010", "3": "0011", "4": "0100", "5": "0101", "6": "0110", "7": "0111",
           "8": "1000", "9": "1001", "a": "1010", "b": "1011", "c": "1100", "d": "1101", "e": "1110", "f": "1111"}
    f = ""
    l = len(msg)
    for i in range(0, l):
        f = f + hex[msg[i]]
    # print(f)
    return f


def binar2he(msg):
    bi = {"0000": "0", "0001": "1", "0010": "2", "0011": "3", "0100": "4", "0101": "5", "0110": "6", "0111": "7",
          "1000": "8", "1001": "9", "1010": "a", "1011": "b", "1100": "c", "1101": "d", "1110": "e", "1111": "f"}
    f = ""
    lis = []
    count = 0
    l = len(msg)
    if l == 64:
        for i in range(0, 16):
            lis = lis + [msg[count:count + 4]]
            f = f + bi[lis[i]]
            count = count + 4
    elif l == 56:
        for i in range(0, 14):
            lis = lis + [msg[count:count + 4]]
            f = f + bi[lis[i]]
            count = count + 4
    elif l == 48:
        for i in range(0, 12):
            lis = lis + [msg[count:count + 4]]
            f = f + bi[lis[i]]
            count = count + 4
    elif l == 32:
        for i in range(0, 8):
            lis = lis + [msg[count:count + 4]]
            f = f + bi[lis[i]]
            count = count + 4

    # print(lis)
    # print(f)

    return f


def first_ini(msg):
    IPC = [58, 50, 42, 34, 26, 18, 10, 2, 60, 52, 44, 36, 28, 20, 12, 4, 62, 54, 46, 38, 30, 22, 14, 6, 64, 56, 48, 40,
           32, 24, 16, 8, 57, 49, 41, 33, 25, 17, 9, 1, 59, 51, 43, 35, 27, 19, 11, 3, 61, 53, 45, 37, 29, 21, 13, 5,
           63, 55, 47, 39, 31, 23, 15, 7]

    bi = he2bin(msg)
    # print(bi)
    le = len(IPC)
    final_s = ""
    # count = 0
    for i in range(0, le):
        # print(IPC[i]-1)
        final_s = final_s + str(bi[IPC[i] - 1])
        # print(final_s)
    # print(final_s)

    h = binar2he(final_s)
    print("Initial permutation : - ", h)
    return h


def enco(msg):
    # r = msg

    # print(r)
    final_s = msg
    # final_s = he2bin(r)
    # le = len(final_s)

    # print(final_s)

    # count = 0
    en_tab = [32, 1, 2, 3, 4, 5, 4, 5, 6, 7, 8, 9, 8, 9, 10, 11, 12, 13, 12, 13, 14, 15, 16, 17, 16, 17, 18, 19, 20, 21,
              20, 21, 22, 23, 24, 25, 24, 25, 26, 27, 28, 29, 28, 29, 30, 31, 32, 1]
    l_f = len(en_tab)
    ret = ""
    for i in range(0, l_f):
        ret = ret + final_s[en_tab[i] - 1]
    return ret


def xor(first, second):
    fi_s = ""
    len1 = len(first)
    # print(first)
    # print(second)
    for i in range(0, len1):
        # print(first[i]," ",second[i])
        if (first[i] == second[i]):
            fi_s = fi_s + '0'
        elif (first[i] != second[i]):
            fi_s = fi_s + '1'
        # print(fi_s)
    # print(fi_s)
    return fi_s


def round(r):
    m = []
    if r == 1:
        m = [[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
             [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
             [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
             [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]]
    elif r == 2:
        m = [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
             [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
             [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
             [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]]
    elif r == 3:
        m = [[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
             [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
             [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
             [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]]
    elif r == 4:
        m = [[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
             [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
             [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
             [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]]
    elif r == 5:
        m = [[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
             [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
             [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
             [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]]
    elif r == 6:
        m = [[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
             [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
             [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
             [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]]
    elif r == 7:
        m = [[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
             [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
             [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
             [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]]
    elif r == 8:
        m = [[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
             [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
             [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
             [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]]
    return m


def s_box(x):
    he = {"0000": "0", "0001": "1", "0010": "2", "0011": "3", "0100": "4", "0101": "5", "0110": "6", "0111": "7",
          "1000": "8", "1001": "9", "1010": "10", "1011": "11", "1100": "12", "1101": "13", "1110": "14", "1111": "15"}
    bi = {"0": "0", "1": "1", "2": "2", "3": "3", "4": "4", "5": "5", "6": "6", "7": "7",
          "8": "8", "9": "9", "10": "a", "11": "b", "12": "c", "13": "d", "14": "e", "15": "f"}
    row = {"00": 0, "01": 1, "10": 2, "11": 3}

    # s_li = ['s1','s2','s3','s4','s5','s6','s7','s8']
    # lis = [x[0:7],x[7:13],x[13:19],]
    count = 0
    lis = []
    for i in range(0, 8):
        lis = lis + [x[count:count + 6]]
        count = count + 6
    # print(lis)
    final_str = ""

    ro = 1
    for i in range(0, 8):
        s = lis[i]
        va = s[0] + s[5]
        # print(row[va])
        m = round(ro)
        # print(ind)
        index = int(row[va])
        # print(index)
        val = int(he[s[1:5]])
        final_str = final_str + str(bi[str(m[index][val])])
        ro = ro + 1
    # print(final_str)
    return he2bin(final_str)


def aft_s_per(msg):
    m = [16, 7, 20, 21, 29, 12, 28, 17, 1, 15, 23, 26, 5, 18, 31, 10, 2, 8, 24, 14, 32, 27, 3, 9, 19, 13, 30, 6, 22, 11,
         4, 25]
    l = len(m)
    final_str = ""
    for i in range(0, l):
        final_str = final_str + msg[m[i] - 1]
    return final_str


def key_perm(msg):
    PC1 = [57, 49, 41, 33, 25, 17, 9,
           1, 58, 50, 42, 34, 26, 18,
           10, 2, 59, 51, 43, 35, 27,
           19, 11, 3, 60, 52, 44, 36,
           63, 55, 47, 39, 31, 23, 15,
           7, 62, 54, 46, 38, 30, 22,
           14, 6, 61, 53, 45, 37, 29,
           21, 13, 5, 28, 20, 12, 4]

    bi = he2bin(msg)
    # print(bi)
    le = len(PC1)
    final_s = ""
    # count = 0
    for i in range(0, le):
        # print(IPC[i]-1)
        final_s = final_s + str(bi[PC1[i] - 1])
        # print(final_s)
    # print(final_s)

    h = binar2he(final_s)
    # print(h)
    return h


def round_key(msg):
    round = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]

    key = key_perm(msg)

    # print(key)
    key_list = []

    key = he2bin(key)
    for i in range(0, 16):
        final_str = ""

        l = ""
        r = ""
        if round[i] == 1:

            l_in = key[0:28]
            r_in = key[28:56]
            # print(len(l_in)," ",len(r_in))
            l = l_in[1:] + l_in[0]
            r = r_in[1:] + r_in[0]

            final_str = l + r
            # print(len(final_str))
            key = final_str
            key_list = key_list + [binar2he(final_str)]
        elif round[i] == 2:
            l_in = key[0:28]
            r_in = key[28:56]
            # print(len(l_in)," ",len(r_in))
            l = l_in[2:] + l_in[0] + l_in[1]
            r = r_in[2:] + r_in[0] + r_in[1]

            final_str = l + r
            # print(len(final_str))
            key = final_str
            key_list = key_list + [binar2he(final_str)]

    print(key_list)
    return key_list


def key_gen(msg):
    PC2 = [14, 17, 11, 24, 1, 5,
           3, 28, 15, 6, 21, 10,
           23, 19, 12, 4, 26, 8,
           16, 7, 27, 20, 13, 2,
           41, 52, 31, 37, 47, 55,
           30, 40, 51, 45, 33, 48,
           44, 49, 39, 56, 34, 53,
           46, 42, 50, 36, 29, 32]

    bi = he2bin(msg)
    # print(bi)
    le = len(PC2)
    final_s = ""
    # count = 0
    for i in range(0, le):
        # print(IPC[i]-1)
        final_s = final_s + str(bi[PC2[i] - 1])
        # print(final_s)
    # print(final_s)

    h = binar2he(final_s)
    # print(h)
    return h


def final_inv_init(msg):
    INV = [40, 8, 48, 16, 56, 24, 64, 32,
           39, 7, 47, 15, 55, 23, 63, 31,
           38, 6, 46, 14, 54, 22, 62, 30,
           37, 5, 45, 13, 53, 21, 61, 29,
           36, 4, 44, 12, 52, 20, 60, 28,
           35, 3, 43, 11, 51, 19, 59, 27,
           34, 2, 42, 10, 50, 18, 58, 26,
           33, 1, 41, 9, 49, 17, 57, 25]

    bi = he2bin(msg)
    # print(bi)
    le = len(INV)
    final_s = ""
    # count = 0
    for i in range(0, le):
        # print(IPC[i]-1)
        final_s = final_s + str(bi[INV[i] - 1])
        # print(final_s)
    # print(final_s)

    h = binar2he(final_s)
    # print(h)
    return h


def final_main(plain, key):
    in1 = he2bin(first_ini(plain))

    l_init = in1[0:32]
    # print("p : - ",l_init)
    r_init = in1[32:64]

    final_list = []
    key_list = round_key(key)
    # print(key_list)
    for i in range(0, 16):
        # print(key_gen(key_list[i]))
        final_key = he2bin(key_gen(key_list[i]))

        finsl_str = ""
        enc = enco(r_init)
        # print(binar2he(enc))
        # print(enc)

        x = xor(enc, final_key)
        # print(final_key)
        m = s_box(x)
        # print(m)
        # print(m)
        f = aft_s_per(m)
        # print(l_init)
        # print(f)
        # print("f : - ",f,"l_init : - ",l_init)
        c = xor(l_init, f)
        # print(c)
        finsl_str = r_init + c
        l_init = r_init
        r_init = c
        final_list = final_list + [binar2he(finsl_str)]

    #print(final_list)
    swap = final_list[len(final_list) - 1]
    final_swap = swap[8:16] + swap[0:8]
    print(final_inv_init(final_swap))


# main message and key
msg = "123456abcd132536"
key = 'aabb09182736ccdd'

final_main(msg, key)
