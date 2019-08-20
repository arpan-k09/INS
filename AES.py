def he2bin(msg):
    hex={"0":"0000","1":"0001","2":"0010","3":"0011","4":"0100","5":"0101","6":"0110","7":"0111","8":"1000","9":"1001","a":"1010","b":"1011","c":"1100","d":"1101","e":"1110","f":"1111"}
    f = ""
    l = len(msg)
    for i in range(0,l):
        f = f + hex[msg[i]]
    #print(f)
    return f



def binar2he(msg):
    bi = {"0000":"0","0001":"1","0010":"2","0011":"3","0100":"4","0101":"5","0110":"6","0111":"7","1000":"8","1001":"9","1010":"a","1011":"b","1100":"c","1101":"d","1110":"e","1111":"f"}
    f = ""
    lis = []
    #count = 0
    l = len(msg)

    count1 = 0
    i = 0
    while count1 != l:

        lis = lis + [msg[count1:count1 + 4]]
        f = f + bi[lis[i]]
        i = i + 1
        count1 = count1 + 4

    #print(lis)
    # print(f)
    return f



def s_box(x):
    he = {"0000":"0",  "0001":"1",  "0010":"2",  "0011":"3",  "0100":"4",  "0101":"5", "0110":"6", "0111": "7",
            "1000":"8","1001": "9" , "1010":"10", "1011":"11", "1100": "12" , "1101":"13",  "1110":"14", "1111": "15"}
    bi = {"0": "0", "1": "1", "2": "2", "3": "3", "4": "4", "5": "5", "6": "6", "7": "7",
          "8": "8", "9": "9", "a":"10", "b":"11", "c":"12", "d":"13", "e":"14", "f":"15"}



    s_b = [["63", "7c", "77", "7b", "f2", "6b", "6f", "c5", "30", "01", "67", "2b", "fe", "d7", "ab", "76"],
           ["ca", "82", "c9", "7d", "fa", "59", "47", "f0", "ad", "d4", "a2", "af", "9c", "a4", "72", "c0"],
           ["b7", "fd", "93", "26", "36", "3f", "f7", "cc", "34", "a5", "e5", "f1", "71", "d8", "31", "15"],
           ["04", "c7", "23", "c3", "18", "96", "05", "9a", "07", "12", "80", "e2", "eb", "27", "b2", "75"],
           ["09", "83", "2c", "1a", "1b", "6e", "5a", "a0", "52", "3b", "d6", "b3", "29", "e3", "2f", "84"],
           ["53", "d1", "00", "ed", "20", "fc", "b1", "5b", "6a", "cb", "be", "39", "4a", "4c", "58", "cf"],
           ["d0", "ef", "aa", "fb", "43", "4d", "33", "85", "45", "f9", "02", "7f", "50", "3c", "9f", "a8"],
           ["51", "a3", "40", "8f", "92", "9d", "38", "f5", "bc", "b6", "da", "21", "10", "ff", "f3", "d2"],
           ["cd", "0c", "13", "ec", "5f", "97", "44", "17", "c4", "a7", "7e", "3d", "64", "5d", "19", "73"],
           ["60", "81", "4f", "dc", "22", "2a", "90", "88", "46", "ee", "b8", "14", "de", "5e", "0b", "db"],
           ["e0", "32", "3a", "0a", "49", "06", "24", "5c", "c2", "d3", "ac", "62", "91", "95", "e4", "79"],
           ["e7", "c8", "37", "6d", "8d", "d5", "4e", "a9", "6c", "56", "f4", "ea", "65", "7a", "ae", "08"],
           ["ba", "78", "25", "2e", "1c", "a6", "b4", "c6", "e8", "dd", "74", "1f", "4b", "bd", "8b", "8a"],
           ["70", "3e", "b5", "66", "48", "03", "f6", "0e", "61", "35", "57", "b9", "86", "c1", "1d", "9e"],
           ["e1", "f8", "98", "11", "69", "d9", "8e", "94", "9b", "1e", "87", "e9", "ce", "55", "28", "df"],
           ["8c", "a1", "89", "0d", "bf", "e6", "42", "68", "41", "99", "2d", "0f", "b0", "54", "bb", "16"]
    ]
    s = s_b[int(bi[x[0]])][int(bi[x[1]])]
    #print(s)
    return s


