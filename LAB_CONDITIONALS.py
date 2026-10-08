age = int(input("Enter your age: "))
day = input("Enter the day: ")
student = input("Are you a student? yes or no: ")

valid_days = [
    "Monday", "Tuesday", "Wednesday",
    "Thursday", "Friday", "Saturday", "Sunday"
]

if age < 0:
    print("Invalid age")

elif day not in valid_days:
    print("Invalid day")

else:
    
    if age < 5:
        price = 0
    elif age <= 12:
        price = 6
    elif age <= 59:
        price = 10
    else:
        price = 7

    
    if day == "Friday" and price > 0:
        price = price + 2

    
    if student == "yes" and price > 0:
        price = price * 0.80

    
    if price == 0:
        print("Ticket price: Free")
    else:
        print(f"Ticket price: ${price:.2f}")