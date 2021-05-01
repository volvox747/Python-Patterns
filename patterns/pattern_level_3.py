
# todo                                                               1
# todo                                                               2 8
# todo                                                               3 9 14
# ?                                                                  4 10 15 19
# ?                                                                  5 11 16 20 23
# todo                                                               6 12 17 21 24 26
# todo                                                               7 13 18 22 25 27 28                                                               


n=7
for i in range(1,n+1):
    sum=i
    a=n
    for j in range(n+1):
        if(j==0):print(sum,end=' ')
        elif (j>1 and j<=i):
            a-=1
            sum=sum+a
            print(sum,end=' ')
    print()
            
# todo                                                             1
# todo                                                             2 3
# todo                                                             6 5 4
# ?                                                                7 8 9 10
# ?                                                                15 14 13 12 11
# ?                                                                16 17 18 19 20 21
# todo                                                             28 27 26 25 24 23 22
# todo                                                             29 30 31 32 33 34 35 36



n=9
a=1
mul=4
for i in range(n):
    if(i==0):
        temp=a
    elif(i>0 and i%2!=0):
        a+=1
        temp=a
    elif (i>0 and i%2==0):
        a+=mul
        temp=a
        mul+=4
    for j in range(1,i+2):
        if(i==0 and j==1):
            print(1,end=' ')
        elif(i>0 and i%2==0):
            print(temp,end=' ')
            temp-=1
        elif(i>0 and i%2!=0):
            print(temp,end=' ')
            temp+=1
    print()

# todo                                                           1
# todo                                                           2 3
# todo                                                           4 5 6
# todo                                                           7 8 9 10
# todo                                                           11 12 13 14 15
# ?                                                              16 17 18 19 20 21
# ?                                                              22 23 24 25 26 27 28
# ?                                                              22 23 24 25 26 27 28
# ?                                                              16 17 18 19 20 21
# todo                                                           11 12 13 14 15
# todo                                                           7 8 9 10
# todo                                                           4 5 6
# todo                                                           2 3
# todo                                                           1



n=7
a=1
for i in range(2*n):
    if(i<n):
        a+=i
        temp=a
    elif(i==n):temp=a
    else:
        a=a-((2*n)-i)
        temp=a
    for j in range(1,n+1):
        if(i<n and j<=i+1):
            print(temp,end=' ')
            temp+=1
        elif(i==n and j<=2*n-i):
            print(temp,end=' ')
            temp+=1
        elif(i>n and j<=2*n-i):
            print(temp,end=' ')
            temp+=1
    print()


# ?                                                              1  2  3  4  5  6  7  8  9
# todo                                                           19 20 21 22 23 24 25 26 27
# todo                                                           37 38 39 40 41 42 43 44 45
# todo                                                           55 56 57 58 59 60 61 62 63
# ?                                                              73 74 75 76 77 78 79 80 81
# todo                                                           64 65 66 67 68 69 70 71 72
# todo                                                           46 47 48 49 50 51 52 53 54
# todo                                                           28 29 30 31 32 33 34 35 36
# ?                                                              10 11 12 13 14 15 16 17 18

