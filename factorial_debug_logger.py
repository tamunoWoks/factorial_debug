# Import the logging module for debugging and tracking program execution
import logging

# Configure the logging system:
logging.basicConfig(
    level=logging.DEBUG, # captures all messages (DEBUG and above)
    format='%(asctime)s -  %(levelname)s -  %(message)s' #specifies what details to show in each log message
)

# Log the start of the program
logging.debug('Start of program')

def factorial(n):
    """
    Compute factorial of a number n using iteration,
    while logging intermediate steps for debugging.
    """
    logging.debug('Start of factorial(' + str(n) + ')')
    total = 1  # Initialize the product result
    
    # Loop through numbers from 0 up to n (inclusive)
    for i in range(n + 1):
        total *= i  # Multiply total by the current i
        logging.debug('i is ' + str(i) + ', total is ' + str(total))  # Log current state
    
    logging.debug('End of factorial(' + str(n) + ')')
    return total  # Return the computed factorial

# Call factorial function and print result
print(factorial(5))
