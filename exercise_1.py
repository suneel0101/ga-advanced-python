def get_evens(numbers):
    # initialize empty evens list
    evens = []
    # go through all of the numbers
    for i in numbers:
        # if i divided by 2 has NO remainder, it's even
        if i % 2 == 0:
            # add i to the evens list
            evens.append(i)
    # return the evens list
    return evens

# initialize list of numbers from 0....10,000
nums_up_to_10000 = xrange(10001)
# save the return of get_evens into the evens variable
evens = get_evens(nums_up_to_10000)
# print out evens
print evens