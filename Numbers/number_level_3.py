
#&                        1. PROGRAM TO GENERATE A JUMPING NUMBER OR NOT



import math
import time
def jumping(n):
    if(0>=i<=10):
        return True
    while(int(math.log10(n))!=0):
        if(((n%100)//10)-n%10==1 or ((n%100)//10)-n%10==-1):
            n//=10
        else:return False
    return True


t=time.time()
num=int(input('Enter the number:'))
l=[]
for i in range(num//2):
    if(jumping(i)==True):
        l.append(i)
    if(jumping(num-i)==True):
        l.append(num-i)
l.sort()
print(l)
print(time.time()-t)


#!  OUTPUT
#*  Enter the number: 30
#?  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 21, 23]






#&                                      2. PROGRAM TO PRINT THE NUMBERS WHICH HAVE EVEN NO. OF ODD NUMBERS AND ODD NO. OF EVEN NUMBERS

def odd_even_digits(n):
    even=0
    odd=0
    while(n!=0):
        if((n%10)%2==0):
            odd+=1
        else:even+=1
        n//=10
    if(even%2==0 and odd%2!=0):
        return True
    else:return False


strt=int(input('Enter the number: '))
end=int(input('Enter the number: '))
c=0
for i in range(strt,end+1):
    if(odd_even_digits(i)==True):
        c+=1
print(c)




#!  OUTPUT
#*  Enter the number: 100
#*  Enter the number: 150
#?  26







#&                                       3. PROGRAM TO FIND THE SMALLEST NUMBER OF A GIVEN NUMBER

import math,time

#` To remove the digits from the number
def remove_digit(num,min_num):
    result=0
    while(num!=0):
        if(num%10!=min_num and num%10>0):
            result=result*10+(num%10)
        num//=10
    return(result)

#` To find the least number 

def least(n,least_num):
    while(n!=0):
        if(n%10<=least_num and n%10>0):
            least_num=n%10
        n//=10
    return least_num


t=time.time()
num=int(input('Enter the number: '))
small=0
while(num!=0):                                                     #`Time is less than 5 sec`
    min_num=9
    min_num=least(num,min_num)
    small=(small*10)+min_num
    num=remove_digit(num,min_num)
print(small)
print(time.time()-t)



#!  OUTPUT
#*  Enter the number: 991233612
#?  12369

#*  Enter the number: 5468001
#?  14568





#&                        4. PROGRAM TO FIND THE SMALLEST NUMBERSUCH THAT THE PRODUCT OF DIGITS IS EQUAL TO THAT NUMBER 

import time
t=time.time()
num=int(input('ENTER THE NUMBER: '))
result=0
l=list()
min_num=9999
for i in range(9,1,-1):
    while(num%i==0):
        l.append(i)
        num//=i
if(num!=1):
    print(-1)
else:
    result=0
    while(len(l)!=0):
        result=result*10+l[-1]
        l.pop()
    print(result)
print(time.time()-t)


#!   OUTPUT
#*   Enter the number: 1000
#?   5558





#&                   5. TO FIND THE LARGEST PALINDROM FROM THE NUMBER OF DIGITS GIVEN

import time
def reverse(num):
    result=0
    while(num!=0):
        result=result*10+num%10
        num//=10
    return result
t=time.time()
max_pal=0
                                            #    `Time limit is less than 4 sec for inputs lesser than 5`
n=int(input('Enter the number of digits'))
for i in range(1*(10**n)-1, 9*(10**(n-1)), -2):
    for j in range(1*(10**n)-1, 9*(10**(n-1)), -2):
        if(i*j==reverse(i*j)):
            if(max_pal<=i*j):
                max_pal=i*j
print(max_pal)
print(time.time()-t)



#!  OUTPUT
#*  Enter the digit: 3
#?  906609  





#&                                             6. PROGRAM TO CHECK WHETHER A NUMBER IS PANDIGITAL OR NOT

import time
def ischeck(n,base):
    while(n!=0):
        if(n%10>=base):
            return False
        n//=10 #n=n//10
    return True

def isPandigital(n,base):
    N=n#n=122345
    base=base-1
    if(base>=0):
        while(n!=0):
            if(n%10==base):
                return isPandigital(N,base)
            n//=10
        return False
    return True

t=time.time()
num=int(input('Enter the number: '))
base=int(input('Enter the base number: '))
if(ischeck(num,base)):
    if(isPandigital(num,base)):
        print('PANDIGITAL NUMBER')
    else:print('NOT A PANDIGITAL NUMBER')
else:print('NOT A VALID NUMBER')
print(time.time()-t)



# !  OUTPUT
# *  Enter the number: 9651723480
# *  Enter the base: 10
# ?  PANDIGITAL NUMBER 


# *  Enter the number:  103678954
# *  Enter the base: 10
# ?  NOT A PANDIGITAL NUMBER







# &                                        7. PROGRAM TO FIND THE NEXT LARGEST NUMBER IN THE GIVEN SET OF DIGITS

import math,time

def swap(n, replace_num):
    min_num=999
    N=n
    l=int(math.log10(N)+1)
    #`` finding the min num of the right side of the digit
    while(n!=0):
        if(n%10<=min_num):
            min_num=n%10
        n//=10
    c=1
    a=N
    #`swaping the positions of two nums
    if(replace_num<min_num):
        while(N!=0):
            if(N%10==min_num):
                #`swaping the positions of digits`
                n=min_num*10**l+(a//(10**c))*10**c+replace_num 
                return n
            c+=1
            print('c=',c)
            N//=10
    else:print(False)

def largest_num(n):
    N=n
    c=0   #`Used to count the traversed digits`
    while(n!=0):
#`comparing the 100th unit and 10th unit of the given input number
        if((n%100)//10<n%10): 
#`right hand side of the given number and the lowest digit`
            swap_num=swap(N%10**(c+1),(n%100)//10)  
#`adding the left hand side and swaped right hand side to combine to a large number`
            new_num=(N//(10**(int(math.log10(swap_num)+1))))*(10**int(math.log10(swap_num)+1))+swap_num
            return new_num
        c+=1
        n//=10
    return('NOT POSSIBLE')
                
t=time.time()
num=int(input('Enter the number: '))
if(num//10**int(math.log10(num))>num%10):
    print('NOT POSSIBLE')
else:
    print(largest_num(num))
print(time.time()-t)





#&                               8.PROGRAM TO FIND THE LARGEST PALINDROME NUMBER 

import math,time

def reverse(n):
    r=0
    while(n!=0):
        r=r*10+n%10
        n//=10
    return(r)

t=time.time()
num=int(input('Enter the number: '))
l = int(math.log10(num))
if((l+1)%2==0):
#`finding the mid element and spliting into left and right part`
#`the right side of the mid element is removed
#`the left side if the element is take and reversed and replaced to the right side of the mid element
#` in case of mid element in ,
#`         i) in case of even number of digits the middle element and element next to it have been added by 10
#`        ii) in case of odd number of digits the mid element alone has been incremented by 1       
    new_num = ((num//10**(l//2))+10)*10**(l//2)+reverse(num//10**(l+1-(l//2)))
    print(new_num)
else:
    new_num=((num//10**(l//2))+1)*10**(l//2)+reverse(num//10**(l+1-(l//2)))
    print(new_num)


#! OUTPUT
#* Enter the number:   124567892
#?  124575421

#* Enter the number:   213456
#?  214412






#&                               10. PROGRAM TO COUNT THE NUMBER OF 2's FROM RANGE 0 to N


def find_2(n):
    c=0
    while(n!=0):
        if(n%10==2):
            c+=1
            print('count=',c)
        n//=10
    return c

num=int(input('Enter the range: '))
forward_2,backward_2=0,0
for i in range(0,(num//2)+1,2):
    print(i,num-i)
    forward_2+=find_2(i)
    backward_2+=find_2(num-i)
print(forward_2+backward_2)



#! OUTPUT
#*  Enter the number: 100
#?  15


#* Enter the number: 20
#? 3  





#&                                    11. PROGRAM TO COUNT THE N-DIGIT NUMBERS WITH ALL DISTINCT DIGITS

import math,time
t=time.time()
num=int(input('Enter the Nth digit: '))
sum=1
c=10
l = int(math.log10(10**(num)))
for i in range(0,l):
    if(i==0):sum*=(c-1)
    else:sum*=c
    c-=1
print(sum)
print(time.time()-t)


#! OUTPUT
#* Enter the Nth digit: 10
#?  3265920

#* Enter the Nth digit: 2
#?  81






#&                                  12. PROGRAM TO FIND THE Nth DIGIT IN A NUMBER SEQUENCE





def findNthDigit(n):
    if (n < 10):
        return n
        # find the digit of n
    digit = 0
    tmp = 0
    pre = 0
    while (tmp < n):
        pre = tmp
        print('pre=',pre)
        digit += 1
        print('digit',digit)
        tmp += (9*(10**(digit-1)))*digit
        print('tmp',tmp)
        # find where it belongs
    n -= pre
    print('n=',n)
    num = 10**(digit-1) + ((n-1)//digit)
    print('10**({})+(({})//{})'.format(digit-1,n-1,digit))
        # find the index
    print('num',num)    
    index = (n-1) %digit
    print('index=',index)
    return num//(10**(digit-index-1)) %10
print(findNthDigit(2341))






#&                                  13. PROGRAM TO COUNT THE NUMBER OF DIGITS REQUIRED TO WRITE NUMBERS FROM 1 to N


num=int(input('Enter the number: '))
if(num<9):
    print(num)
else:
    print(((num-9)*2)+9)



#!   OUTPUT
#*    Enter the number: 10
#?    11


#*   Enter the number: 81
#?   153 






#&                               14. PROGRAM TO COUNT THE NUMBER OF NATURAL OCTAL NUMBERS FRO GIVEN N digits


n=int(input('Enter the number of digits: '))
print(7*(8**(n-1)))



#!  OUTPUT
#*  Enter the number of digits: 2
#?  56  

#*  Enter the number of digits: 4
#?  3584





#&                                 15. PROGRAM TO CREATE A LARGE PALINDROME  

import math,time

def reverse(n):
    s=0
    while(n!=0):
        s=s*10+n%10
        n//=10
    return s

def count(num):
    c=1
    while(num!=0):
        if((num%100)//10< num%10):
            break;
        c+=1
        num//=10 
    return c


t=time.time()
num=int(input('Enter the number: '))
l=int(math.log10(num)+1)
c=count(num)                                    #` Time limit is less than 2 secs`
first=num//10**(l-c)
middle = (((num % 10**(l-c))//10**(c))*10**(c))
last=num%10**(c)
large_pal=reverse(first)*10**(l-c)+middle+reverse(last)
print(large_pal) if (large_pal>num) else print(-1)
print(time.time()-t)



#!  OUTPUT
#*  Enter the number: 247656742
#?  742656247

#*  Enter the number: 210012
#?  210012

#*  Enter the number: 963369
#?  -1






#&                                16. PROGRAM TO DELETE THE DIGITS THAT TURNS A NUMBER INTO ODD AND SUM OF THE DIGITS EVEN

import math,time

def remove_digits(n):
    result=0
    mul=1
    while(n!=0):
        if((n%10)%2!=0):
            result=result+(n%10)*mul
            mul*=10
        n//=10
    if(int(math.log10(result)+1)%2!=0):
        result//=10
    return -1 if result==0 else result
t=time.time()
num=int(input('Enter the number: '))
print(remove_digits(num))
print(time.time()-t)



#! OUTPUT
#*  Enter the number: 25679
#?  57 

#*  Enter the number: 100
#?  -1








#&                              17. PROGRAM TO FIND A PRIME NUMBER WITH PRIME DIGITS 

# import math,time

# def isPrime(n):
#     if(n==2 or n==3 or n==5 or n==7):
#         return 1
#     return 0

# def prime_num(num,c):
#     c+=1
#     if(isPrime(num%10) and num%10>2):
#         if(num%10==3):
#             return [(num//10)*10+(num%10)-1,c]
#         return [(num//10)*10+(num%10)-2,c]
    
#     elif(isPrime(num%10)==0 and num%10>2):
#         if(num%10==9):
#             return [(num//10)*10+(num%10)-2,c]
#         return [(num//10)*10+(num%10)-1,c]
#     else:
#         n,c = prime_num(num//10, c)
#         new_num = n*(10**1)+7*int('1'*1)
#         return [new_num,c]


# # print(prime_num(725255,0))

# num=int(input('Enter the number: '))
# c=0
# pnum=0
# N=num
# l = int(math.log10(num)+1)
# if(num//10**(int(math.log10(num)))<=2):
#     num=num%10**l-1
#     new_num=7*int(str(1)*(l-1))
#     print(new_num)
# else:
#     while(num!=0):
#         c+=1
#         # print('num={} in c={}'.format(num,c))
#         if(num%10<2):
#             new_num, count = prime_num(num//10**(c),0)
#             # print('new_num={} in c={}'.format(new_num,c))
#             # print('count is ',count)
#             pnum=new_num*10**(c)+7*int((str(1)*(c)))
#             # print('pnum={} in c={}'.format(pnum,c))
#             num=num//(10**(count+1))
#             # print('num after n//=10**count is {}'.format(num))
#             c=count+1
#             # print('updated c is',c)
#         elif(isPrime(num%10) and num%10>=2):
#             num//=10
#             # print('num after isPrime==1 is',num)
#         elif(isPrime(num % 10)==0 and num % 10 >= 2):
#             new_num,count = prime_num(num,0)
#             # print('new_num={} in c={} after isPrime==0'.format(new_num, c))
#             pnum=new_num*10**(c-1)+pnum%10**(c-1)
#             # print('pnum={} in c={} after isPrime==0'.format(pnum, c))
#             num=num//(10**count)
#             # print('num after n//=10**count in isPrime==0 is {}'.format(num))
#     print(pnum)








#&                                         18. PROGRAM TO OUTPUT PRATICAL NUMBER FROM 1 TO N


# n=int(input('Enter the number: '))
# mul=1
# result=0
# while(n!=0):
#     if((n%100)//10==n%10):
#         result+=(n%10)*mul
#         n//=100
#     else:
#         result+=(n%10)*mul
#         n//=10
#     mul*=10
# print(result)






#&                                     19. PROGRAM TO CREATE A PERFECT SQUARE BY DELETING MINIMUN NUMBER OF DIGITS  




# from math import sqrt,floor
# from itertools import combinations
# num=input('Enter the number: ')
# lst=[]
# for i in range(1,len(num)+1):
#     #`Generating differnt sequence of numbers using itertool module`
#     l=list((combinations(num,i)))
#     #`Converting tuple in a list to a string using map function
#     l=list(map(''.join,l))
#     lst+=l
# new_list=[]
# for i in range(len(lst)):
#     #`seperating perfect squares from rest of the sequence of numbers`
#     #`taking the sqrtroot of num`
#     s = floor(sqrt(int(lst[i])))
#     #`checking perfect square or not`
#     if(s*s==int(lst[i])):
#         new_list.append(int(lst[i]))
# if(new_list==[]):print(-1)
# else:print(max(new_list), len(num)-len(str(max(new_list))))




#!   OUTPUT
#*   Enter the number: 2345
#?   25 2

#*  Enter the number: 787
#?  -1