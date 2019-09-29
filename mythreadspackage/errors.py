""" module defines the errors/exceptions for this package """

__version__ = '0.1 (2019-09-29)'
__author__ = 'UTOPIA SOFTWARE'

class NoNumberError(Exception):
    """ Error should be raised when no number is avaialble to return by a callable.
    """
    
    def __init__(self, *args, **kwargs):
        if len(args) == 0: # if no argument provide to constructor, provide one
            args = ("No Number Available",)
        super().__init__(*args, **kwargs)
