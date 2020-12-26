# #Sat_Decision.ipynb

# Question 1
# Write a program that takes input of number from user and checks whether number is positive or negative.

#ANSWER: 
number = int(input("Enter number:"))
if number > 0: 
        print("Positive") 
elif number < 0: 
        print("Negative") 
else: 
        print("Equal to zero") 


# Question 2
# Write a program that inputs a number from user and checks whether number is even or odd.

#ANSWER
number = int(input("Enter number:"))
check = number%2
if check == 0: 
        print(number, "It is a even number") 
elif check == 1: 
        print(number, "It is a odd number") 
else: 
        print("Invalid number") 



# Question 3
# Write a program that finds greatest among three numbers. 
# And output print with "The largest number is (output)"
#ANSWER

number1 = float(input("Enter first number: "))
number2 = float(input("Enter second number: "))
number3 = float(input("Enter third number: "))

if (number1 >= number2) and (number1 >= number3):
   largest = number1
elif (number2 >= number1) and (number2 >= number3):
   largest = number2
else:
   largest = number3
print("The largest number is", largest)



# Question 4
# You’re on a long car trip and arrive at a gas station. The next gas station is 200km away. Write a program to figure out if you need to buy gas here, or if you can wait for the next station. 
# The condition to buy gas here is if car is able to run at least 200km more 
# Ask user for input: How many litres of gas left in tank? How many km/litre is your car? 
# Hint: Calculate the distance your car can still run with remaining gas

#ANSWER
lit = float(input("How many litres of gas in your tank now: "))
kmlit = float(input("What is your car consumption - kilometer per litre: "))

km = (kmlit/1)*lit

print(km)


if km > 200:
    print("You have enough gas")
elif km < 200:
    print("You do not have enough gas, top up now!")



# Question 5
# A soccer team is looking for girls from ages 10 to 12 to play on their team. 
# Write a program to ask the user’s age and whether the user is male or female (using “m” or “f”). 
# Display a message indicating whether the person is eligible to play on the team. 
# Bonus: Make the program so that it doesn’t ask for the age unless the user is a girl.

# ANSWER
print("Are you keen to join our superb soccer team? Fill up the details below:")
age = int(input("Enter your age: "))
gender = input("Enter your gender: (m or f) ")
if (age >= 10) and (age <= 12):
    if gender == "f":
        print("You are selected!")
else:
    print("Sorry you are not selected!")


# Question 6
# Write a program that prompts the user to enter a weight in kilograms and height in metres and then displays the BMI as well as below interpreations.
# If BMI is Below 18.5, it is interpreted as Underweight. 
# If BMI is from 18.5–24.9, it is interpreted as Normal. 
# If BMI is from 25.0–29.9, it is interpreted as Overweight. 
# else If BMI is Above 30.0, it is interpreted as Obese.

#ANSWER
weight = float(input("Enter your weight (in kg): "))
height = float(input("Enter your height (in meter): "))

bmi = weight/height/height

if bmi < 18.5:
    print("Your BMI", int(bmi), "is Below 18.5, it is interpreted as Underweight. ")
elif (bmi > 18.5) and (bmi <24.9):
    print("Your BMI", int(bmi), "is from 18.5–24.9, it is interpreted as Normal.")
elif (bmi >25.0) and (bmi < 29.9):
    print("Your BMI", int(bmi), "is from 25.0–29.9, it is interpreted as Overweight. ")
elif (bmi > 30.0):
    print("Your BMI", int(bmi), "is Above 30.0, it is interpreted as Obese.")
else: 
    print("Please check your inputs")



# Question 7
# Write a program in which user enters one number and whether it is divisible by 7 (ie. remainder 0 when divide by 7) and is not a multiple of 5.

#ANSWER
number = float(input("Enter a number: "))
checknum = number%7
checknum2 = number%5
if (checknum == 0) and (checknum2 != 0):
    print(number, "is divisble by 7 and not a mulitple of 5")
elif (checknum == 0) and (checknum2 ==0):
    print(number, "is divisble by 7 and it is a mulitple of 5")
elif (checknum != 0) and (checknum2 ==0):
    print(number, "is not divisble by 7 and it is a mulitple of 5")



# #Sat_Lists.ipynb

# 1. Which of the following would be the resulting list after inserting the value 50 at index 2? 
# 0: 35 1: 15 2: 45 3: 28
# ANSWER: B

# (a)  0: 35       (b)   0: 35        (c)  0: 50
#      1: 50             1: 15             1: 35
#      2: 15             2: 50             2: 15
#      3: 45             3: 45             3: 45
#      4: 28             4: 28             4: 28

# 2. Lists and tuples must each contain at least one element. (TRUE/FALSE)
# ANSWER: TRUE

# 3. For lst = 4, 2, 9, 1, what is the result of the following operation, lst.insert(2, 3)?
#ANWER A

# (a) 4, 2, 3, 9, 1 
# (b) 4, 3 ,2, 9, 1 
# (c) 4, 2, 9, 2, 1

# Question 2
# What Will Be The Output Of The Following Code Snippet? 
#ANSWER: A