s_box("20")

def xor(first,second):
    fi_s = ""
    len1 = len(first)
    #print(first)
    #print(second)
    for i in range(0,len1):
        #print(first[i]," ",second[i])
        if (first[i]==second[i]):
            fi_s = fi_s + '0'
        elif(first[i]!=second[i]):
            fi_s = fi_s + '1'
        #print(fi_s)
    #print(fi_s)
    return fi_s




def key(k,r):


    #print(he2bin(k[0][0]))
    #print(he2bin(rcon[0]))
    #print(mid_key)
    #print(he2bin(col[0]))

    #print(mid_key1)
    #print(r)
    final_key = []
    #rcon = [["01","00","00","00"],["02","00","00","00"],["04""00","00","00"],["08","00","00","00"],["10","00","00","00"],["20","00","00","00"],["40","00","00","00"],["80","00","00","00"],["1b","00","00","00"],["36""00","00","00"]]
    #rcon = ["01", "00", "00", "00"]
    rcon = r
    for i in range(0,4):
        if i == 0:
            first_col = []
            temp = k[3]

            for i in range(1, len(temp)):
                first_col = first_col + [temp[i]]
            first_col = first_col + [temp[0]]
            # print(first_col)
            col = []

            for i in range(0, len(first_col)):
                col = col + [s_box(first_col[i])]
            # print(col)

            key1 = []
            for p in range(0,4):
                mid_key = xor(he2bin(k[0][p]), he2bin(r[p]))
                mid_key1 = xor(mid_key, he2bin(col[p]))
                key1 = key1 + [str(binar2he(mid_key1))]


            #print(key1)
            final_key = final_key + [key1]

        elif i > 0:
            first_col = []

            for p in range(0,4):
                mid_key = xor(he2bin(k[i][p]),he2bin(final_key[i-1][p]))
                first_col = first_col + [str(binar2he(mid_key))]

            final_key = final_key + [first_col]
    return final_key
    #print(final_key)

def coltorow(k):
    row = []
    for i in range(0,4):
        col = []
        for j in range(0,4):
            col = col + [k[j][i]]
        row = row + [col]
    return (row)

def rowtocol(k):
    col = []
    for i in range(0,4):
        row = []
        for j in range(0,4):
            row = row + [k[j][i]]
        col = col + [row]
    return (col)



def addround(pt,k):
    #k = coltorow(k)

    row = []
    for i in range(0, 4):
        col = []
        for j in range(0, 4):
            x = xor(he2bin(k[i][j]),he2bin(pt[i][j]))
            col = col + [binar2he(x)]
        row = row + [col]

    return (coltorow(row))

def subByte(k):
    row = []
    for i in range(0,4):
        col = []
        for j in range(0,4):
            col = col + [s_box(k[i][j])]
        row = row + [col]
    return (row)


def shiftrow(sb):
    sr = []

    sr = sr + [sb[0]]
    #second = []
    second = [sb[1][1]] + [sb[1][2]] + [sb[1][3]] + [sb[1][0]]
    sr = sr + [second]

    third = [sb[2][2]] + [sb[2][3]] + [sb[2][0]] + [sb[2][1]]
    sr = sr + [third]

    four = [sb[3][3]] + [sb[3][0]] + [sb[3][1]] + [sb[3][2]]
    sr = sr + [four]

    return sr


def mix_2(val):

    bi = he2bin(val[0])+he2bin(val[1])
    fin = ''
    if bi[0] == '1':
        bi = bi[1:len(bi)] + '0'
        fin = xor(bi,he2bin('1b'))

    elif bi[0] == '0':
        fin = bi[1:len(bi)] + '0'

    return fin
