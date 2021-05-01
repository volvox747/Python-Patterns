
#?                                                                      *********
#!                                                                      **     **
#!                                                                      * *   * *
#!                                                                      *  * *  *
#?                                                                      *   *   *
#!                                                                      *  * *  *
#!                                                                      * *   * *
#!                                                                      **     **
#?                                                                      *********


# n=6
# N=2*n-1
# for i in range(1,N+1):
#     for j in range(1,N+1):
#         if(i==1 or i==N):
#             print('*',end='')
#         elif(i<n and (j==1 or j==N or j==i or j==N-i+1)):
#             print('*',end='')
#         elif(i==n and (j==1 or j==N or j==n)):
#             print('*',end='')
#         elif(i>n and (j==1 or j==N or j==i or j==N-i+1)):
#             print('*',end='')
#         else:
#             print(' ',end='')
#     print()
     

#?                                                                          ***********
#!                                                                          *    *    *
#!                                                                          *    *    *
#!                                                                          *    *    *
#!                                                                          *    *    *
#?                                                                          ***********
#!                                                                          *    *    *
#!                                                                          *    *    *
#!                                                                          *    *    *
#!                                                                          *    *    *
#?                                                                          ***********




# n=6
# N=2*n+1
# for i in range(1,N+1):
#     for j in range(1,N+1):
#         if(i==1 or i==n+1 or i==N):print('*',end='')
#         elif(i>1 and i<=n and (j==1 or j==n+1 or j==N)):print('*',end='')
#         elif (i>n+1 and (j==1 or j==n+1 or j==N)):print('*',end='') 
#         else:print(' ',end='')
#     print()


#!                                                                         ****************
#!                                                                         *******  *******
#!                                                                         ******    ******
#!                                                                         *****      *****
#!                                                                         ****        ****
#!                                                                         ***          ***
#!                                                                         **            **
#!                                                                         *              *
#?                                                                         **            **
#?                                                                         ***          ***
#?                                                                         ****        ****
#?                                                                         *****      *****
#?                                                                         ******    ******
#?                                                                         *******  *******
#?                                                                         ****************


# n=5
# R=2*n-1
# C=2*n
# b=n
# for i in range(1,R+1):
#     for j in range(1,C+1):
#         if(i<=n and (j <= b or j > C-b)):print('*', end='')
#         elif(i>n and (j<=b or j>C-b)):print('*',end='')
#         else:print(' ',end='')
#     if(i<n):b-=1
#     else:b+=1
#     print()

# !  CREATED PATTERN

#                                                                                  *
#                                                                                  * *
#                                                                                  ** **
#                                                                                  *** ***
#                                                                                  **** ****
#                                                                                  ***** *****
#                                                                                  ****** ******
#                                                                                  **************
#                                                                                  ****** ******
#                                                                                  ***** *****
#                                                                                  **** ****
#                                                                                  *** ***
#                                                                                  ** **
#                                                                                  * *
#                                                                                  *


#!                                                                            *            *
#!                                                                            **          **
#!                                                                            ***        ***
#!                                                                            ****      ****
#!                                                                            *****    *****
#?                                                                            ******  ******
#?                                                                            **************
#?                                                                            ******  ******
#!                                                                            *****    *****
#!                                                                            ****      ****
#!                                                                            ***        ***
#!                                                                            **          **
#!                                                                            *            *
                                  
                                      
                                       
                                   
                                            
                            

# n = 7
# R=2*n-1
# C=2*n
# for i in range(1,R+1):
#     for j in range(1,C+1):
#         if(i<=n and (j<=i or j>C-i)):print('*',end='')
#         elif (i>n and (j<=C-i or j>i)):print('*',end='')
#         else:print(' ',end='')
#     print()
            




#todo                                                                     1
#todo                                                                     2 3
#?                                                                        4 5 6
#?                                                                        7 8 9 10
#todo                                                                     11 12 13 14 15 
#todo                                                                     16 17 18 19 20 21  

# n=10
# add=0
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         add+=1
#         print(add,end=' ')
#     print()

#todo                                                                     21 20 19 18 17 16
#todo                                                                     15 14 13 12 11
#?                                                                        10 9 8 7
#?                                                                        6 5 4
#todo                                                                     3 2
#todo                                                                     1


