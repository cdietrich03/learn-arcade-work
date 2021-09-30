# def average_three(x, y, z):
#     my_result = (x + y + z) / 3
#     return my_result
#
# # my_result = average_three(10, 20, 30)
# # print(my_result)
#
# n1 = 10
# n2 = 20
# n3 = 30
# my_result = average_three(n1, n2, n3)
# print(my_result)
#
# # "If" statement
# # "Conditional logic"
#
# a = 4
# b = 5
# c = 3
# if a < b:
#     print("a is less than b")
#
# if a > b:
#     print("a is greater than b")
#
# print("Done")
#
# if a <= b:
#     print("a is less than or equal to b")
#
# if a >= b:
#     print("a is greater than or equal to b")
#
# # Equal
# if a == b:
#     print("a is equal to b")
#
# # not equal
# if a != b:
#     print("a and b are not equal")
#
# # And
# if a < b and a < c:
#     print("a is less than b and c")
#
# # Non-exclusive or
# if a < b or a < c:
#     print("a is less than either b or c (or both)")

# Boolean data type. This is legal!
# a = True
# if a:
#     print("a is true")
#
# if not a:
#     print ("a is false")
#
# a = True
# b = False
#
# if a and b:
#     print("a and b are both true")
#
# a = 3
# b = 3
#
# # This next line is strange-looking, but legal.
# # c will be true or false, depending if
# # a and b are equal.
# c = a == b
#
# # Prints value of c, in this case True
# print(c)

# if 1:
#     print("1")
# if "A":
#     print("A")
#
# # 0 is always false and "" evaluates to false

# temperature = input("What is the temperature in Fahrenheit? ")
# print("You said the temperature was " + temperature + ".")

# temperature = input("What is the temperature in Fahrenheit? ")
# temperature = int(temperature)
# if temperature > 90:
#     print("It is hot outside.")

# # Get input from the user, easier to write than the code above
# temperature = int(input("What is the temperature in Fahrenheit? "))
# print(f"You said the temperature was {temperature}.")
# # Do our comparison
# if temperature > 90:
#     print("It is hot outside.")

# temperature = int(input("What is the temperature in Fahrenheit? "))
# if temperature > 90:
#     print("It is hot outside")
# print("Done")
#
# temperature = int(input("What is the temperature in Farenheit? "))
# print(f"You said the temperature was {temperature}.")
# if temperature >= 90:
#     print("It is hot outside")
# elif temperature <= 30:
#     print("It is cold outside")
# else:
#     print("It is not hot outside")

user_name = input("What is your name? ")
if user_name == "Paul":
    print("You have a nice name.")
else:
    print("Your name is ok.")