# Find the needle in the haystack, and return the index
def find_needle(haystack):
    return f"found the needle at position {[ind for ind, x in enumerate(haystack) if x == 'needle'].pop()}"
print(find_needle(['hay', 'junk', 'hay', 'hay', 'moreJunk', 'needle', 'randomJunk']))

# Convert number to reversed array of digits
def digitize(n):
    return list(map(int, str(n)))[::-1]
print(digitize(345))

# Vowel remover
def shortcut(s):
    return str(''.join([l for l in s if l not in "aeiou"]))
print(shortcut("hello"))

# Function to return an array of numbers N to 0, where N is > 0
def reverse_seq(n):
    return [x for x in range(1, n)[::-1]]
print(reverse_seq(8))