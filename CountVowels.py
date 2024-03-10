#Question 6:Count Vowels
#Write a program that counts the number of vowels in a sentence.
def count_vowels(sentence):
    vowels = 'aeiouAEIOU'
    count = 0
    for char in sentence:
        if char in vowels:
            count=count+1
            return count
sentence = input("Enter a sentence: ")
print("The number of vowels is: ",count_vowels(sentence))
