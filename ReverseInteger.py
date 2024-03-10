#Question 5:Reverse Integer
#Write a program that takes an integer and returns an integer with reversed digit ordering.
def reverse_integer(n):
    if n<0:
        return int(str(n)[::-1].replace('-',''))
    else:
        return int(str(n)[::-1])
num=int(input("Enter an integer:"))
reversed_num=reverse_integer(num)
print(reversed_num)
    
