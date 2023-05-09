'''a simple ascript to test all the functions'''
from func_enum import Operation
from NUMBERS.simp import adding, subtracting
from NUMBERS.comp import sumofdigits, ispal
from tools.col import my_zip

# Define a function to perform mathematical operations based on input operation
def perform_operation(n1, n2, operation):
    if operation == Operation.ADD:  # If operation is addition
        return adding(n1, n2)  # Call the add function from simp package
    elif operation == Operation.SUBTRACT:  # If operation is subtraction
        return subtracting(n1, n2)  # Call the subtract function from simp package
    elif operation == Operation.SUM_OF_DIGITS:  # If operation is sum of digits
        return sumofdigits(n1)  # Call the sumofdigits function from comp package
    elif operation == Operation.IS_PALINDROME:  # If operation is palindrome check
        return ispal(n1)  # Call the ispal function from comp package
    elif operation == Operation.MY_ZIP:  # If operation is zip
        return my_zip(n1, n2)  # Call the my_zip function from col package
    else:
        raise ValueError("Invalid operation")  # If an invalid operation is provided, raise an error


# Call the perform_operation function with different inputs and print the output
if __name__ == '__main__':
    print(perform_operation(2, 3, Operation.ADD)) 
    print(perform_operation(5, 1, Operation.SUBTRACT)) 
    print(perform_operation(123, None, Operation.SUM_OF_DIGITS)) 
    print(perform_operation(121, None, Operation.IS_PALINDROME)) 
    print(list(perform_operation([1, 2, 3], ['a', 'b', 'c'], Operation.MY_ZIP))) 
