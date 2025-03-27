try:
    user_input = input("Enter a number: ")
    number = int(user_input)  # Convert input to integer

    if number % 2 == 0:
        print("The number", number, "is Even.")
    else:
        print("The number", number, "is Odd.")

except ValueError:
    print("Invalid input. Please enter an integer.")
