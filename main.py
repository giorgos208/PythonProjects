
x = (input("Enter a word: "))

while (x != ""):
    flag = True
    N = len(x)
    for i in range(N//2):

        if (x[i]!=x[N-i-1]): flag = False
    if (flag): print("palindrome")
    else: print("no palindrome")
    x = (input("Enter a word: "))




