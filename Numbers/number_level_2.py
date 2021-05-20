
#todo                         1. PROGRAM TO FIND THE SUM OF DIGITS OF A NUMBER REPEATEDLY UNTILL A SINGLE NUMBER OCCURS

def sum_fn(n):
    s=0
    while(n!=0):
        s+=n%10
        n//=10
    return(s)

num=int(input('Enter the number: '))
add = sum_fn(num)
while(add>=10):
    add=sum_fn(add)
print(add) 

#! OUTPUT
#*  Enter the number: 1647
#?  9

#*  Enter the number: 392
#?  5


#** While in python(Uisng built-in) 
num=input('Enter the number: ')
l=list(map(int,num))
add=sum(l)
while(add>=10):
    sum_list=list(map(int,str(add)))
    add=sum(sum_list)
print(add)

#! or

def sum_fn(n):
    return(sum(list(map(int,str(n)))))


num = input('Enter the number: ')
add=sum_fn(num)
while(add>=10):
    add=sum_fn(add)
print(add)






#todo                     2. PROGRAM TO FIND 'MAGIC NUMBER' OR NOT

def magic(n):
    d=0
    while(n!=0):
        d+=n%10
        n//=10
    return d

num=int(input('Enter the number: '))
add=magic(num)
while(add>=10):
    add=magic(add)
if(add==1):print('MAGIC NUMBER')
else:print('NOT A MAGIC NUMBER')


#! OUTPUT
#* Enter the number: 406
#? MAGIC NUMBER   

#* Enter the number: 95
#? NOT A MAGIC NUMBER   




#todo                     3. PROGRAM TO PRINT THE LAST TWO DIGITS OF FIBONACCI NUMBER 


num=int(input('Enter the nth number: '))
n0,n1=0,1
if(num <= 0):
    print(0)
elif(num == 1):
    print(n1)
else:
    for i in range(num-1):
        ans = n0+n1
        n0, n1 = n1, ans
    print(ans % 100)

#! OUTPUT
#* Enter the nth number: 15
#? 10

#* Enter the nth number: 1
#? 1





#todo                     4. PROGRAM TO PRINT THE 'Kth' DIGIT


l=list(map(int,input('Enter the three numbers').split()))
num=l[0]**l[1]
for i in range(l[2]):
    if(i==l[2]-1):print(num%10)
    else:num//=10

#!  OUTPUT
#*  Enter the three numbers: 9 4 3
#?  5   


