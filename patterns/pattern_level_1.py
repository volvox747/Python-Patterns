
#!                                                   *                          * 
#!                                                   **                        **
#!                                                   ***                      ***
#!                                                   ****                    ****
#?                                                   *****         and      *****
#!                                                   ****                    ****
#!                                                   ***                      ***
#!                                                   **                        **  
#!                                                   *                          *    

# import math
# n=5
# N=(2*n)-1
# a=2
# for i in range(1,N+1):
#     if(i>n):
#         print(('*'*(i-a)).rjust(n))
#         a+=2
#     else:print(('*'*i).rjust(n))
# b=2
# for i in range(1, N+1):
#     if(i > n):
#         print('*'*(i-b))
#         b += 2
#     else:
#         print('*'*i)




#!                                                     *                      ******                                                                         
#!                                                    **                       *****          
#?                                                   ***           and          ****        
#?                                                  ****                         ***       
#!                                                 *****                          **      
#!                                                ******                           *    
# n=6
# for i in range(1,n+1):
#     print(('*'*i).rjust(n))
# for i in range(1, n+1):
#     print(('*'*(n+1-i)).rjust(n))






#!                                                   *                                     ***********       
#!                                                  ***                                     ********* 
#?                                                 *****               and                   *******          
#?                                                *******                                     *****             
#!                                               *********                                     ***             
#!                                              ***********                                     *       
# n=6
# for i in range(n,0,-1):
#     print(('*'*(2*i-1)).center(n*2-1))
# for i in range(0,n+1):
#     print(('*'*(2*i-1)).center(n*2-1))







#!                                                   *                                     * * * * * *            
#!                                                  * *                                     * * * * *             
#?                                                 * * *               and                   * * * *                 
#?                                                * * * *                                     * * *                     
#!                                               * * * * *                                     * *                    
#!                                              * * * * * *                                     *                    
# n=10
# for i in range(1,n+1):
#     print(('* '*i).center(n*2-1))
# for i in range(n,-1,-1):
#     print(('* '*i).center(n*2-1))





#!                                                                   *******
#!                                                                    *****
#?                                                                     ***
#?                                                                      *
#?                                                                     ***
#!                                                                    *****
#!                                                                   *******   


# n=9
# N=2*n-1
# for i in range(0,N):
#     if(i>n-1):
#         N+=2
#         print(('*'*N).center(2*n-1,))
#     else:
#         print(('*'*N).center(2*n-1,))
#         N=abs(N-2)



#!                                                                        *         *
#!                                                                         *       *   
#!                                                                          *     *    
#?                                                                           *   *     
#?                                                                            * *          
#*                                                                             *                
#?                                                                            * *                                
#?                                                                           *   *        
#!                                                                          *     *         
#!                                                                         *       *  
#!                                                                        *         *  


# n=11
# N=2*n-1
# for i in range(1,N+1):
#     if(i<n):
#         N-=2
#         print(('*'+(' '*N)+'*').center(2*n-1))
#     elif (i==n):
#         N-=2
#         print('*'.center(2*n-1))
#     else:
#         N+=2
#         print(('*'+(' '*N)+'*').center(2*n-1))

        




#!                                                                                *
#!                                                                                * 
#!                                                                                *
#?                                                                             *******
#!                                                                                *
#!                                                                                *
#!                                                                                *     



# n=6
# N=2*n-1
# for i in range(1,N+1):
#     if(i<n):print('*'.center(N))
#     elif (i==n):print(('*'*N).center(N))
#     else:print('*'.center(N))
        


#?                                                                             ******* 
#!                                                                             *     *  
#!                                                                             *     *  
#!                                                                             *     *
#!                                                                             *     *
#!                                                                             *     *
#?                                                                             *******     





# class Rectangle():
#     def __init__(self,n):
#         self.n=n
#     def solve(self):
#         N=2*self.n-1
#         for i in range(1,N+1):print('*'*N) if(i==1 or i==N) else print('*'+(' '*(N-2))+'*')
# r=Rectangle(4)
# r.solve()





#!                                                                               * 
#!                                                                              * * 
#?                                                                             *   *
#?                                                                            *     * 
#!                                                                           *       *
#!                                                                          * * * * * * 

# n=6
# N=2*n-1
# for i in range(n):
#     if(i==0):print('*'.center(N))
#     elif (i==n-1):print(('* '*n))
#     else:print(('*'+" "*(2*i-1)+'*').center(N))







#?                                                                            * * * * * *
#!                                                                           *         * 
#!                                                                          *         *  
#!                                                                         *         *   
#!                                                                        *         *    
#?                                                                       * * * * * *      


# n=6
# N=2*n-1
# for i in range(n-1,-1,-1):    
#     if(i==0 or i==n-1):print((('*'+'-')*n).rjust(N+i+1,'-'))
#     else:print(('*'+" "*(N-2)+'*').rjust(N+i,'-'))







