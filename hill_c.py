def encr(msg,key):
    le = len(msg)
    rem = le % 3
    r = 3 - rem
    if rem != 0:
        while r != 0:
            msg = msg + 'x'
            r = r - 1
    #print(msg)

    #fi = "abcdefghijklmnopqrstuvwxyz"
    #count = 0
    rem1 = len(msg)
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

    print(key_li)
    #while rem1 != 0:
     #   count = 0
      #  while


       # rem1 = rem1 - 3


m = "meet"
key = "abcdefghi"
encr(m,key)

