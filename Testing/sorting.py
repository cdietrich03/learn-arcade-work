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


# Insert sort
# 15 57 14 33 72 79 26 56 42 40
# 14 15 57 33 72 79 26 56 42 40
# 14 15 33 57 72 79 26 56 42 40
# 14 15 33 57 72 79 26 56 42 40
# 14 15 33 57 72 79 26 56 42 40
# 14 15 26 33 57 72 79 56 42 40
# 14 15 26 33 56 57 72 79 42 40
# 14 15 26 33 42 56 57 72 79 40
# 14 15 26 33 40 42 56 57 72 79

# right to left
def insertion_sort(my_list):
    for key_pos in range(1, len(my_list)): # 100
        key_value = my_list[key_pos]
        scan_pos = key_pos - 1
        while(scan_pos >= 0) and (my_list[scan_pos] > key_value): # worst case - 50, average - 25
            my_list[scan_pos + 1] = my_list[scan_pos]
            scan_pos -= 1

        my_list[scan_pos + 1] = key_value





my_list = [15, 57, 14, 33, 72, 79, 26, 56, 42, 40]
insertion_sort(my_list)
print(my_list)

# Selection sort, all cases
# n = 10, 10 * 5 = 50
# n = 100, 100 * 50 = 5000
# n = 1000, 1000 * 500 = 500000
# n * (n/2) = n^2 / 2

# Insertion sort, worst case
# n = 10, 10 * 5 = 50
# n = 100, 100 * 50 = 5000
# n = 1000, 1000 * 500 = 500000
# n * (n/2) = n^2 / 2

# Insertion sort, average case
# n = 10, 10 * 2.5 = 25
# n = 100, 100 * 14 = 2500
# n = 1000, 1000 * 250 = 250000
# n * (n/4) = n^2 / 4

# Insertion sort, best case
# n = 10, 10 * 1 = 10
# n = 100, 100 * 1 = 100
# n = 1000, 1000 * 1 = 1000
# n

