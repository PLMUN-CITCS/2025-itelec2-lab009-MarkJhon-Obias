def main():
    """Main function to check if the number is even or odd."""
    
    try:
        user_input = input("Enter a number: ")
        number = int(user_input)

        # Check if the number is even or odd
        if number % 2 == 0:
            print("The number", number, "is Even.")
        else:
            print("The number", number, "is Odd.")
             
    except ValueError:
        print("Invalid input. Please enter an integer.")
    
if __name__ == "__main__":
    main()
