def is_palindrome(num):
    # Check if the number is a two-digit number
    if num < 10 or num > 99:
        raise ValueError("Please enter a two-digit number.")
    
    # Convert the number to string to check for palindrome
    str_num = str(num)
    return str_num == str_num[::-1]

# Example usage
if __name__ == "__main__":
    try:
        number = int(input("Enter a two-digit number: "))
        if is_palindrome(number):
            print(f"{number} is a palindrome.")
        else:
            print(f"{number} is not a palindrome.")
    except ValueError as e:
        print(e)
