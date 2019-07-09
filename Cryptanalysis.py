plain_small = "abcdefghijklmnopqrstuvwxyz"
plain_cap = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
key_small = "defghijklmnopqrstuvwxyzabc"
key_cap = "GHIJKLMNOPQRSTUVWXYZABCEDF"

#name = input("Enter msg : - ")
name = "a paragraph is a series of sentences that are organized and coherent, and are all related to a single topic. almost every piece of writing you do that is longer than a few sentences should be organized into paragraphs. this is because paragraphs show a reader where the subdivisions of an essay begin and end, and thus help the reader see the organization of the essay and grasp its main points."
msg = ""
leng_s = len(plain_small)
leng = len(name)
count = 0

while(count != leng):
    if(name[count].isupper()):
        count1 = 0

        while (name[count] != plain_cap[count1]):

            count1 = count1 + 1
        msg = msg + key_cap[count1]

    elif(name[count].islower()):
        count2 = 0

        while (name[count] != plain_small[count2]):

            count2 = count2 + 1
        msg = msg + key_small[count2]
    else:
        msg = msg + name[count]

    count = count + 1

print(msg)


freq = {}
test_str = msg
my_list = []
leng = len(test_str)
count = 0
while(count != leng):
    my_list = my_list + [test_str[count]]
    count = count + 1


#my_list =[1, 1, 1, 5, 5, 3, 1, 3, 3, 1, 4, 4, 4, 2, 2, 2, 2]
for items in my_list:
    freq[items] = my_list.count(items)

freq.pop(" ")
#req.pop("-")
freq.pop(",")
freq.pop(".")


decy_small = ""
decy_cap = ""

s = [(k, freq[k]) for k in sorted(freq, key = freq.get, reverse=True)]
for k, v in s:
    if k.isupper():
        decy_cap = decy_cap + k
    elif k.islower():
        decy_small = decy_small + k
print(decy_small)
final_len = len(test_str)
final_str = "etaoinshrdlucmwfgypbvkjxqz"
out = ""

count_f = 0
while count_f != final_len:
    count_in = 0
    if test_str[count_f].islower():
        while test_str[count_f] !=  decy_small[count_in]:
            count_in = count_in + 1

        out = out + final_str[count_in]
    else:
        out = out + test_str[count_f]
    count_f = count_f + 1
print(out)