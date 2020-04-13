k = 1
SortList = []

def Ggnome():
    global SortList
    global k
    while True:
        if SortList[k] < SortList[k-1]:
            swap()
            dec()
        else:
            inc()
        
        if k == (len(SortList)):
            break
        
    print("Sorted List : ",SortList)
    

def dec():
    global k
    if not k == 1:
        k = k - 1
    return

def inc():
    global k
    global SortList
    leg = (len(SortList))
    if not k == leg:
        k = k + 1
    return
 
def swap():
    global SortList
    global k
    temp = SortList[k]
    SortList[k] = SortList[k - 1]
    SortList[k - 1] = temp



n = int(input("Enter the number of Items you would like to insert : "))

print("Enter ",n," Number of valuee")

for i in range(n):
    ele = int(input())
    SortList.append(ele)

print("Unsorted List : ",SortList)

Ggnome()       

        


