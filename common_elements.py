"""
File: common_elements.py
------------------------
File to implement a function that is passed two lists and returns a new list
containing those elements that appear in both of the lists passed in.
"""

def findItem(list, item):
    for e in list:
        if e==item:
            return True
    return False

def common(list1, list2):
    newls =[]
    for elem1 in list1:
        for elem2 in list2:
            if elem1==elem2:
                if findItem(newls, elem2)==False:
                    newls.append(elem2)
    return newls
    """
    This function is passed two lists and returns a new list containing
    those elements that appear in both of the lists passed in.
    >>> common(['a'], ['a'])
    ['a']
    >>> common(['a', 'b', 'c'], ['x', 'a', 'z', 'c'])
    ['a', 'c']
    >>> common(['a', 'b', 'c'], ['x', 'y', 'z'])
    []
    >>> common(['a', 'a', 'b'], ['a', 'a', 'x'])
    ['a']
    """

    """
    You implement this function.  Don't forget to remove the 'pass' statement above.
    """


def main():

    # Same tests as the doctests above, but can be run from the terminal:
    # python3 common_elements.py
    print(common(['a'], ['a']))                             # should print ['a']
    print(common(['a', 'b', 'c'], ['x', 'a', 'z', 'c']))    # should print ['a', 'c']
    print(common(['a', 'b', 'c'], ['x', 'y', 'z']))         # should print []
    print(common(['a', 'a', 'b'], ['a', 'a', 'x']))         # should print ['a']


if __name__ == '__main__':
    main()