# n=6
# sub=(n*(n+1))//2
# for i in range(n,0,-1):
#     for j in range(1,i+1):
#         print(sub,end=' ')
#         sub-=1
#     print()


#todo                                                                     1 2 3 4 5 6
#todo                                                                     2 3 4 5 6 1
#?                                                                        3 4 5 6 1 2
#?                                                                        4 5 6 1 2 3
#todo                                                                     5 6 1 2 3 4
#todo                                                                     6 1 2 3 4 5


# a = 0
# n = 6
# for i in range(n):
#     b = 0
#     a = i
#     for j in range(1, n+1):
#         if(j >= n+1-i):
#             b += 1
#             print(b, end=' ')
#         else:
#             a += 1
#             print(a, end=' ')
#     print()


#todo                                                                     6 6 6 6 6 6
#todo                                                                     6 5 5 5 5 5
#?                                                                        6 5 4 4 4 4
#?                                                                        6 5 4 3 3 3
#todo                                                                     6 5 4 3 2 2
#todo                                                                     6 5 4 3 2 1

# n=6
# for i in range(n):
#     for j in range(n):
#         if(j<=i):print(n-j,end=' ')
#         else:print(n-i,end=' ')
#     print()
    

#todo                                                                     1 1 1 1 1 1 2
#todo                                                                     3 2 2 2 2 2 2
#?                                                                        3 3 3 3 3 3 4
#?                                                                        5 4 4 4 4 4 4
#todo                                                                     5 5 5 5 5 5 6
#todo                                                                     7 6 6 6 6 6 6


# n=6
# for i in range(1,n+1):
#     for j in range(1,n+2):
#         if(i%2!=0):
#             if(j==n+1):print(i+1,end=' ')
#             else:print(i,end=' ')
#         else:
#             if(j==1):print(i+1,end=' ')
#             else:print(i,end=' ')
#     print()
# !   optimized one
# for i in range(1,n+1):
#     for j in range(1,n+2):
#         if(i % 2 != 0 and j == n+1 or (i % 2 == 0 and j == 1)):
#             print(i+1, end=' ')
#         else:
#             print(i,end=' ')
#     print()


#?                                                                                  6
#todo                                                                             5 6 5
#todo                                                                           4 5 6 5 4
#todo                                                                         3 4 5 6 5 4 3
#todo                                                                       2 3 4 5 6 5 4 3 2
#?                                                                        1 2 3 4 5 6 5 4 3 2 1


# n=6
# N=2*n-1
# for i in range(n):
#     a=0
#     for j in range(1,N+1):
#         if(j <= n and j >= n-i):
#             print(j,end=' ')
#         elif(j>n and j<=n+i):
#             a+=2
#             print(j-a,end=' ')
#         else:print(' ',end=' ')
#     print()


#todo                                                                               1
#todo                                                                             2 1
#?                                                                              1 2 3
#?                                                                            4 3 2 1
#todo                                                                       1 2 3 4 5
#todo                                                                     6 5 4 3 2 1


# n=6
# for i in range(n):
#     if(i%2==0):sum=0
#     else:sum=i+1
#     for j in range(1,n+1):
#         if(i%2==0 and(j>=n-i and j<=n)):
#             sum+=1
#             print(sum,end=' ')
#         elif(i%2!=0 and (j>=n-i and j<=n)):
#             print(sum,end=' ')
#             sum-=1
#         else:print(' ',end=' ')
#     print()
            

#todo                                                                     1 2 3 4 5 6
#todo                                                                     6 5 4 3 2
#?                                                                        1 2 3 4
#?                                                                        6 5 4
#todo                                                                     1 2
#todo                                                                     6
# n = 6
# for i in range(n):
#     num=n
#     for j in range(1,n+1):
#         if(i%2==0 and j<=n-i):
#             print(j,end=' ')
#         elif(i%2!=0 and j<=n-i):
#             print(num,end=' ')
#             num-=1
#     print()

#todo                                                                     1  3  5  7  9  11
#todo                                                                     2  4  6  8  10 12
#?                                                                        13 15 17 19 21 23
#?                                                                        14 16 18 20 22 24
#todo                                                                     25 27 29 31 33 35
#todo                                                                     26 28 30 32 34 36


