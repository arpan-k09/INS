def matrix(key):
    matrix = []
    for e in key.lower():
        if e not in matrix:
            matrix.append(e)
    alphabet = "abcdefghiklmnopqrstuvwxyz"

    for e in alphabet:
        if e not in matrix:
            matrix.append(e)

    leng = len(matrix)
    mat = []
    count = 0
    i = 0
    while count < 5:
        a = []
        count2 = 0

        while count2 < 5:
            a = a +  [matrix[i]]
            i = i + 1
            count2 = count2 + 1
        mat = mat + [a]

        count = count + 1

    return mat
#print(matrix("arpankorat"))


def spl(message_original):
    message = []
    for e in message_original:
        message.append(e)

    for unused in range(len(message)):
        if " " in message:
            message.remove(" ")

    i = 0
    for e in range(int(len(message) / 2)):
        if message[i] == message[i + 1]:
            if message[i] == 'x':
                message.insert (i + 1,'y')
            else:
                message.insert(i + 1, 'x')
        i = i + 2

    if len(message) % 2 == 1:
        if message[len(message)-1] == 'x':
            message.append('y')
        else:
            message.append("x")

    i = 0
    new = []
    for x in range(1, int(len(message) / 2 + 1)):
        new.append(message[i: i + 2])
        i = i + 2
    return new

#print(spl("riddhi chodvadiya"))


def fp(key_matrix, letter):
    x = y = 0
    for i in range(5):
        for j in range(5):
            if key_matrix[i][j] == letter:
                x = i
                y = j

    return x, y


def encrypt(message):
    message = spl(message)
    print(message)
    #print(message)
    key_matrix = matrix("textile")
    cipher = []
    for e in message:
        a = e[0]
        b = e[1]
        if e[0] == 'j':
            a = 'i'
        elif e[1] == 'j':
            b = 'i'
        p1, q1 = fp(key_matrix, a)
        p2, q2 = fp(key_matrix, b)
        if p1 == p2:
            if q1 == 4:
                q1 = -1
            if q2 == 4:
                q2 = -1
            cipher.append(key_matrix[p1][q1 + 1])
            cipher.append(key_matrix[p1][q2 + 1])
        elif q1 == q2:
            if p1 == 4:
                p1 = -1;
            if p2 == 4:
                p2 = -1;
            cipher.append(key_matrix[p1 + 1][q1])
            cipher.append(key_matrix[p2 + 1][q2])
        else:
            cipher.append(key_matrix[p1][q2])
            cipher.append(key_matrix[p2][q1])
    return cipher

e = encrypt("committee")
leng = len(e)
co = 0
st = ""
while co != leng:

    st = st + e[co]
    co = co + 1

print(st)