#?                                                                        5
#todo                                                                     5 5
#todo                                                                     5 5 5
#todo                                                                     5 5 5 5
#?                                                                        5 5 5 5 5


# n=5
# for i in range(n):
#     print((str(n)+' ')*(i+1))




#todo                                                                      1 1 1 1 1
#?                                                                         2 2 2 2 2
#todo                                                                      3 3 3 3 3
#?                                                                         4 4 4 4 4
#todo                                                                      5 5 5 5 5

# n=3
# for i in range(n):
#     print((str(i+1)+' ')*n)


#todo                                                                       1
#?                                                                          1 2
#todo                                                                       1 2 3
#?                                                                          1 2 3 4
#todo                                                                       1 2 3 4 5   


# from abc import ABC,abstractmethod
# class Pattern(ABC):
#     def __init__(self,n):
#         self.n=n
#     @abstractmethod
#     def calc():pass
# class Number(Pattern):
#     def __init__(self,n):
#         super().__init__(n)
#     def calc(self):
#         for i in range(1,self.n+1): 
#             for j in range(1,i+1):
#                 print(str(j),end=' ')
#             print()
# n=Number(5)
# n.calc()



#todo                                                                          1 2 3 4 5 6 
#todo                                                                            2 3 4 5 6
#?                                                                                 3 4 5 6
#?                                                                                   4 5 6
#todo                                                                                  5 6
#todo                                                                                    6


# n=10
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if(j>=i):print(j,end=' ')
#         else:print(' ')
#     print()


#todo                                                                                    6
#todo                                                                                   6 5
#?                                                                                     6 5 4
#?                                                                                    6 5 4 3
#todo                                                                                6 5 4 3 2
#todo                                                                               6 5 4 3 2 1



# n=10
# b=n
# for i in range(n,0,-1):
#     a=1
#     while(a<b):
#         print(end=' ')
#         a+=1
#     for j in range(n,i-1,-1):print(j,end=' ')
#     b-=1
#     print()


#todo                                                                          1 1 1 1 1 1 1 1 1 1
#todo                                                                          1 0 0 0 0 0 0 0 0 1
#?                                                                             1 0 0 0 0 0 0 0 0 1
#?                                                                             1 0 0 0 0 0 0 0 0 1
#?                                                                             1 0 0 0 0 0 0 0 0 1
#?                                                                             1 0 0 0 0 0 0 0 0 1
#todo                                                                          1 0 0 0 0 0 0 0 0 1
#todo                                                                          1 1 1 1 1 1 1 1 1 1


# n=10
# for i in range(1,n+1):
#     if(i==1 or i==n):
#         print('1 '*n)
#     else:print('1 '+'0 '*(n-2)+'1')


#todo                                                                                1
#todo                                                                                1 0
#todo                                                                                1 0 1
#?                                                                                   1 0 1 0
#?                                                                                   1 0 1 0 1
#todo                                                                                1 0 1 0 1 0
#todo                                                                                1 0 1 0 1 0 1



# n=7
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(0, end=' ') if(j % 2 == 0) else print(1,end=' ')
#     print()


#todo                                                                               1 1 1 1 1 1
#?                                                                                  0 0 0 0 0 0
#todo                                                                               1 1 1 1 1 1
#?                                                                                  0 0 0 0 0 0
#todo                                                                               1 1 1 1 1 1
#?                                                                                  0 0 0 0 0 0


# n=6
# for i in range(1,n+1):print('0 '*n) if(i%2==0) else print('1 '*n)




#todo                                                                                       1
#todo                                                                                      1 1
#?                                                                                        1 0 1
#?                                                                                       1 0 0 1
#todo                                                                                   1 0 0 0 1
#todo                                                                                  1 1 1 1 1 1

# n=4
# b=n
# for i in range(1,n+1):
#     if(i==n):
#         print('1 '*n)
#         break
#     a=1
#     while(a<b):
#         print(end=' ')
#         a+=1
#     for j in range(1,i+1):print(1, end=' ') if(j == 1 or j == i) else print(0, end=' ')
#     b-=1  
#     print()

#*                                                                                   A A A A A
#!                                                                                   B B B B B
#*                                                                                   C C C C C
#!                                                                                   D D D D D
#*                                                                                   E E E E E

# n=5
# for i in range(n):
#     print((chr(65+i)+' ')*n)




#!                                                                                   A B C D E
#*                                                                                   A B C D E
#!                                                                                   A B C D E
#*                                                                                   A B C D E
#!                                                                                   A B C D E

# n=6
# for i in range(1,n+1):
#     for j in range(n):
#         print(chr(65+j),end=' ')
#     print()
