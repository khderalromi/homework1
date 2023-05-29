user_number = input("Enter a binary number: ")
d = 0
for i in user_number:
    if i not in ['0', '1']:
        print("Invalid input enter binary numbers")
        break
    d = int(user_number, 2)
else:
    print("The decimal equivalent of", user_number, "is", d)
