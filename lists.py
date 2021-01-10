
"""SKILLS: LISTS

Complete the following functions.
"""

#notes: I am unsure what some of the indicated return values were supposed to mean
    # I detailed this in other notes

def print_indices(items):
    """Print each item in the list, followed by its index.

    Do this without using a "counting variable" --- in other words,
    DON'T do this:

        >>> count = 0
        >>> for item in list:
        ...     print(count)
        ...     count = count + 1
        ...

    The output should look like this:

        >>> print_indices(['apple', 'berry', 'cherry'])
        apple 0
        berry 1
        cherry 2
    """
    # sudo:
        # iterate through the list with a for loop and range()
        # upon each iteration, print the list item followed by index

    #notes: 
    # I did briefly look at my notes for this one
        # i originally printed in the loop: print(items, index)
        # i noticed that the output was close, but printed the whole list three times 
            # rather than one item at a time
        # From the notes, I saw that in the print statement items needed to to be items[index]
            # I understand the logic of this though!
    # I don't know what "Nothig at all" means in this context

    
    for index in range(len(items)):
        print(items[index], index)


print_indices(["apple", "berry", "cherry"])
# print_indices("Nothing at all")


#----------------------------------------------------------------------------------------------
def words_in_common(words1, words2):
    """Return words that are shared between `words1` and `words2`.

    The returned words are sorted alphabetically.

    NOTE: For this problem, feel free to use other data structures we've
    learned about in this class.

    For example:

        >>> words_in_common(
        ...     ['Python', 'Python', 'Python'],
        ...     ['Lizard', 'Turtle', 'Python']
        ... )
        ['Python']

    The returned list should not have any duplicates:

        >>> words_in_common(
        ...     ['cheese', 'cheese', 'cheese', 'cake'],
        ...     ['cheese', 'hummus', 'beets', 'cake']
        ... )
        ['cake', 'cheese']

    If there are no words in common, return an empty list:

        >>> words_in_common(
        ...     ['lamb', 'chili', 'cheese'],
        ...     ['cake', 'ice cream']
        ... )
        []
    """
    #sudo
        # create an empty list called shared_words
        # for nested loop
            # for item1 in words1
                # for items2 in word2
        # if item1 = item2: add to shared_words
        # then create a set to remove repeated words
            # set(shared_words)
        # return set turned back into a list

    #notes
        # i don't know what i'm supposed to do with ['the wrong thing']
            # it's a list, yes, but only one list item. Also, it's only one of two needed lists

    # return ['the wrong thing']

    shared_words = []

    for item1 in words1:
        for item2 in words2:
            if item1 == item2:
                shared_words.append(item1)
    
    shared_set = set(shared_words)

    return list(shared_set)

print(words_in_common(['apple', 'cherry', 'berry'], ['grape', 'cherry', 'banana', 'berry'])) #[cherry, berry]
#----------------------------------------------------------------------------------------------
def every_other_item(items):
    """Return every other item in `items`, starting at first item.

    For example:

       >>> every_other_item(['a', 400, True, 'b', 0])
       ['a', True, 0]
    """
    # sudo:
        # turn tuple into a list
        # use slice with a skip (2)

    #note: 
        # i don't know what "return the wrong the is for"

    # return ['the wrong thing']
    
       
    items_slice = items[::2]

    return items_slice

print(every_other_item(['a', 400, True, 'b', 0]))
print(every_other_item(['the wrong thing']))





#----------------------------------------------------------------------------------------------
def smallest_n_items(items, n):
    """Return the `n` smallest integers in list in descending order.

    You can assume that `n` will be less than the length of the list.

    For example:

        >>> smallest_n_items([2, 6006, 700, 42, 6, 59], 3)
        [42, 6, 2]

    If `n` is 0, return an empty list:

        >>> smallest_n_items([3, 4, 5], 0)
        []

    Duplicates are OK:

        >>> smallest_n_items([1, 1, 1, 1, 1, 1], 2)
        [1, 1]
    """
    #sudo
        # list.sort() will sort them in ascending order, 
            # then .reverse() to get descending order
        # slice with n
        # slice.reverse()

    
    items.sort()

    items_slice = items[:n]
    items_slice.reverse()

    return items_slice

print(smallest_n_items([2, 6006, 700, 42, 6, 59], 3)) # [42, 6, 2]
print(smallest_n_items([3, 4, 5, -1, 12], 0))
print(smallest_n_items([1, 1, 1, 1, 1, 1], 2))