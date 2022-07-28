# a lambda function to calcuate sum of two numbers.
# f=lambda x,y,z: x+y+z  # write lambda function
# s=lambda x,y,z: x*y*z   #write lambda function
# r=f(3,10,2)   #call lambda function
# z=s(2,3,5)
# print('sum =',r)     sum = 15
# print('mul =',z)     mul = 30


# a lambda function that returns bigger number
# m= lambda x, y: x if x>y else y     #write a lambda function
# x,y= [int(n)for n in input("enter two numbers: ").split()]         #enter two numbers: 8 12
# print(m(x,y))                         # 12

# m= lambda x, y: x if x>y else y                                 
# x,y= [int(n)for n in input("enter two numbers: ").split()]   #enter two numbers: 4 7      
# print(m(x,y))                  #7


# a=[int(n)for n in input("enter two numbers: ").split()]     #enter two numbers: 5 8
# print('Bigger number is: ',max(a))                      Bigger number is:  8
# print('Smaller number is: ',max(a))                     #Smaller number is:  8

# a=20,39,50
# print(max(a))         #50
# print(min(a))         #20


# a lambda function that returns even numbers from list
# a=[int(x) for x in input().split()]           2
# b=list(filter(lambda x: (x%2 == 0), a))       [2]
# c=list(filter(lambda x: (x%2 != 0), a))       []
# print(b)
# print(c)
