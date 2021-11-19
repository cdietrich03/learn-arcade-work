

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

# lists use brackets, functions use parenthesis

# Write your function below:




# This is some code you can use to test:

# my_list = [4, 2, 56, 2, 0]
# positive_outlook_list = []
# for item in my_list:
#     if item > 0:
#         positive_outlook_list.append(item)


# print(positive_outlook_list)


# Import functions into 'my_functions' namespace

# Start - sorting wks example - selection sort
# 15 57 14 33 72 79 26 56 42 40

# 14 is smallest, swap 14 to pos 0
# 14 57 33 72 79 26 56 42 40

# 15 is next smallest, swap 15 to pos 1
# 14 15 57 33 72 79 26 56 42 40

# 26 is next smallest, swap 26 to pos 2
# 14 15 26 33 72 79 57 56 42 40

# n = 10, 10 * 5 = 50
# n = 100, 100 * 50 = 5000
# n = 1000, 1000 * 500 = 500000
# n * (n/2) = n^2 / 2


# Take the first value, loop through, find the next number thats lower and flip them,
# do the same thing with the second value and so on
def selection_sort(my_list):
    for cur_pos in range(len(my_list)):
        min_pos = cur_pos
        for scan_pos in range(cur_pos + 1, len(my_list)):
            if my_list[scan_pos] < my_list[min_pos]:
                min_pos = scan_pos

        temp = my_list[min_pos]
        my_list[min_pos] = my_list[cur_pos]
        my_list[cur_pos] = temp


my_list = [15, 57, 14, 33, 72, 79, 26, 56, 42, 40]
selection_sort(my_list)
print(my_list)
