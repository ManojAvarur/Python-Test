def anagrams(s1 , s2):
    str1 = "\nSting is anagram"
    str2 = "\nSting is not a anagram"
    if( sorted(s1) == sorted(s2) ):
        return str1
    else:
        return str2


s1 = input("Enter string 1 : ")
s2 = input("\nEnter string 2 : ")
result = anagrams(s1 , s2)
print(result)