# n=6
# odd,even=1,0
# for i in range(1,n+1):
#     for j in range(n):
#         if(i%2==0):
#             even+=2
#             print(even,end=' ')
#         else:
#             print(odd,end=' ')
#             odd+=2
#     print()
#todo                                                                               1
#todo                                                                             1 2 1
#?                                                                              1 2 3 2 1
#?                                                                            1 2 3 4 3 2 1
#todo                                                                       1 2 3 4 5 4 3 2 1
#todo                                                                     1 2 3 4 5 6 5 4 3 2 1

# n=6
# N=2*n-1
# for i in range(n):
#     num=0
#     for j in range(1,N+1):
#         if(j>=n-i and j<=n):
#             num+=1
#             print(num,end=' ')
#         elif(j>n and j<=n+i):
#             num-=1
#             print(num,end=' ')
#         else:print(' ',end=' ')
#     print()

#!                                                                        U T S R Q P
#!                                                                        O N M L K
#*                                                                        J I H G
#*                                                                        F E D
#!                                                                        C B
#!                                                                        A

# n=6
# N=((n*(n+1))//2)-1
# for i in range(n):
#     for j in range(1,n+1):
#         if(j<=n-i):
#             print(chr(65+N),end=' ')
#             N-=1
#     print()

#!                                                                        a
#!                                                                        b c
#*                                                                        d e f
#*                                                                        g h i j
#!                                                                        k l m n o
#!                                                                        p q r s t u
# n=6
# sum=0
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(chr(97+sum),end=' ')
#         sum+=1
#     print()


#!                                                                             a
#!                                                                            B c
#*                                                                           D e F
#*                                                                          g H i J
#!                                                                         k L m N o
#!                                                                        P q R s T u
# n=6
# N=2*n-1
# sum=0
# for i in range(n):
#     a=n-i
#     for j in range(1,N+1):
#         alpha=97+sum
#         if(alpha % 2 != 0 and (j == a and a <= n+i)):
#             print(chr(alpha),end='')
#             a+=2
#             sum += 1
#         elif(alpha % 2 == 0 and (j == a and a <= n+i)):
#             print(chr(alpha).capitalize(), end='')
#             a+=2
#             sum+=1
#         else:print(' ',end='')
#     print()

#!                                                                      A B C D E F E D C B A
#*                                                                        A B C D E D C B A
#!                                                                          A B C D C B A
#*                                                                            A B C B A
#!                                                                              A B A
#*                                                                                A
# n=5
# N=2*n-1
# for i in range(n):
#     alpha=64
#     for j in range(1,N+1):
#         if(j>i and j<=N-i):
#             if(j<=n):
#                 alpha+=1
#                 print(chr(alpha),end=' ')
#             else:
#                 alpha-=1
#                 print(chr(alpha),end=' ')
#         else:
#             print(' ',end=' ')
#     print()

#!                                                                      A B C D E F E D C B A
#*                                                                        B C D E F E D C B
#!                                                                          C D E F E D C
#*                                                                            D E F E D
#!                                                                              E F E
#*                                                                                F
# n = 5
# N = 2*n-1
# for i in range(n):
#     alpha = 64+i
#     for j in range(1, N+1):
#         if(j > i and j <= N-i):
#             if(j <= n):
#                 alpha += 1
#                 print(chr(alpha), end=' ')
#             else:
#                 alpha -= 1
#                 print(chr(alpha), end=' ')
#         else:
#             print(' ', end=' ')
#     print()


#!                                                                       A Z B Y C X D W
#!                                                                         E V F U G T H
#*                                                                           S I R J Q K
#*                                                                             P L O M N
#*                                                                               N M O L
#!                                                                                 P K Q
#!                                                                                   J R
#!                                                                                     I

# n=8
# first=65
# last=90
# count=1
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if(j>=i and count%2!=0):
#             print(chr(first),end=' ')
#             first+=1
#             count+=1
#         elif(j>=i and count%2==0):
#             print(chr(last),end=' ')
#             last-=1
#             count+=1
#         else:
#             print(' ',end=' ')
#     print()