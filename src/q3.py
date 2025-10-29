from typing import Any, TypeVar

"""
This question does not contain starter code.

Create a class decorator called add_counter that automatically adds methods to track how many times any method of the class has been called.

Your decorator should:

- Start the count variable at zero in the constructor
- Track calls by wrapping all methods (except those starting and ending with __) with a counting function
- Add a get_call_count() method that returns the total number of method calls
- Add a reset_counter() method that resets the count to zero
"""

T = TypeVar("T")
