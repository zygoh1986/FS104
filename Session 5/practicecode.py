# def add(a,b):
#     if type(a) == int and type(b) == int:
#         return a + b
#     else:
#         return "The type of number provided is not integer"

# print(add(15, 15))


# def sum(numbers):
#     #numbers = listofnumbers
#     #numbers = [1,2,3,4]
#     total = 0
#     for x in numbers:
#         #x = 1
#         total += x
#         #total = total + x
#         #total = 0 +1
#         #total = 1
#     return total
    
# listofnumbers = [1,2,3,4]
# print(sum((listofnumbers)))


# class Apollo:
#     #define a constructor to initialise a property, destination
#     # setp 1 -> how do refer the object? A: self
#     # Step 2 -> how do i create a property/ attribute? A: self.<name of the property>
#     # Setp 3 -> Where do i get the value of this property from? A: from the mehod parameter/ agrument that i send to it
#     def __init__ (self, destination):
#         self.mission_destination = destination
#     #variables
#     destination = "moon"
#     #member functions / behavior
#     def printhello(self):
#         print("hello moon")
#     def get_destination(self):
#         print("my destination - ", self.mission_destination)

# apollo1 = Apollo("moon")
# #apollo1.printhello()
# apollo1.get_destination()

# apollo2 = Apollo("mars")
# #apollo2.destination = "mars"
# apollo2.get_destination()

# a = lambda x : x + 10
# print(a(5))

# def function(x):
#     return x+10

# function(5)


# mylist = range(-5, 5)
# negatives = filter(lambda x: x < 0, mylist)
# print(list(negatives))


# a = [1,2,3,4]
# b = [10,10,10,10]
# c = map(lambda x,y:x+y, a,b)
# print(list(c))
