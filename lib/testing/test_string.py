#!/usr/bin/env python3

from string_functions import return_string, interpolate_string  # Use interpolate_welcome if needed

def test_return_string():
    '''in string_functions, function "return_string()" returns a variable of type str.'''
    assert type(return_string()) == str

def test_interpolate_string():  # Updated the test name to match the function
    '''in string_functions, function "interpolate_string(s)" returns a string formatted with the input string.'''
    assert interpolate_string('Guido') == 'Hello, Guido!'  # Assuming you defined interpolate_string as such