#mix_2('41')

def mix_3(val):

    bi = mix_2(val)
    #print(bi)
    fin = xor(bi,he2bin(val))
    return fin
#mix_3('bf')

#g = ['d4', 'bf', '5d', '30']
def first_row(row):
    #print(mix_2(row[0]))
    #print(mix_3(row[1]))

    first_two = xor(mix_2(row[0]),mix_3(row[1]))
    #print(first_two)
    seconde_two = xor(he2bin(row[2]), he2bin(row[3]))
    fin = xor(first_two,seconde_two)
    return binar2he(fin)
    #fin = xor(first_two, seconde_two)
    #print(fin)
    #x1 = row[0]
    #x2 = row[1]
    #first_two = xor(mix_2(x1),mix_3(x2))
    #print(first_two)
    #print(len(mix_2(x1)))
    #print(len(mix_3(x2)))
    #x3 = row[2]
    #x4 = row[3]
#first_row(g)


def second_row(row):
    first_two = xor(he2bin(row[0]),mix_2(row[1]))
    second_two = xor(mix_3(row[2]),he2bin(row[3]))
    fin = xor(first_two,second_two)
    return binar2he(fin)
#second_row(g)

def third_row(row):
    first_two = xor(he2bin(row[0]),he2bin(row[1]))
    second_two = xor(mix_3(row[3]),mix_2(row[2]))
    fin = xor(first_two,second_two)
    return binar2he(fin)
#third_row(g)

def fourth_row(row):
    first_two = xor(mix_3(row[0]),he2bin(row[1]))
    second_two = xor(mix_2(row[3]),he2bin(row[2]))
    fin = xor(first_two,second_two)
    return binar2he(fin)
#fourth_row(g)



def mix_col(sr):
    final_row = []
    for i in range(0,4):
        row = [first_row(sr[i])] + [second_row(sr[i])] + [third_row(sr[i])] + [fourth_row(sr[i])]
        final_row = final_row + [row]
    return final_row


rcon = [["01","00","00","00"],["02","00","00","00"],["04","00","00","00"],["08","00","00","00"],["10","00","00","00"],["20","00","00","00"],["40","00","00","00"],["80","00","00","00"],["1b","00","00","00"],["36","00","00","00"]]

def main_fun(pt,k):
    ar = addround(pt,k)
    #print(ar)
    sb = subByte(ar)
    #print(sb)
    sr = shiftrow(sb)
    #print(sr)
    mx = mix_col(rowtocol(sr))
    #print(mx)
    ar = addround(mx,key(k,rcon[0]))
    #print(ar)
    k = key(k,rcon[0])

    #print(addround(mx,ke))
    #r = 1
    for i in range(1,9):

        #print("\n")
        ke = key(k,rcon[i])
        k = ke
        #ar = addround(mx, k)
        #print(ar)
        sb = subByte(ar)
        #print(sb)
        sr = shiftrow(sb)
        #print(sr)

        mx = mix_col(rowtocol(sr))
        #print(mx)
        ar = addround(mx,k)
        #print(ar)
        #print("\n",k)
        #ke = key(k,r)
        #r = r + 1

    sb = subByte(ar)
    #print(sb)
    sr = rowtocol(shiftrow(sb))
    #print(sr)
    #mx = mix_col(sr)
    ke = key(k,rcon[9])
    ar = addround(sr, ke)

    print(ar)


#k = [["0f","15","71","c9"],["47","d9","e8","59"],["0c","b7","ad","d6"],["af","7f","67","98"]]
k = [["54","68","61","74"],["73","20","6d","79"],["20","4b","75","6e"],["67","20","46","75"]]
#pt = [["32","43","f6","a8"],["88","5a","30","8d"],["31","31","98","a2"],["e0","37","07","34"]]
pt = [["54","77","6f","20"],["4f","6e","65","20"],["4e","69","6e","65"],["20","54","77","6f"]]

main_fun(pt,k)
