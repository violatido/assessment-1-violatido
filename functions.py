# Note to instructors:
    # I created my own sudo code above each function declaration
    # for better personal readibility, I sectioned off each prompt with "#----------------""
        # please let me know if this is not-kosher!
    # Where applicable, I included notes in order to communicate to you any issues or confusion I had 

"""SKILLS: FUNCTIONS

Please complete the following promps.
"""

#################### PART 1 ####################

"""PROMPT 1

Write a function that returns `True` if a town name matches the name of your
hometown.

Examples: (let's say my hometown is San Francisco)
    - 'Oakland' -> False
    - 'San Francisco' -> True

Arguments:
    - The name of a town (str)

Return:
    - True or False (bool)
"""
# my sudo:
# globally define hometown as Fort Washington
# declare a function that takes in a string, which is a town
# if town equals hometown, return True
    # considering capitalization differences, apply the title() method to town for standardization
# otherwise, return False

# Write your function here
def check_hometown(town):
    hometown = "Fort Washington"
    if town.title() == hometown:
        return True
    else:
        return False
print(check_hometown("Fort Washington")) #True
print(check_hometown("Brookyln")) #False
print(check_hometown("fort washington")) #True

#-----------------------------------------------------------------------------------------------
"""PROMPT 2

Write a function that takes in a first and last name and returns a full name.

Examples:
    - 'Brighticorn', 'Hackbright' -> 'Brighticorn Hackbright'

Arguments:
    - First name (str)
    - Last name (str)

Return:
    - Full name (str)
"""
# sudo:
# declare a function that takes in two strings, a first and last name
# return the full name by concatenating the strings
# Write your function here
def full_name(first_name, last_name):
    return first_name + " " + last_name

print(full_name("Ilana", "Mercer"))

#-----------------------------------------------------------------------------------------------
"""PROMPT 3

Write a function that prints a greeting.

If the person is from your hometown, print
    Hi <full name>, we're from the same place!

Otherwise, print
    Hi <full name>, I'd like to visit <town name>!

HINT: You can reuse the functions that you wrote in PROMPT 1 and Prompt 2.

Examples: (still assume my hometown is San Francisco)
    - 'Fido', 'Bark', 'Oakland' -> Hi Fido Bark, I'd like to visit Oakland!
    - 'Mel', 'M', 'San Francisco' -> Hi Mel M, we're from the same place!

Arguments:
    - First name (str)
    - Last name (str)
    - Hometown (str)
"""
# sudo:
    # declare a function that takes in three strings, first name, last name, hometown
    # return this greeting: Hi <full name>, I'd like to visit <town name>!
    # following the function, declare a hometown variable to pass into the greeting function
        # the value of this hometown variable will be the return of the check_hometown username

# notes for instructor:
    # I had to double check the syntax for f strings very quickly. 
        # I understand them and have used them plenty, 
            # but I was accidentally placing the f within the quotes. 
        # I could have continued with concatenation, but that could have been ovnoxious 
# Write your function here
def greeting(full_name, hometown):
    return f"Hi {full_name}! I'd like to visit {hometown}!"

my_name = full_name("Ilana", "Mercer")
print(greeting(my_name, "Fort Washington"))

#-----------------------------------------------------------------------------------------------
"""PROMPT 4

Write a function that returns True if a fruit is a berry.

Valid berries are:
    - strawberry
    - raspberry
    - blackberry
    - currant

Examples:
    - currant -> True
    - durian -> False

Arguments:
    - A fruit (str)

Return:
    - True or False (bool)
"""
# sudo:
# def function that takes in a string that is a fruit
# create a collection of berries 
# if fruit is in the collection, return true
# Write your function here

berries = ["strawberry", "raspberry", "blueberry", "currant"]

def check_berry(fruit):
    if fruit in berries:
        return True
    else:
        return False

print(check_berry("currant"))
print(check_berry("kfgha"))
# #-----------------------------------------------------------------------------------------------
# """PROMPT 5

# Write a function that returns the shipping cost of an item.

# Berries cost $0 to ship. Everything else costs $5.

# Arguments:
#     - Something that needs to be shipped (str)

# Return:
#     - Shipping cost (int)
# """
# sudo:
# declare a function that takes in a string, which is the item to ship
# declare a cost variable that equals 0
# calculate how much shipping costs
    # if item doesn't equal berry
        # add $5 to cost
