Monday = int(input("Enter Monday: "))
Tuesday = int(input("Enter Thuesday: "))
Wednesday = int(input("Enter Wednesday: "))
Thursday = int(input("Enter Thursday: "))
Friday = int(input("Enter Friday: "))
Saturday = int(input("Enter Saturday: "))
Sunday = int(input("Enter Sunday: "))
days_above_Average =
Average = float((Monday + Tuesday + Wednesday + Thursday + Friday + Saturday + Sunday)  // 7)

if days_above_Average > Average:
    print(f"Above Average: {days_above_Average}")