n=9
a=1
for i in range(n):
    if(i==0):
        temp=a
    else:
        if(n%2==0):
            if(i<n//2):
                a+=n*2
                temp=a
            elif(i==(n//2)+1):
                a -= n
                temp = a
            elif(i>(n//2)+1):
                a-=n*2
                temp=a
        else:
            if(i<=n//2):
                a+=n*2
                temp=a
            elif(i==(n//2)+1):
                a-=n
                temp=a
            elif(i>(n//2)+1):
                a-=n*2
                temp=a
    for j in range(n):
        print(temp,end=' ')
        temp+=1
    print()


# todo                                                 1  2  3  4  5  6  7  8   65 66 67 68 69 70 71 72
# todo                                                    9  10 11 12 13 14 15  58 59 60 61 62 63 64
# todo                                                       16 17 18 19 20 21  52 53 54 55 56 57
# ?                                                             22 23 24 25 26  47 48 49 50 51
# ?                                                                27 28 29 30  43 44 45 46
# todo                                                                31 32 33  40 41 42
# todo                                                                   34 35  38 39
# todo                                                                      36  37



n=8
first_half=1
second_half=n**2
for i in range(n):
    if(i>0):
        second_half-=n-i
        temp=second_half
    else:temp=second_half
    for j in range(n):
        if(j>=i):
            print(first_half,end=' ')
            first_half+=1
        else:
            print(' ',end=' ')
    for k in range(n):
        if(k<n-i):
            temp+=1
            print(temp,end=' ')
    print()

# todo                                               0
# todo                                               9 0 9
# todo                                               8 9 0 9 8
# ?                                                  7 8 9 0 9 8 7
# ?                                                  6 7 8 9 0 9 8 7 6
# ?                                                  5 6 7 8 9 0 9 8 7 6 5
# ?                                                  4 5 6 7 8 9 0 9 8 7 6 5 4
# todo                                               3 4 5 6 7 8 9 0 9 8 7 6 5 4 3
# todo                                               2 3 4 5 6 7 8 9 0 9 8 7 6 5 4 3 2


n=9
for i in range(n):
    a=10
    a-=i
    for j in range(i+(i+1)):
        if(j==i):print(a-10,end=' ')
        elif(j<i):
            print(a,end=' ')
            a+=1
        elif(j>i):
            a-=1
            print(a,end=' ')
    print()

# todo                                              3 8 1 3 8 1 8 3 0
# todo                                              8 1 3 8 1 8 3 0
# todo                                              1 3 8 1 8 3 0
# ?                                                 3 8 1 8 3 0
# ?                                                 8 1 8 3 0
# todo                                              1 8 3 0
# todo                                              8 3 0
# todo                                              3 0
# todo                                              0


n='381381830'
for i in range(len(n)):
    for j in n[i:]:print(j,end=' ')
    print() 





# ?                                                           1 0 0 9 0 0 1
# todo                                                         0 0 9 0 0 1
# todo                                                          0 9 0 0 1
# todo                                                           9 0 0 1
# todo                                                            0 0 1
# ?                                                                0 1
# ?                                                                 1
# ?                                                                0 1
# todo                                                            0 0 1
# todo                                                           9 0 0 1
# todo                                                          0 9 0 0 1
# todo                                                         0 0 9 0 0 1
# ?                                                           1 0 0 9 0 0 1




n = '1009001'
N = len(n)*2-1
for i in range(N):
    if(i <= N//2):
        index = i
    else:
        index = (N-i)-1
    for j in range(N):
        if(j >= i and j < N-i):
            if(i % 2 == 0 and j % 2 == 0):
                print(n[index], end='')
                index += 1
            elif(i % 2 != 0 and j % 2 != 0):
                print(n[index], end='')
                index += 1
            else:
                print(' ', end='')
        elif(j >= (N-i)-1 and j <= i):
            if(i % 2 == 0 and j % 2 == 0):
                print(n[index], end='')
                index += 1
            elif(i % 2 != 0 and j % 2 != 0):
                print(n[index], end='')
                index += 1
            else:
                print(' ', end='')

        else:
            print(' ', end='')
    print()







# ?                                                     ****
# !                                                    *    *
# !                                                    *    *
# !                                                    *    *
# !                                                    *    *
# ?                                                    ******
# !                                                    *    *
# !                                                    *    *
# !                                                    *    *
# !                                                    *    *   



n=20
for i in range(n):
    for j in range((n//2)+1):
        if(i==0 and (j>i and j<n//2)):print('*',end='')
        elif(i!=0 and (j==0 or j==n//2)):print('*',end='')
        elif(i==n//2):print('*',end='')
        else:print(' ',end='')
    print()


# *                                                          A B C D E F G
# !                                                          A B C D E F
# !                                                          A B C D E
# !                                                          A B C D
# !                                                          A B C
# !                                                          A B
# *                                                          A
# *                                                          A
# !                                                          A B
# !                                                          A B C
# !                                                          A B C D
# !                                                          A B C D E
# !                                                          A B C D E F
# *                                                          A B C D E F G


n='ABCDEFG'
N=len(n)*2
for i in range(N):
    index=0
    for j in range(len(n)):
        if(j<len(n)-i):
            print(n[index],end=' ')
            index+=1
        elif(i>=len(n) and j<=abs(len(n)-i)):
            print(n[index],end=' ')
            index+=1
    print()
        
