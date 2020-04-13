fileOpen = open('txt3.txt')
removed = [",", "\n"]
txt = ""
max = []

for i in fileOpen:
    txt += i
    
print("\n\nString is : \n",txt)

for i in range(len(removed)):
    txt = txt.replace(removed[i],"")


txt = txt.split(' ')

#print(txt)

for i in txt:
    max.append(len(i)) 

max = sorted(max)

for i in txt:
    if max[len(max) - 1] == len(i):
        print("\n\nLongest word is :",i,"\n\n")