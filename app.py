# Task 1
subject_marks = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
subject_marks.sort(key=lambda key: key[1])
print(subject_marks)
print()

# Task 2
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filtered = list(filter(lambda num: (num % 2 == 0), numbers))
print(filtered)
print()

# Task 3
""" 
def protected(name, password):
    if name == 'admin' and password == 'admin':
        return private
    else:
        return 'You are not authorized'

def public():
    print("Hello World!")

@protected
def private():
    print("Welcome, admin!")

public(name='admin', password='admin')
private(name='sdcd', password='wdew') """


""" def foo(num):
    while 5 <= num <= 15:
        print(num)
        num += 1
print(str(foo(5))) """

""" def countdown(n):
    for i in range(n,0,-1):
        print(i)
countdown(5) """
   
# using lambda
""" countdown1 = lambda n:[i for i in range(n,0,-1)]
print(countdown1(7))

# using recursion
def countdown_r(n):
    print(n)
    if n>1:
        countdown_r(n-1)

countdown_r(6)

def seq_sum(n):
    s = 0
    for i in range(0,n+1):
        s += i
    return s
print(seq_sum(5))

def seq_sum_r(n):
    if n>0: # base case
        return n + seq_sum_r(n-1) # recursion
    else:
        return 0

print(seq_sum_r(5)) """


# num_n = int(input('n: '))
# num_m = int(input('m: '))

# def num_power():
#     return num_n ** num_m

# print(num_power())

# def power(m,n):
#     p=1
#     for i in range(0,1):
#         p*=m
#     return p

# def pow_r(m,n):
#     if m==0:
#         return 1
#     else:
#         return m * pow_r(m,n-1)

""" def fact_foo(num):
    if num == 1:
        return num
    else:
        return num * fact_foo(num-1)
    
print(fact_foo(7))
print()

def facto(n):
    f=1
    for i in range(n,0,-1):
        f *= i
    return f

print()
numb=5
factor=1
for i in range(1,numb+1):
    factor = i*factor
print(factor)
print()


nterms = int(input("How many terms? "))
n1, n2 = 0, 1
count = 0
while count < nterms:
       print(n1)
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       count += 1

print()

def recur_fibo(n):
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))

for i in range(nterms):
       print(recur_fibo(i))  

print() """


my_string = 'Hello, world!'
def check_frequency(my_str,my_ch):
   if not my_str:
      return 0
   elif my_str[0]==my_ch:
      return 1 + check_frequency(my_str[1:],my_ch)
   else:
      return check_frequency(my_str[1:],my_ch)

print("The frequency of " + '"l"' + " is :")
print(check_frequency(my_string,'l'))
print()

string1="Hello, world!"
list1=[]
list2=[]
for i in string1:
  if i not in list1:
    list1.append(i)#appending unique characters of string
    list2.append(string1.count(i))
#finding maximum in the list
occ=max(list2)
ele=list1[list2.index(occ)]
print(ele,occ)
