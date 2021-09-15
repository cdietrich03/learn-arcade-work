# Define a simple function that prints x
def f(x):
    x += 1
    print(x)


# Set x
x = 10
# Call the function
f(x)
# Print x to see if it changed
print(x)

# Example 4
def a():
    print("A start")
    b()
    print("A end")


def b():
    print("B start")
    c()
    print("B end")


def c():
    print("C start and end")

a()

# Example 5
def a(x):
    print("A start, x =", x)
    b(x + 1)
    print("A end, x =", x)


def b(x):
    print("B start, x =", x)
    c(x + 1)
    print("B end, x =", x)


def c(x):
    print("C start and end, x =", x)


a(5)


# Example 9
def a(x, y):
    x = x + 1
    y = y + 1
    print(x, y)


x = 10
y = 20
a(y, x)

# return ends a function