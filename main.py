from sensor.exception import SensorException
import sys
import os
from sensor.logger import logging

def test_exception():
    try:
        logging.info("divison error")
        a = 1 / 0  # This will raise a ZeroDivisionError
    except Exception as e:
        raise SensorException(e, sys)  # Raise custom SensorException


if __name__ == "__main__":  # Run when the script is executed
    try:
        test_exception()  # Call the function to trigger the exception
    except SensorException as se:  # Catch and handle the custom exception
        print(se)  # Print the detailed error message from SensorException
