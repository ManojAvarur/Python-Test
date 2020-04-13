fl1 = open('txt1.txt')
fl2 = open('txt2.txt')
for ln1,ln2 in zip(fl1,fl2):
    print(ln1 + ln2)
