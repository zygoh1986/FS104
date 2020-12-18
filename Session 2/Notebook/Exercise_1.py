#Exercise_Data types.ipynb

#Question 1
#Use float() to create a number from a string like '12.34'. Make sure the result is really a number!

stringnum = '12.34'
print(float(stringnum))

#Question 2
#Try using int() to create an integer from a decimal number like 56.78. Did the answer get rounded up or down?
#ANSWER: round down

floatint = 56.78
print(int(floatint))

#Question 3
#Try using int() to create an integer from a string. Make sure the result is really an integer!

intstring = '20'
print(int(intstring))

#Question 4 
# Which of the following are valid string literals in Python.

# (a) "Hello"
# (b) 'hello'
# (c) "Hello'
# (d) 'Hello there'
# (e) ''
#Answer: (a) & (b) & (c)


#Exercise_Variables.ipynb

# Question 1
# How do you tell Python that a variable is a string (characters) instead of a number?
#ANSWER: String in python are surrounded by either single quotation or double quotation marks


# Question 2
# Once you have created a variable, can you change the value that is assigned to it?
#ANSWER: Yes, re-declare the same variable name with a different value. 

# Question 3
# With variable names, is TEACHER the same as TEACHEr?
#ANSWER: No not the same. It's case sensitive

# Question 4
# Is 'Blah' the same as "Blah" to Python?
#ANSWER: Yes, same. Both are strings

# Question 5
# Is '4' the same as 4 to Python?
#ANSWER: Different. '4' - String and 4 - Its integer

# Question 6
# Which of the following is not a correct variable name? Why?

# a) Teacher2 
# b) 2Teacher 
# c) teacher_25 
# d) TeaCher

#ANSWER: (B) - Invalid Syntax

# Question 7
# Is "10" a number or a string?
#ANSWER: String

# Question 8
# What is the value of variable n after the following instructions are executed?
#ANSWER: 50 (5*10)

j=5
k=10
n=j*k

print(n)

# Question 9
# What's the output of following code if the user enters 24 in response to the input prompt.
#ANSWER: Output: "You are 24 years old". 24 become a string and print into a sentence. 

age = input('How old are you?: ') 
print('You are', age, 'years old')