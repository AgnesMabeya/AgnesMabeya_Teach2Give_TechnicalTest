#Question 3:Power Of Two
#Write a program that takes an integer as input and returns true if the input is a power of two.
def power_of_two(n):
    if n <=0:
        return False
    return(n&(n-1))==0
num=int(input("Enter an integer:"))
print(power_of_two(num))
    
