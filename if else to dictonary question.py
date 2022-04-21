'''Question 9  Take a user input of three-digit numbers and print their reverse output. 
Ex. input  654
       Output 456'''


# number=int(input("enter any number:-"))
# if number>=100 and number<1000:
#     a=number%10
#     number//=10
#     b=number%10
#     c=number//10
#     d=(a*100+b*10+c*1)
#     print("this is reverse of",d)
# else:
#     print("wrong reverce number")


'''Question 10 Take a user input and display the last digit of the number and check if the last digit of 
the number is 3 or not?'''

# number=int(input("enter any number:-"))
# if number%10==3:
#     print("the last digit of number is 3")
# else:
#     print("the last digit of number is not a 3")    


'''Question 11 Check the flow of the program and give output….'''

# if (True):
#      print("hello")
# if (True):
#     print("hii")
# elif(True):
#     print("Byee")
# if (True):
#     print("bye")
# else:
#     print("oho")
# if (True):
#     print("i am again")


'''Question 5 while signing up at any webpage you must have noticed the conditions for password validation
websites. This task is the same idea to develop through coding by you people. Below are the instructions
were given to you to make the password strong.'''

'''Question 1 Given a two Python list. Write a program to iterate both lists simultaneously and display
items from list1 in original order and items from list2 in reverse order.
Input 
list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]
Output 
10 400
20 300
30 200
40 100'''

# list1 = [10, 20, 30, 40]
# list2 = [100, 200, 300, 400]
# i=0
# while i<len(list1):
#     print(list1[i],list2[-(i+1)])
#     i+=1


'''Question 2. Write a program to separate the character and numeric value from a given list and store 
them in a separate list.
    A = [1,’f’,2,’b’,3,4,’h’,j’,6,9,0,’k’]'''

# A = [1,'f',2,'b',3,4,'h','j',6,9,0,'k']
# i=0
# j=[]
# k=[]
# while i<len(A):
#     if type(A[i])==int:
#         j.append(A[i])
#     else:
#         k.append(A[i])
#     i+=1
# print(j)  
# print(k) 
     

'''Question 3  Given an array arr[] of N positive integers. The task is to find the maximum for every
adjacent pair in the array.
Input [1,2,2,3,4,5]
Output [2,2,3,4,5]'''

# list= [9,2,2,3,4,5]
# i=1
# l=[]
# while i<len(list):
#     if list[i]<list[i-1]:
#         l.append(list[i-1])
#     else:
#         l.append(list[i]) 
#     i+=1
# print(l)          



'''Question 4 Given 3 digits a, b, and c. The task is to find all the possible combinations from these
digits.Input [0, 9, 5]
Output:
0 9 5
0 5 9
9 0 5 
9 5 0
5 0 9
5 9 0'''

# list=[0,9,5]
# i=0
# while i<len(list):
#     j=0
#     while j<len(list):
#         k=0
#         while k<len(list):
#             if list[i]!=list[j] and list[j]!=list[k] and list[i]!=list[k]:
#                 print(list[i],list[j],list[k])
#             k+=1
#         j+=1
#     i+=1


'''Question 5 Write a program for sum of this list
List = [1,2,[3,2,[5,6],3[4]]89,80]'''

# List =[1,2,[3,2,[5,6],3,[4]],89,80]
# i=0
# sum=0
# while i<len(List):
#     if type(List[i])==list:
#         j=0
#         while j<len(List[i]):
#             if type(List[i][j])==list:
#                 k=0
#                 while k<len(List[i][j]):
#                     sum=sum+List[i][j][k]
#                     k+=1
#             else:
#                 sum=sum+List[i][j] 
#             j+=1
#     else:
#         sum=sum+List[i]  
#     i+=1
# print(sum)       



'''Question 6 Write a Python program to find the list in a list of lists whose sum of elements is the
highest.
Sample lists: [[1,2,3], [4,5,6], [10,11,12], [7,8,9]]
Expected Output: [10, 11, 12]'''

# lists=[[1,2,3], [4,5,6], [10,11,12], [7,8,9]]
# i=0
# maxim=0
# maximum_list=lists[i]
# while i<len(lists):
#     j=0
#     sum=0
#     while j<len(lists[i]):
#         sum=sum+lists[i][j]
#         j+=1
#     if sum>maxim:
#         maxim=sum
#         maximum_list=lists[i]
#     i+=1
# print(maximum_list)


'''Question 6 Write a Python program to round the numbers of a given list, print the minimum and maximum 
numbers and multiply the numbers by 5. Print the unique numbers in ascending order separated by space.
Original list: [22.4, 4.0, 16.22, 9.1, 11.0, 12.22, 14.2, 5.2, 17.5]
Minimum value: 4
Maximum value: 22
Result:
20 25 45 55 60 70 80 90 110'''

# Original_list=[22.4, 4.0, 16.22, 9.1, 11.0, 12.22,14.2, 5.2, 17.5]
# i=0
# min=Original_list[i]
# maximum=Original_list[i]
# while i<len(Original_list):
#     if Original_list[i]>maximum:
#         maximum=Original_list[i]
#     elif Original_list[i]<min:
#         min=Original_list[i]    
#     i=i+1
# print(int(maximum))
# print(int(min))
# j=0
# l=[]
# while j<len(Original_list):
#     l.append((int(Original_list[j])*5))
#     j+=1
# s=0
# while s<len(l):
#     a=0
#     while a<len(l):
#         if l[s]<l[a]:
#             tem=l[s]
#             l[s]=l[a]
#             l[a]=tem
#         a+=1
#     s+=1
# print(l)


'''Question 7 Write a Python program to find the list with maximum and minimum length. 
Original list:
[[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
List with maximum length of lists:
(3, [13, 15, 17])
List with minimum length of lists:
(1, [0])'''


# Original_list=[[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
# i=0
# maxim=len(Original_list[0])
# maximum_list=Original_list[0]
# minimum=len(Original_list[0])
# minimum_list=Original_list[0]
# while i<len(Original_list):
#     if (len(Original_list[i]))>maxim:
#         maxim=len(Original_list[i])
#         maximum_list=Original_list[i]
#     elif (len(Original_list[i]))<minimum:
#         minimum=len(Original_list[i])
#         minimum_list=Original_list[i]    
#     i+=1
# print(maximum_list)
# print(minimum_list)


# '''Question 8 Write a Python program to split a list every Nth element. 
# Sample list: ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
# Expected Output: [['a', 'd', 'g', 'j', 'm'], ['b', 'e', 'h', 'k', 'n'], ['c', 'f', 'i', 'l']'''

# i=0



            








