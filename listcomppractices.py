# Find the needle in the haystack, and return the index
def find_needle(haystack):
    return f"found the needle at position {[ind for ind, x in enumerate(haystack) if x == 'needle'].pop()}"
print(find_needle(['hay', 'junk', 'hay', 'hay', 'moreJunk', 'needle', 'randomJunk']))

# Convert number to reversed array of digits
def digitize(n):
    return list(map(int, str(n)))[::-1]
print(digitize(345))
