# Import the logging module for debugging and tracking program execution
import logging

# Configure the logging system:
logging.basicConfig(
    level=logging.DEBUG, # captures all messages (DEBUG and above)
    format='%(asctime)s -  %(levelname)s -  %(message)s' #specifies what details to show in each log message
)

# Log the start of the program
logging.debug('Start of program')
