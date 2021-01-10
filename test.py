# def every_other_item(items):
#     """Return every other item in `items`, starting at first item.

#     For example:

#        >>> every_other_item(['a', 400, True, 'b', 0])
#        ['a', True, 0]
#     """
#     # sudo:
#         # turn tuple into a list
#         # use slice with a skip (2)
#         # return ['the wrong thing']
    
#     #notes:
#         # my first instinct was to use slice with a skip (items[::2])
#             # however, boolean types are not iterable, so I needed to convert to a string
#         # i think tried using range with a skip, but it didn't have the desired results
#             # I believe that it would only return an index, not actual items
#         # i could also check for index using %, removing every index that is odd, but that is overbearing
#         # because of these issues, I consulted my notes to double check syntax for slice     
    
#     item2 = items[2]

#     return items

# # print(every_other_item(every_other_item(['a', 400, True, 'b', 0])))

# print(every_other_item(every_other_item(["apple", "berry", "cherry"])))




def every_other_item(items):
    items_slice = items[::2]

    return items_slice

print(every_other_item(['a', 400, True, 'b', 0]))
