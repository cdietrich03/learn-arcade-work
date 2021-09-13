# Expressions
x = 5
x + 1
print(x)

# Will actually add one
x = 5
x = x + 1
print(x)

# increase to 11
x = 5
x += x + 1
print(x)

# back to 6
x = 5
x += 1
print(x)

# review

# chapter 8

# defining functions


def print_hello():
    """ This is a comment that describes the functions. """
    print("Hello!")


# This calls our function twice.
print_hello()
print_hello()


def print_hello():
    """ This function prints hello. """
    print("Hello!")


def print_goodbye():
    print("Bye!")


# Here is the main code, after all the function
# definitions.
print_hello()
print_goodbye()


def print_hello():
    print("Hello!")


def print_goodbye():
    print("Bye!")


def main():
    """ This is my main program function """
    print_hello()
    print_goodbye()


# Call (run) the main function
main()

# Only run the main function if we are running this file. Don't run it
# if we are importing this file.
if __name__ == "__main__":
    main()


def print_number(my_number):
    print(my_number)


print_number(55)
print_number(25)
print_number(8)

# click next to print and the click the bug button and step into

# This is wrong


def add_numbers(a, b):
    a = 11
    b = 7
    print(a + b)

add_numbers(11, 7)

# Add two numbers and return the results


def sum_two_numbers(a, b):
    result = a + b
    return result


# This doesn't do much, because we don't capture the result
sum_two_numbers(4, 5)

# Capture the function's result into a variable
# by putting "my_result =" in front of it.
# (Use whatever variable name best describes the data,
# don't blindly use 'my_result' for everything.)
my_result = sum_two_numbers(22, 15) # <--- This line CAPTURES the return value

# Now that I captured the result, print it.
print(my_result) # <--- This is printing, NOT capturing.


def volume_cylinder(radius, height):
    pi = 3.141592653589
    volume = pi * radius ** 2 * height
    return volume


six_pack_volume = volume_cylinder(2.5, 5) * 6
print(six_pack_volume)

# This function will print the result
def sum_print(a, b):
    result = a + b
    print(result)


# This function will return the result
def sum_return(a, b):
    result = a + b
    return result


# This code prints the sum of 4+4, because the function has a print
sum_print(4, 4)

# This code prints nothing, because the function returns, and doesn't print
sum_return(4, 4)

# This code will not set x1 to the sum.
# The sum_print function does not have a return statement, so it returns
# nothing!
# x1 actually gets a value of 'None' because nothing was returned
# the none is equal to nothing aka the function does not work
x1 = sum_print(4, 4)
print("x1 =", x1)

# This will set x2 to the sum and print it properly.
x2 = sum_return(4, 4)
print("x2 =", x2)

def calculate_average(a, b):
    """ Calculate an average of two numbers """
    result = (a + b) / 2
    return result


# Pretend you have some code here
x = 45
y = 56

# Wait, how do I print the result of this?
my_average = calculate_average(x, y)
print(my_average)


