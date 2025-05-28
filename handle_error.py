while True:
    try:
        # Get first number
        num1 = float(input("Enter the first number: "))
        
        # Get second number
        while True:
            num2 = float(input("Enter the second number (cannot be zero): "))
            if num2 != 0:
                break
            print("Error: Division by zero is not allowed. Please try again.")
        
        # Perform division
        result = num1 / num2
        print(f"The result of {num1} divided by {num2} is: {result}")
        break
        
    except ValueError:
        print("Error: Please enter valid numbers only.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")