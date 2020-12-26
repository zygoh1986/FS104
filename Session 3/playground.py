# number1 = float(input("Enter first number: "))
# number2 = float(input("Enter second number: "))
# number3 = float(input("Enter third number: "))

# allnum = [number1, number2, number3]

# print(max(allnum))


# lit = float(input("How many litres of gas in your tank now: "))
# kmlit = float(input("What is your car consumption - kilometer per litre: "))

# km = (kmlit/1)*lit

# print(km)


# if km > 200:
#     print("You have enough gas")
# elif km < 200:
#     print("You do not have enough gas, top up now!")

# x = (100,200,300)
# print("This is a tuple, {}".format(str(x)))


# import random
# import string

# if __name__ == "__main__":
#     z1 = string.ascii_lowercase
#     z2 = string.ascii_uppercase
#     z3 = string.digits
#     z4 = string.punctuation
#     password = int(input("Enter password length: "))
#     a = []
#     a.extend(list(z1))
#     a.extend(list(z2))
#     a.extend(list(z3))
#     a.extend(list(z4))
#     print("Your password: ", end="")
#     print("".join(random.sample(a, password)))

i = 1
while i < 64:
    a = 2**i
    print("No of square:", i, "equals", a)
    i += 1



