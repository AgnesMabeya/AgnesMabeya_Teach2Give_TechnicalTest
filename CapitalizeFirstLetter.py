#Question 4:Capitalize Words
#Write a program that accepts string as,capitalizes the first letter of each word in the string, and then returns the returns the result string
def capitalize_first_letter(sentence):
    words=sentence.split()
    capitalized_words=[word.capitalize() for word in words]
    return" ".join(capitalized_words)
input_string=input("Enter a string:")
result=capitalize_first_letter(input_string)
print(result)
