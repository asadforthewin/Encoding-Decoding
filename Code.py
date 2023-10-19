import random
random_str = "hah" , "gao", "qrw", "aab", "ava", "abc", "ave", "aey","rye"

x = input("enter your message: ")
msg = x.split(" ")
coding = input("Press 1 for coding and 0 for decoding")
coding= True if (coding == "1") else False
if (coding):

    words_direc = []
    for y in msg:
        if (len(y)>=3):
            var = random.choice(random_str) + y[1:len(y)] + y[0] +random.choice(random_str)
            words_direc.append(var)
        else:
            words_direc.append(y[::-1])

    print(" " . join(words_direc))

else:
    words_direc = []
    for y in msg:
        if (len(y) >= 3):
            var =y[3:-3]
            var = var[-1] + var[:-1]
            words_direc.append(var)
        else:
            words_direc.append(y[::-1])

    print(" ".join(words_direc))