# a = 1,2,3,4,5 
# a[0:4:2]

# A. 1,3
# B. 1,3,5
# C. 2,4

# Question 3
# Write a Python program to print a tuple with string formatting.
# Sample tuple : (100, 200, 300)
# Output : This is a tuple (100, 200, 300)
x = (100,200,300)
print("This is a tuple, {}".format(str(x)))




# What would be the range of index values for a list of 10 elements?
# ANSWER (A)
# (a) 0–9 (b) 0–10 (c) 1–10




# Which of the following sequence types is a mutable type?
# ANSWER (A)
# (a) strings (b) lists (c) tuples









# #Sat_Loops.ipynb






# Question 1
# Predict the Output.
#ANSWER: Print hello 5 times

for i in [1, 2, 3, 4, 5]:
     print ("hello")



# Question 2

# Predict the Output.
# ANSWER: Print 12345
for i in [1, 2, 3, 4, 5]:
    print (i)


# Question 3
# Predict the Output.

#ANSWER:
# 1 times 8 = 8
# 2 times 8 = 16
# 3 times 8 = 24
# 4 times 8 = 32
# 5 times 8 = 40

for looper in [1, 2, 3, 4, 5]:
    print (looper, "times 8 =", looper * 8)


# Question 4
# Predict the Output.
# ANSWER: There is a count down - 5, 4, 3, 2, 1 then print string "BLAST OFF"

# import time
# for i in range (5, 0, -1):         #Counts backward. 
#                                      #Range ([start], [stop], [ step])
#                                     #start: Starting number of the sequence.
#                                     #stop: Generate numbers up to, but not including this number.
#                                     #step: Difference between each number in the sequence.
#     print (i)
#     time.sleep(1)                   #Waits one second
# print ("BLAST OFF!")



# Question 5
# Predict the Output.
# ANSWER: "Hi, Warren" print 3 times

for i in range(1, 6, 2):
    print ('Hi, Warren')


# Question 6
# Fill in the blank such that program prints "Hello! How are you" 5 times but 3rd time it prints only "Hello!"

#ANSWER: 
for i in range (6):
    if i ==3 : 
        print("Hello")
        continue 
    print ('How are you')





# Question 7
# What does the following for loop output?
# ANSWER B


# nums = [10, 30, 20, 40]
# for k in range(1, 4):    # range(1,4) refers to [1,2,3]   --> k = 1, k = 2, k = 3
#     print(nums[k])       # print nums[1], nums[2], nums[3]

#     (a) 10 (b) 30 (c) 10
#         30     20     30
#         20     40     20
#                       40 


# Question 8


# Write a python program to 1) ask the user the length of password and 2) generate a password randomly of given length.

# Step 1 import library "random"
# #import library random
# import random
# random.choice('ri39fk')
# Combine random alphabets,numbers and special characters, and store it in a variable called password.
# chars = 'abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*.'
# password = ''
# # Take input from user.
# # generate for loop

#ANSWER: 
import random
import string

if __name__ == "__main__":
    z1 = string.ascii_lowercase
    z2 = string.ascii_uppercase
    z3 = string.digits
    z4 = string.punctuation
    password = int(input("Enter password length: "))
    a = []
    a.extend(list(z1))
    a.extend(list(z2))
    a.extend(list(z3))
    a.extend(list(z4))
    print("Your password: ", end="")
    print("".join(random.sample(a, password)))



# Question 10

# What is the output of this code if input my_input = 0? What is the output if my_input=5?
#ANSWER: System will prompt 3 times to enter a no. if the input is 5 and if the input is 0, it will just print thank you

a = 1

while a <= 3:
    my_input = int (input ("enter a no: "))
    if my_input == 0:
        print ("your input is 0")
        break
    a+=1
    print ("looping")

print('thank you')



# Question 11

# Write a Python program to count the elements in a list before it first hits a tuple.
#ANSWER: 2

number = [10,20,(1,2),40]
counter = 0
for a in number:
    if isinstance(a, tuple):
        break
    counter += 1
print(counter)






# Question 12 - a revisit!

# A king played chess with his subject and his subject won. He asked the subject what he wanted in return. 
# The subject, being clever, asked for one grain of wheat on the first square, two grains of wheat on the second square, four grains of wheat on the third square, and so forth, doubling the amount on each next square.

# Calculate how much wheat the last square would be in kg. There are 64 squares in a chess board. A grain of wheat weighs approximately 1/7,000 of a kg.

# # first square = 1         --> 2**0
# # second square = 2        --> 2**1
# # third square = 2*2 = 4   --> 2**2
# # fourth square = 2*2*2 = 8 --> 2**3 .......

# total_grains=2**63
# total_weight =total_grains/7000
# print ("Total grain weight in kg: ", total_weight)

# Total grain weight in kg:  1317624576693539.5
# Now, using your knowledge in loops how do you calculate total grains?

#ANSWER: 
i = 1
while i < 64:
    a = 2**i
    print("No of square:", i, "equals", a)
    i += 1
