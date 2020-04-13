import re 
password = input("Enter a string : ")
flag = 0

if not re.search("[a-z]", password): 
        flag = -1

if not re.search("[A-Z]", password): 
        flag = -1
if not re.search("[0-9]", password): 
        flag = -1
if not re.search("[_]", password): 
        flag = -1
if re.search("[@#$%^&*()\"\'.,:;\\<>{}]", password): 
        flag = -1
if re.search("\s", password): 
        flag = -1
  
if flag ==-1: 
    print("Not a Valid Password")
else:
    print("Valid Password") 
    