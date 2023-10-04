def calculator(input_string):
    try:
        # Evaluate the input string
        result = eval(input_string)

        # Check for division by zero
        if 'ZeroDivisionError' in str(result):
            raise ZeroDivisionError

        return result

    except ZeroDivisionError:
        return "Error: Division by zero."

    except (SyntaxError, NameError):
        return "Error: Invalid input."

if __name__ == "__main__":
    # Prompt user for input
    input_string = input("Enter an arithmetic expression: ")

    # Remove leading and trailing spaces
    input_string = input_string.strip()

    # Check for empty input
    if not input_string:
        print("Error: Empty input.")
    else:
        # Calculate and display the result
        result = calculator(input_string)
        print("Result:", result)
