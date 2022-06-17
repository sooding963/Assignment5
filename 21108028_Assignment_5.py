#QUESTION 1
s=str(input("Enter a String :"))
d=s[::-1]
print("The reverse string is :", d)

#QUESTION 2
lower=int(input("Enter lower range limit:"))
upper=int(input("Enter upper range limit:"))
n=int(input("Enter the number to be divided by:"))
for i in range(lower,upper+1):
    if(i%n==0):
        print(i)
        
#QUESTION 3
import math
a = int(input("Enter length of first side of the triangle:"))
b = int(input("Enter length of second side of the triangle:"))
c = int(input("Enter length of third side of the triangle:"))
s = (a+b+c)/2   # s = semi-perimeter
if a < b+c and b < a+c and c < a+b:    #checks if the sides can form a triangle.
    A = math.sqrt(s*(s-a)*(s-b)*(s-c))
    print("Area of the trianle is",A)
else:
    print("Not a valid triangle!")
    
#QUESTION 4
for i in range(1,6):
    for i in range(1,i+1):
        print('*',end=' ')
    print()
for j in range(4,0,-1):
    for k in range(j):
        print('*',end=' ')
    print()
    
    
#QUESTION 5 
n = int(input("Enter number of rows:"))
k = 65
for i in range(n):
    for j in range(i+1):
        print(chr(k), end=" ")
        k = k + 1
    print()

#QUESTION 6
print("Prime numbers in an input range.")
start = int(input("Enter starting of range(>=2):"))
end = int(input("Enter ending of range:"))
for i in range(start,end+1):
    for j in range(2,i):
        if i % j == 0:
            break
    else:
        print(i)
    
#QUESTION 7
for i in range(1, 501):
    if i % 7 == 0 and i % 11 == 0:
        print(i)

#QUESTION 8
i = 10
l = []
p = []
n = []
odd = []
even = []
Dict = {}
while i > 1:
    num = int(input("Enter integer:"))
    l.append(num)       # make an original list with user inputted integers
    i -= 1
for j in l:
    if j >= 0:          # adds to positive integers list
        p.append(j)
    if j < 0:           # adds to negative integers list
        n.append(j)
    if j % 2 != 0:      # adds to odd integers list
        odd.append(j)
    if j % 2 == 0:      # adds to even integers list
        even.append(j)
    Dict[j] = l.count(j)
print("a) Positive integers:", p)
print("b) Negative integers:", n)
print("c) Odd integers:", odd)
print("d) Even integers:", even)
print('e)')
for k in Dict:
    print(f'integer:{k} ; number of times it occurs: {Dict[k]}')

#QUESTION 9
list=input('Enter the words in space separated format : ').split()
d={}                # dictionary to count number of occurences
for i in list:
    if i in d:      # if key already in d, then increment count by 1
        d[i]+=1
    else:           # if key not in d, then count is 1
        d[i]=1
print(d) 
