# print("It's alright")
# print("He is called 'Johnny'")
# print('He is called "Johnny"')

# a = """Lorem ipsum dolor sit amet,
# consectetur adipiscing elit,
# sed do eiusmod tempor incididunt,
# ut labore et dolore magna aliqua."""
# print(a)

# a = "Hello, World!"
# print(a[5])

# for x in "banana":
#   print(x)

#The len() function returns the length of a string:
# a = "Hello, World!"
# print(len(a))

#To check if a certain phrase or character is present in a string, we can use the keyword in.
# txt = "The best things in life are free!"
# print("man" in txt)

# txt = "The best things in life are free!"
# if "free" in txt:
#   print("Yes, 'free' is present.")

# txt = "The best things in life are free!"
# print("expensive" not in txt)

# if "expensive" not in txt:
#   print("Yes, 'expensive' is NOT present.")

#Slicing
# Get the characters from position 2 to position 5 (not included):
# b = "Hello, World!"
# print(b[2:12])

# b = "Hello, World!"
# print(b[2:])

# b = "Hello, World!"
# print(b[-5:-2])

#The strip() method removes any whitespace from the beginning or the end:
# a = " Hello, World! "
# print(a.strip()) # returns "Hello, World!"
# print(a) # returns "Hello, World!"

# a = "Hello, World!"
# print(a.replace("H", "J"))

# #The split() method splits the string into substrings if it finds instances of the separator:

# a = "Hello, World!"
# print(a.split(",")) # returns ['Hello', ' World!']

# a = "Hello"
# b = "World"
# c = a + " " + b
# print(c)

# a = "Hello"
# b = "World"
# c = a + b
# print(c)

#f-strings
# age = 36
# txt = f"My name is John, I am {age} "
# print(txt)

#placeholders with modifiers
# price = 59
# txt = f"The price is {price:.5f} dollars"
# print(txt)

# txt = f"The price is {20 * 30} dollars"
# print(txt)

txt = "We are the so-called \"Vikings\" from the north."
print(txt)



