"""Given list of ints, return list of *indices* of even numbers in list.

For example::

    >>> show_evens([])
    []

    >>> show_evens([2])
    [0]

    >>> show_evens([1, 2, 3, 4])
    [1, 3]

"""


def show_evens(nums):
    """Given list of ints, return list of *indices* of even numbers in list."""

    #initialize empty list of indices
    #iterate through num list keeping track of indices
        #check if num is even
        #if it is, add index of num to indices_list
    #return list of indices

    list_of_indices = []

    for i, num in enumerate(nums):
        if num % 2 == 0:
            list_of_indices.append(i)

    return list_of_indices

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. EVENLY HANDLED!\n")
