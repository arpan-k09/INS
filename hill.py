def encr(msg,key):

    msg1 = msg
    rem = len(msg1) % 3
    r = 3 - rem

    if rem != 0:
        while r != 0:
            msg1 = msg1 + 'x'
            r = r - 1

    le = len(msg1)
    count = 0
    fi_msg = []

    while count != le:
        st =''
        c1 = 0
        while c1 != 3:
            st = st + msg1[count + c1]
            c1 = c1 + 1

        fi_msg = fi_msg + [st]
        count = count + 3
    #print(fi_msg)


    #print(msg)

    #fi = "abcdefghijklmnopqrstuvwxyz"
    #count = 0
    #print(rem1)

    key_l = len(key)
    co1 = 0
    key_li = []
    while key_l > 0:
        ms = ''
        c = 0
        while c != 3:
            ms = ms + key[co1+c]
            c = c + 1

        key_li = key_li + [ms]
        co1 = co1 + 3
        key_l = key_l - 3

    #print(key_li)

    rem1 = len(fi_msg)
    final_count = 0
    final_str = ''

    while final_count != rem1:
        key_count = 0
        while key_count != 3:
            temp = 0
            sum1 = 0
            while temp != 3:
                #f = ord(key_li[key_count][temp])%97
                #print(f)
                sum1 = sum1 + ((ord(key_li[key_count][temp])%97)*(ord(fi_msg[final_count][temp])%97))
                #chr((ord(key_li[key_count][temp])%65)*(ord(fi_msg[final_count][temp])%65))%26)
                temp = temp + 1
            final_str = final_str + chr((sum1%26)+97)
            key_count = key_count + 1
        final_count = final_count + 1
    print(final_str)

m = "gfg"
#m = "paymoremoney"
key = "hillmagic"
#key = "rrfvsvcct"
encr(m,key)
