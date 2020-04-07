Find = []

def Dup():
    global Find
    for i in range((len(Find) - 1)):
        temp = Find[i]
        for i in range(( i + 1),(len(Find))):
            if( temp == Find[i]):
                return temp
                
    return -1

n = int(input("Enter the number of Items you would like to insert : "))

print("Enter ",n," Number of valuee")

for i in range(n):
    ele = int(input())
    Find.append(ele)

print(Find)

sol = Dup()
print("Duplicate Element in the array is : ",sol)