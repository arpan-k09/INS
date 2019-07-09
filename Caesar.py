str = "abcd"
key = 25

result = ""
count1 = 0
leng1 = len(str)
while count1 != leng1:
    char = str[count1]

    # Encrypt uppercase characters
    if (char.isupper()):
        result += chr((ord(char) + key - 65) % 26 + 65)

        # Encrypt lowercase characters
    elif (char.islower()):
        result += chr((ord(char) + key - 97) % 26 + 97)

    else:
        result += char

    count1 = count1 + 1

print(result)
leng = len(result)
count = 0
result1 = ""

while count != leng:
    char = result[count]

    # For Uppercase
    if (char.isupper()):
        result1 += chr((ord(char) - key - 65) % 26 + 65)

        # Encrypt lowercase characters
    elif (char.islower()):
        result1 += chr((ord(char) - key - 97) % 26 + 97)

    else:
        result1 += char

    count = count + 1

print(result1)






