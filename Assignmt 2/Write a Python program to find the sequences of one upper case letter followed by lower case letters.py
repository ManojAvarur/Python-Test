import re

txt = input("Enter a string : ")
pattern = '[A-Z][a-z]+'
x = re.findall(pattern,txt)
if (x):
  print("Yes, the string exist")
  print(x)
else:
  print("No match")