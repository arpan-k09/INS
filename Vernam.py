msg = input("Enter msg : - ")
key = input("Enter key : - ")
final_str = " "
if len(msg)==len(key):
    for i in range(len(msg)):
        sum = (ord(msg[i])-97)+(ord(key[i])-97)

        if sum >= 26:
            sum = (sum%26)+97

            final_str += chr(sum)
        else:
            sum = sum+97
            final_str += chr(sum)
print(final_str)
