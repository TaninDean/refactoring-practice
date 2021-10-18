"""
This code creates a datetime.time object from a string.

- Is it easy to verify that it works correctly?
- Do you see any obvious errors?
- How would you modify it to be easier to read?
"""

import datetime


def create_time_from_time_stamp(timestamp: str) -> datetime.time:
    """Create a datetime.time object from a string in the form 'hh:mm:ss'.

    Args:
    timestamp - string containing a timestamp in the format 'hh:mm:ss'

    Returns:
    a datetime.time object with value equal to the timestamp

    Raises:
    ValueError if timestamp is not a string in form "hh:mm:ss"

    Example:
    >>> t = create_time_from_time_stamp("9:23:15")
    >>> type(t)
    <class 'datetime.time'>
    >>> print(t)
    09:23:15
    """
    args = timestamp.split(":")
    if len(args) != 3:
        raise ValueError('Timestamp must be "hh:mm:ss"')
    (hour, minute, second) = args
    # if the timestamp is not valid, this may raise TypeError or ValueError
    if is_valid_time(int(hour), int(minute), int(second)):
        return datetime.time(int(hour), int(minute), int(second))


def is_valid_time(hour, minute, second):
    """Verify hour, minute and second is valid.

        Return:
            bollean

        Raise:
            ValueError if hour, minute and second is can't cast to integer
    """
    return 0 <= int(hour) <= 23 and 0 <= int(minute) < 60 and 0 <= int(second) < 60
