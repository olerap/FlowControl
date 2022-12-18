name = input("What's your name? ")
age = int(input("How old are you? " ))

if 18 <= age <= 30:
    print("Congratulations {}, your age of {} is valid for this holiday!".format(name,age))
else:
    print("Sorry {}, you're not suitable for this holiday due to your age of {}".format(name,age))
