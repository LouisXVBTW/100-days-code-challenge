def age():
    age = int(input ("Gimme Ur age: "))
    while age < 0:
            age = int(input ("Gimme Ur age: "))
    return age

def calcAge(age):
    days = age * 365
    return days

print(calcAge(age()))

input("Press enter to exit ")
