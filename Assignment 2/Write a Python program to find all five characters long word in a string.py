import re

txt = input("Enter the string : ")
x = re.findall(r"\b\w{5}\b",txt)
print(x)
if (x):
  print("Yes, the string exist")
  print(x)
else:
  print("No match")