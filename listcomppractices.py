def find_needle(haystack):
    return f"found the needle at position {[ind for ind, x in enumerate(haystack) if x == 'needle'].pop()}"
print(find_needle(['hay', 'junk', 'hay', 'hay', 'moreJunk', 'needle', 'randomJunk']))