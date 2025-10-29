from typing import Any, Callable

"""
This question does not contain starter code.

Create a function decorator called cache which stores what the function returns in a dictionary.

The decorator should:
1. Add a cache as an attribute to the function, if it doesn't already have that attribute
2. The keys in the cache should be a tuple of the arguments passed to the function
3. The values in the cache should be the result returned by the function
4. The decorator should check if the cache already contains the result for this particular
   tuple of arguments. If so, return it. If not, calculate it, store it in the cache, and
   then return it.
"""
