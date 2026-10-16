age = input("Enter age: ")
experience = int(input("Enter experience in month: "))
certificate = input("Certificate (Y/N): ")

if age > 21 and certificate == "Y" and experience >= 12:
    print("invite")
elif age > 21 and certificate == "N" and experience >= 24:
    print("invite")