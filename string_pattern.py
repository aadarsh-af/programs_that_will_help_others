str1 = input("Type Something: ")
length = len(str1)
for rows in range(0,length):
    for cols in range(0,rows+1):
        print(str1[cols],end='')
    print()
