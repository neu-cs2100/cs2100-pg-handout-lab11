from typing import Any, TypeVar

"""
There is no starter code for this problem.

Create a class decorator called add_display_methods that automatically adds two useful methods to any class:

print(): Prints what is returned by __str__()
describe(): Prints all the object's attributes and their values

The decorator should work on any class.

Hint: You can use the built-in vars() function to get the attributes of an object as a dictionary.
Hint: You can use setattr(cls, "method_name", method) to add methods to a class dynamically.
Hint: The print method should not override the built-in print function, so make sure to define it in a way that avoids name conflicts.
"""

T = TypeVar("T")
