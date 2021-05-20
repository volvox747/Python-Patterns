
# todo                                                     1. PRINT THE ONES,TENS,THOUSANDS

from number_level_2 import sum_fn


num=input("Enter a number: ")
for i in range(1,len(num)):
    ans=int(num)//10**i
    print("No of digits: ",ans)

# ! OUTPUT: 
#     * Enter a number:567890
#     ? No of digits:  56789
#     ? No of digits:  5678
#     ? No of digits:  567
#     ? No of digits:  56
#     ? No of digits:  5



# todo                                                2. PRINT THE QUOTIENT AND REMINDER WHEN DIVIDIMG A NUMBER WITH ITS PLACE VALUE


num = input("Enter a number: ")
for i in range(len(num)+1):
    quotient = int(num)//10**i
    reminder=int(num)%10**i
    print('{} / {} = {}'.format(num,10**i,quotient))
    print('{} % {} = {}'.format(num, 10**i, reminder))

#! OUTPUT:

    #* Enter a number: 6479
    #? 6479 / 1 = 6479
    #? 6479 % 1 = 0
    #? 6479 / 10 = 647
    #? 6479 % 10 = 9
    #? 6479 / 100 = 64
    #? 6479 % 100 = 79
    #? 6479 / 1000 = 6
    #? 6479 % 1000 = 479
    #? 6479 / 10000 = 0
    #? 6479 % 10000 = 6479


#todo                                              3. PROGRAM TO PRINT A UNIT DIGIT OF A GIVEN NUMBER

num = input("Enter a number: ")
print('The unit digit of a number is',int(num)%10)

#! OUTPUT:
    #* Enter a number: 8654
    #? The unit digit of a number is 4







# todo                                              4. PROGRAM TO PRINT A LAST TWO DIGIT OF A GIVEN NUMBER

num = input("Enter a number: ")
print('The last two digit of a number is',int(num)%100)

#! OUTPUT:
    #* Enter a number: 8654
    #? The last two digit of a number is 54





#todo                                              5. PROGRAM TO PRINT A FIRST TWO DIGIT OF A GIVEN NUMBER

