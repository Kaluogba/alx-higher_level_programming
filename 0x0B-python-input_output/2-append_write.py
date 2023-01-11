#!/usr/bin/python3
"""A Module that contains a function that appends a string at the end of
   a text file (UTF8) and returns the number of characters added
"""


def append_write(filename="", text=""):
    """Function that appends to a text file

    Args:
        filename: name of file to be appended
        text:string or text to be appended
    """
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
