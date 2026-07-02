#!/usr/bin/python3
"""Module that raises a name exception with a message"""


def raise_exception_msg(message=""):
    """Raises a NameError exception with a message

    Args:
        message: the message for the exception
    """
    raise NameError(message)
