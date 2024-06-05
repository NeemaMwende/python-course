# x = 10

# if x > 5:
#     print("x is greater than 5")
# else:
#     print("x is less than or equal to 5")

# y = 3;
# c = 7;
# if y > 3 and c > 5:
#     print("y > 3 and c > 5")
# elif y <= 3 or c <= 5:
#         print("y <= 3 or c <= 5")
# else:
#     print("y <= 3 or c <= 5") 

# for i in range(5):
#     print(i)

# import sys
# print(sys.version)

# print("Cheers mate!")
# x =str(5)
# y =int(5)
# z= float(5)
# print(x, y, z)
# print(type(x), type(y), type(z))

# a = 5
# A = "Angel"
# print(a, A)

# x, y, z = 5, 10, 15
# a, b, c, = "me", "you", "us"
# print(x, y, z, a, b, c)

# x = y = z = "Orange"
# print(x)
# print(y)
# print(z)

# fruits = ["apple", "banana", "cherry"]
# x, y, z = fruits
# print(x)
# print(y)
# print(z)

# x = "Python"
# y = "is"
# z = "awesome"
# print(x, y, z)

# x = "Python "
# y = "is "
# z = "awesome"
# print(x + y + z)

# x = "awesome"

# def myfunc():
#   print("Python is " + x)

# myfunc()

# y = "Hey"

# def myfunc():
#     print("Charles is" + y)
# myfunc()

# x = "awesome"

# def myfunc():
#   x = "fantastic"
#   print("Python is " + x)

# myfunc()

# print("Python is " + x)

# def myfunc():
#     global x
#     x = "fantastic"
# myfunc()
# print("Python is " + x)

# x = "awesome"
x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)
