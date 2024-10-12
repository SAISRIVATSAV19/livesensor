import os
import sys


def error_message_detail(error, error_detail: sys):
    # Get exception details from sys
    _, _, exc_tb = error_detail.exc_info()
    
    # Get the filename and line number from traceback object
    filename = exc_tb.tb_frame.f_code.co_filename
    error_message = (
        "Error occurred in the file [{0}] at line number [{1}] with error: [{2}]"
        .format(filename, exc_tb.tb_lineno, str(error))
    )
    
    return error_message


class SensorException(Exception):  # Inheriting from Exception
    
    def __init__(self, error, error_detail: sys):
        super().__init__(str(error))  # Initialize the base class with the error message
        
        # Set the detailed error message
        self.error_message = error_message_detail(error, error_detail)
    
    def __str__(self):
        return self.error_message
