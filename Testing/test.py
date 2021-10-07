

# print("Most exciting class ever!!!")
# print("I want to sleep \\\\hi\\\\")
# print("What does\ndo? It\nis weird.")
# print("""Wow
# the professor
# has
# gone
# crazy""")


# ch 11
# 'for loops' - when you know how many times to loop
# 'while loop' - loop until a condition

# i represent increment, can be replaced with any variable


# sentinel variable, teh variable watched until exiting a function
# Running total
# Boolean variables are true and false


# Write your function below:
def zap_list(list):
    for index in range(len(my_list)):
        my_list[index] = 0


# This is some code you can use to test:

# Example 1, should print [0, 0, 0, 0]
my_list = [6, 1, -1, 10]
zap_list(my_list)
print("Example 1:", my_list)