# Write a Python function find_missing_number(arr, n) that takes in a list of integers arr containing n-1 distinct numbers from 1 to n, with one number missing. The function should return the missing number.
"""
# Missing number in a list
def find_missing_number(arr, n):
    total_sum = n * (n + 1) // 2
    arr_sum = sum(arr)
    return total_sum - arr_sum

# Example usage
arr = [1, 2, 3, 4, 6]
n = 6
print(find_missing_number(arr, n))  # Output: 3
 """
        #                   or

# Missing number in a list
"""
list =[1,2,4,5]
n= 5

num = n * (n+1)//2
list_num =sum(list)
total = num -list_num
print(total)
"""

# find the second largest number in a list
"""
a=[10,31,94,53,64,54,]
a.sort()
print(a[-1])
"""

"""
a = list(map(int, input().split()))
a = list(map(int, input().split()))
a.sort()
print(a[-1])

print(a) 

"""

# count the digit of a  number

"""
num=int(input("enter the number:"))
count =0 
while num>0:
    num=num//10
    count+=1
print(count)
"""
#                           or
"""
num=int(input("enter the number:"))
a = str(num)
total= len(a) 
print(total)
"""

# find out the min number in a list without using min() function
"""
# num = list(map(int,input().split(sep=",")))
# print(num)
num =[22,24,54,2,24,23]
min =num[0]

for i in num:
    if i<min:
        min = i
print(min)

"""

# find out the max number in a list without using min() function
"""

num =[18,9,14,5]
lar =0

for i in num:
    if i>lar:
        lar =i 
print(lar)

"""

"""
num =[18,9,14,5]
lar =max(num)
print(lar)

"""

# reserve the number without using reverse() function 
"""
rev = int(input("enter the number:"))
string =str(rev)
rev1 =string[::-1]
print(rev1)

"""


# reserve the string without using reverse() function 
"""
rev = input("enter the string:")
rev1 =rev[::-1]
print(rev1)


a=input()
res=""
for i in a:
    res= i+res
print(res)
"""


# armstrong number
"""
num = int(input("enter the number:"))
sum =0
temp =num
while temp>0:
    dig = temp%10
    sum = sum + (dig**3)
    temp = temp //10

if num ==sum:
    print("it is armstrong")
else:
    print("it is not armstrong")

"""
# check the prime num or not
"""
num = int(input("enter the number:"))
count = 0
for i in range(1,num+1):
    if num%i ==0:
        count = count+1
if count == 2:
    print("prime")
else:
    print("not prime")
"""
#factorial number
"""
num =int(input("enter the number:"))
fact =1


for i in range(1,num+1):
    fact = fact * i
print(fact)
"""


# fibonnaci sequence
"""
num = int(input("enter the number:"))
fib =[0,1]
for i in range(2,num):
    next = fib[i-2]+fib[i-1]
    fib.append(next)
print(fib)
"""


# sum of list 
"""
sum =[1,2,3,4,6]
total =0
for i in sum:
    total = i +total
print(total)

"""

#for loop - square of number
"""
for i in range(1,11):
    print("square is",i, "is",i*i)

"""

# linear search - find the element in the list
"""
list =[1,23,45,55,26,52,34]
print(list)
num =int(input("enter the number:"))
for i in range(len(list)):
    if list[i] == num:
        print(num,"is present in the list at index is",i)
        break
else:
    print(num,"is not present in the list at no index ")
    
"""

# word count 
 

"""
from collections import Counter

text = input("enter the value:")
str = Counter(text.split())
print(str)
"""

#print the first 10 natural number using while loop

"""
n =1
while n<=10:
    print(n)
    n=n+1
"""

# for loop - table

"""
n=int(input("enter the table:"))

for i  in range(1,11):
    print(n,"*",i,"=",n*i)
"""


# find the duplicates in a list 
""""
# num = list(map(int,input().split()))

num =[1,2,4,1,2,6,8,6,5,9,]
same =[]
dup=[]

for i in num:
    if i not in same:
        same.append(i)
    elif i not in dup:
        dup.append(i)
        
# print(same)
print(dup)
"""


# write A program  remove duplicates in a list 
"""
num =list(map(int,input().split()))

original =[]

for i in num:
    if i not in original:
        original.append(i)
print(original)

"""
"""
num =[32,44,31,2,2,4,42,4,24,4,22]

a=set(num)
b=list(a)
print(b)
"""

# find the length of string without len()
"""
str = input("enter the value:")
count = 0

for i in str:
    count+=1
print(count)

"""

# write a program to square the number in a list 
"""
num = list(map(int,input().split()))

square_num =[]
for i in num:
    square_num.append(i*i)

print(square_num)


"""

start = int(input("enter the number:"))
end = int(input("enter the number:"))


for i in range(start,end+1):
    if i>1:
        for j in range(2,i):
            if i%j ==0:
                break
        else:
            print(i , end=" ")












# prime num between the given range 

# start = int(input())
# end = int(input())
# for i in range(start,end+1):
#     if i>1:
#         count =0
#         for j in range(2,i):
#             if i%j==0:
#                 count = count+1
#         if count ==0:
#             print(i,end=" ")
            

# arr = [10, 2, 45, 67, 23, 89, 1]

# for i in range(len(arr)):
   
#     min_index = i
#     for j in range(i + 1, len(arr)):
#         if arr[j] < arr[min_index]:
#             min_index = j
    
#     # Swap the found smallest element with the first element of the unsorted part
#     arr[i], arr[min_index] = arr[min_index], arr[i]

# print("List sorted from low to high:", arr)


# def sort_list_asc_to_desc(lst):
#     # Sort the list in ascending order
#     for i in range(len(lst)):
#         for j in range(i + 1, len(lst)):
#             if lst[i] > lst[j]:
#                 lst[i], lst[j] = lst[j], lst[i]
    
#     # Sort the list in descending order
#     for i in range(len(lst)):
#         for j in range(i + 1, len(lst)):
#             if lst[i] < lst[j]:
#                 lst[i], lst[j] = lst[j], lst[i]
    
#     return lst

# # Example usage
# my_list = [4, 1, 8, 3, 9, 2]
# sorted_list = sort_list_asc_to_desc(my_list)
# print("List sorted from ascending to descending:", sorted_list)
