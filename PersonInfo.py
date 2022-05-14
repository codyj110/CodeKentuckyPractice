#function input will write the string give and put the user response into variable name
name = input("enter your name: ")
#function input will write the string give and put the user response into variable age
age = input("enter your age: ")
x = KentuckyCode = input("are you enjoying the course so far? (enter yes/no) ")
if x == "yes":
    print("Awesome")
else:
    print("Sorry to hear that")
# two methods are used here print to print the string to the user and .format puts the variables name and age
# into the two brackets {}
print("{} {}".format(name, age))

#another way to do the same thing
print(name + " " + age)