# return shipping cost
# # Write your function here
def shipping_cost(item):
    cost = 0 
    if item not in berries:
        cost = cost + 5
    else:
        cost = cost
    return cost

print(shipping_cost("apple"))
print(shipping_cost("currant"))

# #-----------------------------------------------------------------------------------------------
# """PROMPT 6

# Write a function that returns the total cost of something by applying
# taxes and fees of various states.

# States will be given as their two-letter abbreviations. For example,
# California's abbreviation is 'CA'.

# There are some states with special fees. All fees should be added to the new
# subtotal *after* tax:
#     - CA (California): add a 3% (0.03) tax for recycling
#     - PA (Pennsylvania): add $2.00 safety fee
#     - MA (Massachusettes):
#         - add $1.00 for items with a base price of $100.00 or less
#         - add $3.00 for items over $100.00

# Arguments:
#     - Base price (int)
#     - Two-letter state abbreviation (str)
#     - Tax percentage as a decimal (optional, float)
#         - If a tax percentage is not given, it defaults to 0.05 (or 5%)

# Return:
#     - Total price after taxes and fees (float)
# """
#sudo
# declare function that takes in base price(int), state (str), and tax percentage(float) with default of .05%
# create total price variable of 0
# if state is CA: total price = alter tax (tax + .03), then multiply base by new tax, then add base price
# else if state is PA: total = caculate tax (multiply base by default tax), add 2 for fee, then add base price
# else if state is MA:
    # if base price is <= $100: total = calculate tax (multiply base price by default tax), then add 1 for fee, 
        # then add base price
    # else: total = caulcate tax (multiply base by default tax), then add 3 for fee, then add base price
# return total 

#notes: 
    # For MA, I was not sure whether you meant to add $1 to base before or after multiplying by tax percentage
        # based off of the pompt saying fees go after, I calculated tax and then added the fee

# # Write your function here
def total_price(base_price, state, tax_rate = .05):
    total_taxes_fees = 1

    if state == "CA":
        total_taxes_fees = (tax_rate + 0.03) * base_price 
    elif state == "PA":
        total_taxes_fees = (base_price * tax_rate) + 2
    elif state == "MA":
        if base_price <= 100:
            total_taxes_fees = (base_price * tax_rate) + 1
        else:
            total_taxes_fees = (base_price * tax_rate) + 3
    else:
        total_taxes_fees = (base_price * tax_rate)

    return total_taxes_fees + base_price

print(total_price(10, "CA", ))
print(total_price(100, "PA", ))
print(total_price(200, "MA", ))
print(total_price(10, "MA", ))
print(total_price(5, "NY", .04))


# #-----------------------------------------------------------------------------------------------
# """PROMPT 7

# Write a function that takes in a list and *any* number of additional arguments.
# The function should add all those items to the end of the  list and return
# the list.

# We haven't taught you how to do this! You'll need to do some research on your
# own --- find a way to write a Python function that can take in an arbitrary
# amount of arguments.

# Arguments:
#     - A list (list)
#     - Additional args

# Return:
#     - A list with arguments added to the end (list)
# """
# sudo
# declare a function that takes in a list and indefinite amount of args (*args)
# loop through the args
    # add all additional args to the list ever iteration
# return list

# # Write your function here
def add_args(list, *args):
    for arg in args:
        list.append(arg)
    return list

print(add_args([3, 4], 5, 6))

# #-----------------------------------------------------------------------------------------------
# """PROMPT 8

# Write a function that takes in a word and returns a tuple. You'll do this in an
# interesting way though, so make sure you read these directions thoroughly.

# The tuple will contain two items:
#     - The given word
#     - The given word, multiplied 3 times

# To do this, your function will create an *inner* function. The *inner*
# function will multiply the given word by 3 and return it.

# Then, the outer function will call the *inner* function to create a tuple.

# Examples:
#     - 'hi' -> ('hi', 'hihihi')

# Arguments:
#     - A word (str)

# Return:
#     - (word, wordx3) (tuple)
# """

# sudo: 
# declare a function that takes in a string (word)
# create an empty string variable
# declare a function that takes in the word
    # multiply the word by three
    # return word
# create a tuple that contains the word, the word * 3
# return tuple

# # Write your function here
def create_tup(word):
    multiplied_word = ""

    def multiply_word(word):
        new_word = multiplied_word + (word * 3)
        return new_word
    
    updated_word = multiply_word("hi")

    word_tup = (word, updated_word)

    return word_tup

print(create_tup("hi"))
