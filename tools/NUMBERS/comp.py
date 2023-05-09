def sumofdigits(n):
    # Initialize a variable to store the sum of digits
    sum = 0
    # Convert the integer to a string to iterate through its digits
    for digit in str(n):
        # Add each digit to the sum variable after converting it back to an integer
        sum += int(digit)
    # Return the final sum
    return sum


def ispal(num):
    num_str = str(num)
    return num_str == num_str[::-1]