#todo                     5. PROGRAM TO FIND WHETHER A NUMBER IS CIRCULAR OR NOT
import time
t0=time.time()
num = int(input('Enter the number: '))
final_num = int(input('Enter the final number: '))
i=1
while(i!=len(str(num))):
    if(num!=final_num):num=int(str(num%10)+str(num//10))
    else:break
    i+=1
if(num==final_num):print('YES')
else:print('NO')
print(time.time()-t0)


#! OUTPUT
#*   Enter the number: 123456
#*   Enter the final number: 345612
#?   YES


#** While in Python way

num = input('Enter the number: ')
final_num = input('Enter the final number: ')
part=''
for i in range(1, len(num)+1):
    part=num[len(num)-i:]+num[:len(num)-i]
    if(part==final_num):break
    else:continue
if(part==final_num):print('YES')
else:print('NO')





#todo                     6. PROGRAM TO FIND 'CIRCULAR PRIME' OR NOT


def prime(n):
    l=[i for i in  range(1,n+1)]
    p=2
    while(p*p<=n):
        if(p in l):
            for i in range(p*p,n+1,p):
                if(i in l and i%p==0):l.remove(i)
        p+=1
    if(n in l):return('PRIME NUMBER')
    else:return('NOT A PRIME NUMBER')

num=int(input('Enter the number'))
c=1
if(prime(num)=='PRIME NUMBER'):
    for i in range(1,len(str(num))):
        part=str(num%10**i)+str(num//10**i)
        if(prime(int(part))=='PRIME NUMBER'):
            c+=1
        else:break
    if(c==len(str(num))):print('CIRCULAR PRIME')
    else:print('NOT A CIRCULAR ')
else:
    print('NOT A CIRCULAR PRIME')


#! OUTPUT
#* Enter the number: 3119
#? CIRCULAR NUMBER

#* Enter the number: 911
#? NOT A CIRCULAR NUMBER






#todo                     7. PROGRAM TO GENERATE CIRCULAR PRIME NUMBERS FROM AN INTERVAL

#! to check wthere a num is prime or not 
def prime(n,i):
    if(n == 1):
        return False
    if(n==i):return True
    if(n%i==0):
        return False
    i+=1
    return(prime(n,i))

# #! to generate circular prime numbers 
def circular(num):
    lst=[num]
    c=1
    for i in range(1, len(str(num))):
        part=str(num%10**i)+str(num//10**i)
        if(prime(int(part),2)==True):
            lst.append(int(part))
            c+=1
        else:break
    if(c==len(str(num))):return lst
    else:return([])

# #! main 
strt=int(input('Enter the Number: '))
end=int(input('Enter the number: '))
if(strt%2==0):
    strt+=1
l=[]
for i in range(strt,end+1,2):
    if(i>10 and prime(i,2)==True and i not in l):
        lst = circular(i)
        l.extend(set(lst))
        l.sort()
print(' '.join(list(map(str,l))),sep=' ')


#! OUTPUT
#*  Enter the Number: 1
#*  Enter the number: 1000
#? 11 13 17 31 37 71 73 79 97 113 131 197 199 311 337 373 719 733 919 971 991

#*  Enter the Number: 10
#*  Enter the number: 100
#? 11 13 17 31 37 71 73 79 97

#*  Enter the Number: 100
#*  Enter the number: 1000
#? 113 131 197 199 311 337 373 719 733 919 971 991








#todo                     8. PROGRAM TO FIND 'LUCKY NUMBER' OR NOT

import time
t0=time.time()
num=input('Enter the number: ')
l=list(map(int,num))
l.sort()
if(l==list(set(l))):print('MAGIC NUMBER')
else:print('NOT A MAGIC NUMBER')
print(time.time()-t0)

#! OUTPUT
#* Enter the number: 1234
#? MAGIC NUMBER  

#* Enter the number: 12321
#? NOT A MAGIC NUMBER


#todo                    9. PROGRAM TO COUNT THE FREQUENCY OF DIGITS 

num=input('Enter the number: ')
for i in num:
    print(num.count(i))

#!OUTPUT
#*Enter the number: 120387332
#? 1
#? 2
#? 1
#? 3
#? 1
#? 1
#? 3
#? 3
#? 2


#todo                     10. PROGRAM TO GENERATE 'ADAM' NUMBERS FROM AN INTERVAL

import time
def square(n):
    return n*n
def reverse(n):
    d=''
    while(n!=0):
        d+=str(n%10)
        n//=10
    return(int(d))
t0=time.time()
strt = int(input('Enter the Number: '))
end=int(input('Enter the number: '))
for i in range(strt,end+1):
    if(square(i)==reverse(square(reverse(i)))):
        print(i,end=' ')
print(time.time()-t0)


#!  OUTPUT
#*  Enter the Number: 10
#*  Enter the number: 100
#?  11 12 13 21 22 31

#*  Enter the Number: 1
#*  Enter the number: 1000
#?  1 2 3 11 12 13 21 22 31 101 102 103 111 112 113 121 122 201 202 211 212 221 301 311


#* While in Python(solve using string...) 
import time
t0=time.time()
strt = int(input('Enter the Number: '))
end=int(input('Enter the number: '))
for i in range(strt,end+1):
    if(i**2==int(str(int(str(i)[::-1])**2)[::-1])):  #checking if sqaure of num is equal to reverse of reversed num's sqaure(i.e,(reverse(sqaure(reverse(num)))))
        print(i,end=' ')
print(time.time()-t0)
#!Note this method has high time complexity when compared to the above method





#todo                     11. PROGRAM TO GENERATE 'GOOD' NUMBERS FROM AN INTERVAL(CREDIT:GFG)


def isValid(n, d):
    	
	# Get last digit and initialize
	# sum from right side
	digit = n % 10;
	sum = digit;

	# If last digit is d, return
	if (digit == d):
		return False;

	# Traverse remaining digits
	n = int(n / 10);
	while (n > 0):
		
		# Current digit
		digit = n % 10;
	
		# If digit is d or digit is
		# less than or equal to sum
		# of digits on right side
		if(digit == d or digit <= sum):
			return False;
			
		# Update sum and n
		else:
			sum += digit;
			n = int(n / 10);
	return True;
	
# Print Good numbers in range [L, R]
def printGoodNumber(L, R, d):
	
	# Traverse all numbers
	# in given range
	for i in range(L, R + 1):
		
		# If current numbers is good,
		# print it
		if(isValid(i, d)):
			print(i, end = " ");
	
# Driver Code
L = 1;
R = 10000;
d = 3;
		
# Print good numbers in [L, R]
printGoodNumber(L, R, d);



#! OUTPUT
#*  Enter the Number: 410
#*  Enter the number: 520
#*  Enter the digit: 3
#?  410 420 421 510 520




#todo                     12. PROGRAM TO FIND 'LUCKY NUMBER' OR NOT
import time,math
t0=time.time()
num=int(input('Enter the number: '))
N=num
l=int(math.log10(num))+1     #**to count the number of digits withon 'len()' built-in function
ams=0
while(num!=0):
    ams+=(num%10)**l
    num//=10
if(ams==N):print('AMSTRONG NUMBER')
else:print('NOT A AMSTRONG NUMBER')
print(time.time()-t0)


#!  OUTPUT
#*  Enter the number: 1634
#?   AMSTRONG NUMBER  






#todo                     13. PROGRAM TO CHECK "STRONG" NUMBER OR NOT


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





#todo                                 14. PROGRAM TO GENERATE AMSTRONG NUMBERS
import math,time
def amstrong(n:int)->int:
    d=0
    l=len(str(n))                    #?  or use l=int(math.log10(n))+1 instead of len()
    while(n!=0):
        d+=(n%10)**l
        n//=10
    return d


t0 = time.time()
strt=int(input('Enter the starting Number: '))
end=int(input('Enter the ending Number: '))
for i in  range(strt,end+1):
    if(amstrong(i)==i):
        print(i,end=' ')
print(time.time()-t0)


#! OUTPUT
#*  Enter the starting Number: 100
#*  Enter the ending Number: 1000
#?  153 370 371 407
   



#todo                               15.TO REPLACE A DIGIT IN A NUMBER WITH ANOTHER ONE
import time
t0 = time.time()
num=int(input('Enter the number: '))
replace_num=int(input('Enter the replace digit: '))
new_num=int(input('Enter the digit to be replaced: '))
result=0
multipy=1
while(num!=0):
    d=num%10
    if(d==replace_num):
        result+=new_num*multipy
    else:
        result+=d*multipy
    multipy*=10
    num//=10
print(result) 
print(time.time()-t0)   #** Time : 7 secs



#! OUTPUT
#* Enter the number: 4515583
#* Enter the replace digit: 5
#* Enter the digit to be replaced: 2
#? 4212283


#* While in python(using list,str methods and loops)
t0 = time.time()
num = input('Enter the number: ')
replace_num = int(input('Enter the replace digit: '))
new_num = int(input('Enter the digit to be replaced: '))
l=list(map(int,num))
for i in range(len(l)):
    if(l[i]==replace_num):
        l[i]=new_num
print(''.join(map(str,l)))
print(time.time()-t0)   #** time :6 secs




#todo                                16. PROGRAM TO ARRANGE THE ODD DIGITS AND EVEN DIGITS IN A GIVEN NUMBER

t0 = time.time()
num=int(input('Enter the number: '))
option=int(input('Enter the option: '))
even=0
odd=0
even_mul=1
odd_mul=1
while(num!=0):
    d=num%10
    if(d%2==0):
        even+=d*even_mul
        even_mul*=10
    else:
        odd+=d*odd_mul
        odd_mul*=10
    num//=10
# print(str(even)+str(odd)) if(option == 0) else print(str(odd)+str(even))      #** Time: 8 secs 
#todo                                  or
print(even*10**len(str(odd))+odd) if(option==0) else print(odd*10**len(str(even))+even)   #**  Time: 10 secs
print(time.time()-t0)


#! OUTPUT
#* Enter the number: 67854
#* Enter the option: 0
#? 68475

#* Enter the number: 12345
#* Enter the option: 1
#? 13524


#* While in python(using string...)
t0 = time.time()
num = input('Enter the number: ')
option = int(input('Enter the option: '))
even,odd='',''
for i in num:
    if(int(i)%2==0):                                           #! Time : more than 10 secs to 22 secs
        even+=i
    else:odd+=i
print(even+odd) if(option == 0) else print(odd+even)
print(time.time()-t0)



#todo                                  17. PROGRAM TO SWAP ALTERNATIVE DIGITS

t0 = time.time()
num=(input('Enter the number: '))
l=list(map(int,num))
for i in range(len(l)-1):
    if(l[i]+1==l[i+1] or l[i]-1==l[i+1]):
        l[i],l[i+1]=l[i+1],l[i]
print(''.join(map(str,l)))
print(time.time()-t0)
#! OUTPUT
#* Enter the number: 56872
#? 65782

#* Enter the number: 123456
#? 214365





#todo                     18. PROGRAM TO CHECK "HAPPY" NUMBER OR NOT




def isHappy(num:int)->bool:
    happy=0
    while(num!=0):
        happy+=(num%10)**2
        num//=10
    if(happy==4):return False
    elif(happy==1):return True
    else:return isHappy(happy)

# t0 = time.time()
num=int(input('Enter the number: '))
if(isHappy(num)==True):
    print('HAPPY NUMBER')
else:print('NOT A HAPPY NUMBER')
print(time.time()-t0)

#! OUTPUT
#*   Enter the number: 32
#?   HAPPY NUMBER

# * Enter the number: 29
#?  NOT A HAPPY NUMBER

#** While in Python(using built-in...) 

def isHappy(num:str):
    happy=sum(list(map(lambda x: int(x)**2,num)))
    if(happy==4):return(False)
    elif(happy==1):return(True)
    else: return isHappy(str(happy))
# t0 = time.time()
num=input('Enter the number: ')
if(isHappy(num)==True):
    print('HAPPY NUMBER')                        #? this one is time less for some inputs when compared with the above one
else:print('NOT A HAPPY NUMBER')
print(time.time()-t0)





#todo                                  19. PROGRAM TO PRINT NUMBERS WHICH HAVE PRIME NUMBER 


#** prime number 


import math
def Prime():
    l=[i for i in range(2,10)]
    p=2
    while(p*p<10):
        if(p in l):
            for i in range(p*p,10,p):
                if(i in l):l.remove(i)
        p+=1
    return l

#** to check the digits of number is prime or not 


def count(n):
    c=0
    while(n!=0):
        if(n%10  in Prime()):
            c+=1
            n//=10
        else:break
    return c

strt=int(input('Enter the strting number: '))
end=int(input('Enter the ending number: '))
for i in range(strt,end+1):
    if(count(i)==int(math.log10(i)+1)):
        print(i,end=' ')

#! OUTPUT
#* Enter the strting number: 10
#* Enter the ending number: 100
#? 22 23 25 27 32 33 35 37 52 53 55 57 72 73 75 77




#todo                                   20. TO CHECK WHETHER A NUMBER IS INCREASING OR DECREASING OR BOUNCY NUMBER OR NOT

import math
num=int(input('Enter the number: '))
inc, dec, boun, l = 0, 0, 0, int(math.log10(num)+1)
while(num!=0):
    digit=num%10
    digit2=(num%100)//10
    if(digit>digit2):
        inc+=1
    elif(digit<digit2):
        dec+=1
    else:
        boun+=1
    num//=10

if(inc==l):print('INCREASING NUMBER')
elif (dec==l):print('DECREASING NUMBER')
else:print('BOUNCY NUMBER')
    
#!  OUTPUT
#*  Enter the number: 78236
#?  BOUNCY NUMBER 


#*  Enter the number: 25789
#?  INCREASING NUMBER 


#*  Enter the number: 85321
#?  DECREASING NUMBER 






#todo                                 21. PROGRAM TO COUNT THE PEAKY DIGITS


num=int(input('Enter the number: '))
c=0
while(num!=0):
    #!   taking the last 3 digits of given number 
    d=num%1000
    #!   checking if the middle element of the last three digits of given number is greater than the left and right digits 
    if((d%100)//10>d//100 and (d%100)//10>d%10):
        c+=1
    num//=10
print(c)


#!   OUTPUT
#*     Enter the number: 1417382
#?     3

#*     Enter the number13265
#?     2





# todo                              22. PROGRAM TO CONVERT BINARY TO OCTAL 

import math,time
def octal(n:int)->int:
    d=0
    mul=1
    while(n!=0):
        d=d+(n%8)*mul
        n//=8
        mul*=10
    return(d)

t0=time.time()   
num=int(input('Enter the binary number: '))
sum_of_digits=0
for i in range(int(math.log10(num)+1)):                #`` Time limit is 15 sec (based on input it differs)
    sum_of_digits+=(num%10)*2**i
    num//=10
print(octal(sum_of_digits))
print(time.time()-t0)


#!  OUTPUT
#*  Enter the binary number: 01101
#?  15 

#*  Enter the binary number: 1010101
#?  125 


#** While in Python(using built-in...)


t0 = time.time()
num=(input('Enter the binary number: '))       #`Time limit is 2 secs (based on input it differs)`
print('{0:o}'.format(int(num,2)))
print(time.time()-t0)




#todo                              23. PROGRAM TO CONVERT BINRY TO HEXADECIMAL


import time,math

#! Decimal
def decimal(n):
    sum_of_digits=0
    for i in range(int(math.log10(n)+1)):
        sum_of_digits+=(n%10)*2**i
        n//=10
    return(sum_of_digits)

#!  Hexadecimal
def hexa(n):
    d={10:'A',11:'B',12:'C',13:'D',14:'E',15:'F'}
    return(d[n])

t=time.time()
num=int(input('Enterthe number: '))                             #`` Time limit is 8 sec
hexa_dec=''
while(num!=0):
    d=num%10000
    # Finding its decimal value
    if(decimal(d)>10):
        hexa_dec+=hexa(decimal(d))
    else:
        hexa_dec+=str(decimal(d))
    num//=10000
print(hexa_dec[::-1])
print(time.time()-t)


#! OUTPUT

#*  Enter the number: 1010101101001
#?  1569

#* Enter the number: 1011
#? B



#** While in Python(using pre-defined and built-in funcions)

t = time.time()
num = (input('Enter the number: '))
print(hex(int(num,2)))                              #`` Time limit is 1.8 sec
print(time.time()-t)

#! OUTPUT
#*  Enter the number: 1010101101001
#?  0x1569
#`                             Here in this output '0x' is prefixed along with the number,
#`                             this is to represent that the number is written in hexadecimal format    
#*  Enter the number: 1011 
#?  0xb






#todo                              24. PROGRAM TO CONVERT HEXADECIMAL TO DECIMAL

def hexa(n):
    d={'A':10,'B':11,'C':12,'D':13,'E':14,'F':15}
    return(d[n])
t=time.time()
num=input('Enter  hexadecimal number')
num=num[::-1]
d=0
for i in range(len(num)):
    if(ord(num[i])>=65 and ord(num[i])<=70):
        d+=hexa(num[i])*16**i
    else:
        d+=int(num[i])*16**i
print(d)
print(time.time()-t)



#!  OUTPUT
#*   Enter  hexadecimal number: ABCDEF
#?   11259375

#*   Enter  hexadecimal numberF1
#?   241






#todo                              25. PROGRAM TO CONVERT OCTAL TO DECIMAL

t = time.time()
num=(int(input('Enter the number: ')))
d=0
for i in range(int(math.log10(num)+1)):
    d+=num%10*8**i
    num//=10
print(d)
print(time.time()-t)


#! OUTPUT
#*  Enter the number: 125
#?  85

#*  Enter the number: 23
#?  19


#* While in python(using pre-defined function)

t = time.time()
num=input('Enter the number: ')
print(int(num,8))
print(time.time()-t)






#todo                             26. PROGRAM TO CHECK WHTHER A NUMBER IS MERSENNE NUMBER OR NOT

import math
def isPrime(n):
    l=[i for i in range(1,n+1)]
    p=2
    while(p*p<=n):
        if(p*p in l):
            for i in range(p*p,n+1,p):
                if(i in l):l.remove(i)
        p+=1
    if(n in l):
        return True
    return False 



t=time.time()
num=int(input('Enter the number: '))
for i in range(2, round(math.sqrt(num))+1):
    if((2**i)-1==num):
        if(isPrime(i)==True):
            print('MERSENNE NUMBER')
        else:
            print('NOT A MERSEENE PRIME')
        break
    else:
        print('NOT A MERSEENE PRIME')
        break
print(time.time()-t)


#! OUTPUT
#*  Enter the number: 2147483648
#?  NOT A MERSEENE PRIME
#`  Time limit  4.420252799987793 

#*  Enter the number: 2147483647
#?  MERSEENE PRIME
#`  Time limit  4.420252799987793 








#todo                             27. PROGRAM TO CHECK WHETHER A NUMBER IS DISARIUM NUMBER OR NOT


import math
t=time.time()
num=int(input('Enter the number: '))
N=num
d=0
for i in range(int(math.log10(num)+1),0,-1):
    d+=(num%10)**i
    num//=10
if(d==N):print('DISARIUM NUMBER')
else:print('NOT A DISARIUM NUMBER')
print(time.time()-t)


#! OUTPUT
#*  Enter the number: 135
#?  DISARIUM NUMBER  






#todo                              28. PROGRAM TO CHECK WETHER A NUMBER IS  MYSTERY NUMBER OR NOT

def reverse(n):
    d=0
    while(n!=0):
        d=d*10+n%10
        n//=10
    return d


def mystery(num):
    for i in range(1,num//2+1):
        if(i+reverse(i)==num):
            return('MYSTERY NUM')
    return('NOT A MYSTERY NUM')

t=time.time()
num=int(input('Enter the number: '))
print(mystery(num))
print(time.time()-t)



#!   OUTPUT
#*   Enter the number: 504
#?   MYSTERY NUMBER

#*  Enter the number: 45
#?  NOT A MYSTERY NUMBER





#todo                              29. PROGRAM TO CONVERT INTO A LARGEST NUMBER


num=int(input('Enter the number: '))
if(num//10**int(math.log10(num))<num%10):
    print((num%10)*10**int(math.log10(num))+num//10)
else:
    print(-1)

#!   OUTPUT
#*   Enter the number: 2349
#?   9234

#*   Enter the number: 6581
#?   -1






#todo                           30. PROGRAM TO CHECK WEHTHER A DIGITS OF NUMBER IS DISTINCT OR NOT



import math
def isDistinct(n):
    if(int(math.log10(n)+1)==2):
        if(n%10==n//10):return False
        return True
    else:
        num=n%10
        n=n//10
        N=n
        right_side = n % 10**(int(math.log10(n)+1)//2)
        left_side=n//10**(int(math.log10(n)+1)//2)
        while(right_side!=0 or left_side!=0):
            if(num==right_side%10 or num==left_side%10):
                return False
            right_side//=10
            left_side//=10
        return isDistinct(N)
print(isDistinct(9924589))



#!  OUPUT
#*   9924589
#?   False


#*   1234567
#?  True   