# What is an Armstrong Number?
"""
    A number of 'n' digits which is equal to the sum of 'nth' power of its digits is called Armstrong Number

    Eg. num = 5; n=1; 5^1=5; '5' is an Armstrong number!
    Eg. num = 43; n=2; 4^2 + 3^2 != 43; '43' is not an Armstrong number...
    Eg. num=157; n=3; 1^3 + 5^3 + 7^3 != 157; '157' is not an Armstrong number...
    Eg. num=7827; n=4; 7^4 + 8^4 + 2^4 + 7^4 != 7827; '7827' is not an Armstrong number...

    Is 1634 an Armstrong number?
"""

#Python program to print Armstrong numbers from 0 to input range:

irange = int(input("Print Armstrong Numbers from 0 to *enter_number*: "))

#loop that prints the Armstrong Numbers in the input range
for numbers in range(0, irange+1):
    numbers = str(numbers)
    num = [int(x) for x in str(numbers)] #converting the number into a list
    total = 0 #initialising total variable

    #loop that gets the nth power of each element in the list
    for i in range(0,len(num)):
        n = len(numbers)
        num[i] = num[i]**n
    
    #loop that finds the sum of all elements in the list
    for ele in range(0, len(num)):
        total = total + num[ele]
    
    # A number of 'n' digits which is equal to the sum of 'nth' power of its digits is called Armstrong Number
    if total==int(numbers):
        print(total)
