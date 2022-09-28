__all__ = (
    'CatainError'
)

class CatainException(Exception):
    """
    Base exception class for catain.py
    """
    pass

class BuildException(CatainException):
    """
    Base exception for building-related errors
    """
    pass

class CostException(CatainException):
    pass