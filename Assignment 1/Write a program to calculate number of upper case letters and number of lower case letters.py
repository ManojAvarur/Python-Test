def check(Str):
    ucount = 0
    lcount = 0
    for i in range(len(Str)):
        if Str[i].isupper():
            ucount += 1
        elif Str[i].islower():
            lcount += 1
    
    print("\nUpper Letter Count = ",ucount)
    print("\nLower Letter Count = ",lcount,"\n")

Str = input("Enter the String : ")
check(Str)


