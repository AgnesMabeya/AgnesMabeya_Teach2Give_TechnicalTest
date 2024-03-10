#Question 2:Fibonacci Sequence
#Write a program to generate the Fibonacci sequence up to 100.
a,b = 0,1
print(a)
print(b)
while a+b <= 100:
    c = a+b
    print(c)
    a,b = b,c
