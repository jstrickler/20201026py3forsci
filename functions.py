
def get_message():
    return "Hello Python world"


def say_hello():
    message = get_message()
    print(message)

say_hello()

def pi():
    return 22/7

print((5 ** 2) * pi())

def nothing():
    return

x = nothing()
print(x)

# var = function()

#         parameter
def hello(whom):
    print(f"Hello, {whom}")

#    argument
hello("Mom")
hello("Dad")
hello("Cousin Itt")

def foo(a, b, c):
    print("foo:", a, b, c)

foo(5, 10, 10)

values = [10, 20, 30]

foo(*values)

#       req opt  positional parameters
def spam(x, *y):
    print("x is:", x)
    print("y is:", y)
    print()

spam("wombat")
spam("wombat", "a", "b", "c")
spam("wombat", 2)


def add(a, b):
    return a + b

print(add(5, 10))
print(add(9.8, 7.1))
print(add("spam", "ham"))
print(add([1, 2, 3], [4, 5, 6]))





