a = {"abba", "bbaa", "abbaba"," bbaabb"}

for i in a:
    if i == i[::-1]:
        print(i, "is Palindrome")
    else:
        print(i, "is Not Palindrome")