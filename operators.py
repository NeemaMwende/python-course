# print (10 ** 3)
# print((6 + 3) - (6 + 3))
# print(100 + 5 * 3)
# print(5 + 4 - 7 + 3)

#LISTS
# thislist = ["apple", "banana", "cherry", "apple", "cherry"]
# print(thislist)

# list1 = ["apple", "banana", "cherry"]
# list2 = [1, 5, 7, 9, 3]
# list3 = [True, False, False]
# list4 = ["abc", 34, True, 40, "male"]
# print(list1,list2,list3,list4)

# mylist = ["apple", "banana", "cherry", "apple", "cherry", "apple", "cherry", "hub"]
# print(type(mylist))

# thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# print(thislist[-1])
# print(mylist[1:5])

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[:4])

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[2:])

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[-4:-1])

# thislist = ["apple", "banana", "cherry"]
# if "apple" in thislist:
#   print("Yes, 'apple' is in the fruits list")

#change item value
# thislist = ["apple", "banana", "cherry"]
# thislist[1] = "blackcurrant"
# print(thislist)

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
# thislist[1:3] = ["blackcurrant", "watermelon"]
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# thislist[1:2] = ["blackcurrant", "watermelon"]
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# thislist[1:3] = ["watermelon"]
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# thislist.insert(2, "watermelon")
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# thislist.append("orange")
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# tropical = ["mango", "pineapple", "papaya"]
# thislist.extend(tropical)
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# thistuple = ("kiwi", "orange")
# thislist.extend(thistuple)
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# thislist.remove("banana")
# print(thislist)

# thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
# thislist.remove("banana")
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# thislist.pop(1)
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# del thislist[0]
# print(thislist)
# del thislist #delete the list completely
# thislist.clear() #clear the list content

# thislist = ["apple", "banana", "cherry"]
# for x in thislist:
#   print(x)

# thislist = ["apple", "banana", "cherry"]
# for i in range(len(thislist)):
#   print(thislist[i])

# thislist = ["apple", "banana", "cherry"]
# i = 0
# while i < len(thislist):
#   print(thislist[i])
#   i = i + 1

# thislist = ["apple", "banana", "cherry"]
# [print(x) for x in thislist]

# Simple Python program to add two numbers provided by the user

# Function to add two numbers
# def add_numbers(num1, num2):
#     return num1 + num2

# # Main function
# def main():
#     print("Welcome to the simple addition program!")
    
#     # Get user input for the first number
#     num1 = float(input("Please enter the first number: "))
    
#     # Get user input for the second number
#     num2 = float(input("Please enter the second number: "))
    
#     # Call the function to add the numbers
#     result = add_numbers(num1, num2)
    
#     # Print the result
#     print(f"The sum of {num1} and {num2} is: {result}")

# # Execute the main function
# if __name__ == "__main__":
#     main()

def add_details(name, age, email, phone):
    return name + age + email + phone

def main():
    print("Welcome to Angel Hotel")
    
    # Get user input for the first number
    name = input("Please enter your name: ")
    age = input("Please enter your age: ")
    email = input("Please enter your email: ")
    phone = input("Please enter your phone number: ")
    
    # Call the function to add the numbers
    result = add_details(name , age , email , phone )
    
    # Print the result
    print(f"Your details are: { result } ")

# Execute the main function
if __name__ == "__main__":
    main()