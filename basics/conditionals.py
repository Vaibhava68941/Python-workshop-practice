day_of_the_week = input("Enter the day of the week: ").lower()
print("The day of the week is:", day_of_the_week)

if day_of_the_week == "saturday" or day_of_the_week == "sunday":
    print("It's a weekend and i will learn Live Devops!")
else:
    print("It's a weekday and i will practice Devops!")
    
    
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))


choice = input("Enter the operation: (Options +, -, *, /: ) ")
if choice == "+":
    sum_of_num = num1 + num2
    print("Addition:", sum_of_num)
elif choice == "-":
    difference_of_num = num1 - num2
    print("Subtraction:", difference_of_num)
elif choice == "*":
    product_of_num = num1 * num2
    print("Multiplication:", product_of_num)
elif choice == "/":
    if num2 != 0:
        division_of_num = num1 / num2
        print("Division:", division_of_num)
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operation selected.")
    