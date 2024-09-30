def time_remaining(age):
    years = 90 - age
    months = years * 12
    weeks = years * 52
    days = years * 365
    print(" ")
    print("********************************************************************")
    print(f"You only have {days} days, {weeks} weeks, and {months} months left!")
    print("********************************************************************")
    print(" ")

print("-----------------------------------")
print(" HOW MUCH TIME DO YOU HAVE LEFT? ")
print("-----------------------------------")

age = int(input("Enter your age: "))

if age < 1:
    age = int(input("Please enter a valid age: "))
elif age > 90:
    print(" ")
    print("***************************************************************************")
    print(f"Wow! You're {age} years old??? You are already on borrowed time my friend.")
    print("***************************************************************************")
    print(" ")
else:
    time_remaining(age)