num = input("Enter a number: ")
print('The first two digit of a number is',int(num)//10**(len(num)-2))

#! OUTPUT
    #* Enter a number: 12376
    #? The first two digit of a number is 12







#todo                                              6. PROGRAM TO REMOVE LAST DIGIT OF A GIVEN NUMBER

num = int(input("Enter a number: "))
num=num//10
print(num)

#! OUTPUT:
    #* Enter a number: 36789
    #? 3678


#todo                                              7. PROGRAM TO REVERSE A GIVEN NUMBER

num=int(input('Enter the number'))
rev_num=''
while(num!=0):
    digit=num%10
    rev_num+=str(digit)+' '
    num=num//10
print(rev_num)

#! OUTPUT:
    #* Enter the number24378
    #? 8 7 3 4 2


#** While in python way...
num=input('Enter the number: ')    #`the python interperter takes the input in string format,unless it is type-casted
print(num[::-1])      #`reversed string


#todo                                              8. PROGRAM TO ADD THE NO. OF DIGITS OF A GIVEN NUMBER


num=int(input('Enter the number: '))
sum_num=0
while(num!=0):
    sum_num+=num%10
    num=num//10
print(sum_num)

#! OUTPUT:
#*  Enter the number: 6783
#?  24


#** While in python way...
num=input('Enter the number: ')    #`the python interperter takes the input in string format,unless it is type-casted
print(sum(list(map(int,num))))


#todo                                              9. PROGRAM TO MULTIPLY THE NO. OF DIGITS OF A GIVEN NUMBER


num=int(input('Enter the number: '))
mul_num=1
while(num!=0):
    mul_num*=num%10
    num=num//10
print(mul_num)

#! OUTPUT:    
    #* Enter the number: 9754
    #? 1260



#** While in python way...(Using numby library)
import numpy as np
num=input('Enter the number: ')    #`the python interperter takes the input in string format,unless it is type-casted
l=list(map(int,num))   #`creating a list using map function
print(np.product(l))  #`product of list


#todo                                              10. PROGRAM TO COUNT THE NO. OF DIGITS OF A GIVEN NUMBER


num = int(input('Enter the num: '))
count=0
while(num!=0):
    num=num//10
    count+=1
print(count)


#! OUTPUT:
    #* Enter the num: 12345
    #? 5


#** While in python
num=input('Enter the num: ')
print(len(num))





#todo                                              11. PROGRAM TO COUNT THE OCCURENCES OF A PARTICULAR DIGIT OF A GIVEN NUMBER

num=int(input('Enter the number: '))
special_digit=int(input('Enter the Special Digit: '))
count=0
while(num!=0):
    digit=num%10
    if(digit==special_digit):
        count+=1
    num//=10
print(count)

#! OUTPUT:
    #*Enter the number: 123532133
    #* Enter the Special Digit: 3
    #? 4



#* While in python way...(Using built-in)
num = input('Enter the number: ')
special_digit = input('Enter the Special Digit: ')
print(num.count(special_digit))





#todo                                               12. PROGRAM TO REPLACE A NUMBER ON A SPECIFIC DIGIT POSITION

num = input('Enter the number: ')
pos=int(input('Enter the position in the number: '))
replace_num = input('Enter the replacing number: ')
l=[i for i in num]
l[len(l)-pos]=replace_num
print(''.join(l))


#! OUTPUT:
    #* Enter the number: 25673
    #* Enter the position in the number: 2
    #* Enter the replacing number: 4
    #? 25643




#todo                                                 13. PROGRAM TO CHECK "HARSHAD" NUMBER OR NOT


num = int(input('Enter the number: '))
sum_num=0
while(num!=0):
    sum_num+=num%10
    num=num//10
if(num%sum_num==0):print("HARSHAD NUMBER")
else:print("NOT A HARSHAD NUMBER")


#! OUTPUT:
    #* Enter the number: 140
    #? HARSHAD NUMBER





#todo                                                 14. PROGRAM TO CHECK "AUTOMORPHIC" NUMBER OR NOT


num = int(input('Enter the number: '))
auto=num**2
if(num==auto%10**len(str(num))):print("AUTOMORPHIC NUMBER")
else:print('NOT A AUTOMORPHIC NUMBER')


#! OUTPUT:
    #* Enter the number: 76
    #? AUTOMORPHIC NUMBER





#todo                                                 15. PROGRAM TO FIND THE SUM OF SQUARES OD 'N' ODD NOS.

num = int(input('Enter the number: '))
sum=0
for i in range(1,num*2,2):
    sum+=i**2
print(sum)


#! OUTPUT:
    #* Enter the number: 5
    #? 165


#todo                                                 16. PROGRAM TO CHECK "STRONG" NUMBER OR NOT


def fact(digit):
    factorial=1
    if(digit!=0):
        factorial*=digit*fact(digit-1)
    return(factorial)

num=int(input('Enter the number: '))
d_num=num
strong_num=0
while(d_num!=0):
    digit=d_num%10
    strong_num +=fact(digit)
    d_num//=10
if(strong_num==num):print('STRONG NUMBER')
else:print('NOT A STRONG NUMBER')



#! OUTPUT:
    #* Enter the number: 40585
    #? STRONG NUMBER


#todo                                                 17. PROGRAM TO CHECK "PALINDROM" NUMBER OR NOT


num = int(input('Enter the number'))
rev_num=''
sum_num=0
while(num!=0):
    digit=num%10
    sum_num+=digit
    num=num//10
d_num=str(sum_num)
while(sum_num!=0):
    sum_digit=sum_num%10
    rev_num+=str(sum_digit)
    sum_num//=10
if(rev_num==d_num):print('PALINDROME')
else:print('NOT A PLAINDROME')


#! OUTPUT:
    #* Enter the number: 1253
    #? PALINDROME NUMBER


#** While in Python way...

n=input('Enter the number')
l1=str(sum(list(map(int,n))))
if(l1==l1[::-1]):print('Palindrome')
else:print('Not a plaindrome') 





#todo                                                 18. PROGRAM TO CHECK "ADAM" NUMBER OR NOT

def reverse_num(n):
    rev=''
    while(n!=0):
        digit=n%10
        rev+=str(digit)
        n//=10
    return(rev)
num=int(input('Enter the number: '))
rev_num=int(reverse_num(num))
square_rev_num=rev_num**2
square_num=num**2
sqaure_num1=int(reverse_num(square_num))
if(square_rev_num==sqaure_num1):print('ADAM NUMBER')
else:print("NOT A ADAM NUMBER")



#todo                                                 19. PROGRAM TO CHECK "EMIRP" NUMBER OR NOT


#! function to find a prime number 
def prime(n):
    l=[i for i in range(1,n+1)]
    p=2
    while(p*p<=n):
        if(p in l):
            for i in range(p*p,n+1,p):
                if(i in l and i%p==0):
                    l.remove(i)
        p+=1
    if(n in l):
        return('PRIME NUMBER')
    else:return('NOT A PRIME NUMBER')
#! function to reverse a number 
def reverse_num(n):
    rev=''
    while(n!=0):
        digit=n%10
        rev+=str(digit)
        n//=10
    return(rev)
# #!main 
if(__name__=='__main__'): 
    num=int(input('Enter the Number: '))
    if(prime(num)=='PRIME NUMBER' and prime(int(reverse_num(num)))=='PRIME NUMBER'):
        print('EMIRP NUMBER')
    else:print('NOT A EMIRP NUMBER')
                
#! OUTPUT:
#** Enter the Number: 13
#?  EMIRP NUMBER



#todo                                              20. PROGRAM TO CONVERT DECIMAL TO BINARY

num=int(input('Enter the number: '))
digit=''
while(num!=1):
    digit+=str(num%2)
    num//=2
print('1'+digit[::-1])


#!  OUTPUT:
#*  Enter the number: 22
#?  10110



#todo                                              21. PROGRAM TO CONVERT BINARY TO DECIMAL


num = int(input('Enter the decimal number: '))
i=0
s=0
while(num!=0):
    digit=num%10
    s+=(2**i)*digit
    num//=10
    i+=1
print(s)

#!  OUTPUT:
#*  Enter the decimal number: 11101110
#?  238

#** While in python way...
num = input('Enter the decimal number: ')
print(int(num,2))



#todo                                              22. PROGRAM TO CONVERT DECIMAL TO OCTAL



num = int(input('Enter the number: '))
digit=''
while(num!=1):
    digit+=str(num%8)
    num//=8
print('1'+digit[::-1])

#!  OUTPUT:
#*  Enter the number: 22
#?  10110


#todo                                              23. PROGRAM TO CONVERT DECIMAL TO HEXADECIMAL


def hexadecimal(n):
    dic={10:'A',11:'B',12:'C',13:'D',14:'E',16:'F'}
    if(n>9):return(dic[n])
    else:return(str(n))

num = int(input('Enter the number: '))
hexa=''
while(num!=0):
    hexa+=hexadecimal(num%16)
    num//=16
print(hexa[::-1])

#!  OUTPUT:
#*  Enter the number: 590
#?  24E
#*  Enter the number: 100
#?  64
#*  Enter the number: 188
#?  BC




#todo                                              24. PROGRAM TO COUNT EVEN OR ODD NUMBERS


num=input('Enter the Series of numbers: ')
even=0
odd=0
for i in num:
    if(int(i)%2==0):
        even+=1
    else:odd+=1
print('Even=',even,'Odd=',odd)


#!  OUTPUT:
#*  Enter the Series of numbers: 816759
#?  Even= 2 
#?  Odd= 4


#todo                                              25. PROGRAM TO COUNT PRIME NUMBERS


def prime(n):
    l=[i for i in range(1,n+1)]
    p=2
    while(p<=n):
        if(p in l):
            for i in range(p*p,n+1,p):
                if(i%p==0):l.remove(i)
        p+=1
    if(n in l and n!=1):return('PRIME NUMBER')
    else:return('NOT A PRIME NUMBER')

num = input('Enter the Series of numbers: ')
c=0
for i in num:
    if(prime(int(i))=='PRIME NUMBER'):
        c+=1
print('Prime=',c)

#!  OUTPUT:
#*  Enter the Series of numbers: 8234
#?  Prime= 2


#todo                                              26. PROGRAM TO FIND LARGE AND SMALL NUMBERS

num = int(input('Enter the Series of numbers: '))
large=0
small=9999999
while(num!=0):
    digit=num%10
    if(digit>large):
        large=digit
    elif(digit<small):small=digit
    num//=10
print('large=',large,'small=',small)


#!  OUTPUT:
#*  Enter the Series of numbers: 9586
#?  large= 9 
#?  small= 5


#** Using Built in  method(Python way)
num = input('Enter the Series of numbers: ')
l=list(map(int,num))
print('large=',max(l),'small=',min(l))


#todo                                              27. PROGRAM TO LEFT ROTATE A GIVEN NUMBER

num=int(input('Enter the number: '))
rotation=int(input('Enter the no. of rotations: '))
part1=num%10**(len(str(num))-rotation)
part2=num//10**(len(str(num))-rotation)
part3=str(part1)+str(part2)
print(part3)

#! OUTPUT
#*  Enter the number: 12345
#*  Enter the no. of rotations2
#?  34512

#*  Enter the number: 12345
#*  Enter the no. of rotations4
#?  51234


#** While in Python way

num = input('Enter the number: ')
rotation = int(input('Enter the no. of rotations: '))
part3=num[rotation:]+num[:rotation]
print(part3)




#todo                                              28. PROGRAM TO RIGHT ROTATE A GIVEN NUMBER

num=int(input('Enter the number: '))
rotation=int(input('Enter the no. of rotations: '))
part1=num%10**rotation
part2=num//10**rotation
part3 = str(part1)+str(part2)
print(part3)


#! OUTPUT
#*  Enter the number: 12345
#*  Enter the no. of rotations2
#?  34512

#*  Enter the number: 7689
#*  Enter the no. of rotations: 2
#?  8976


#** While in Python way

num = input('Enter the number: ')
rotation = int(input('Enter the no. of rotations: '))
part3 = num[len(num)-rotation:]+num[:len(num)-rotation]
print(part3)




#todo                                              29. PROGRAM TO GENERATE ALL THE RIGHT ROTATIONS OF A GIVEN NUMBER

num=int(input('Enter the number: '))
for i in range(1,len(str(num))):
    part1=num%10**i
    part2=num//10**i
    part3 = str(part1)+str(part2)
    print(part3)


#! OUTPUT
#*  Enter the number: 123456
#?  612345
#?  561234
#?  456123
#?  345612
#?  234561


#** While in Python way

num = input('Enter the number: ')
for i in range(1, len(str(num))):
    print(num[len(num)-i:], num[:len(num)-i])
    part3 = num[len(num)-i:]+num[:len(num)-i]
    print(part3)
