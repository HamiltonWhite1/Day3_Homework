# Exercise #1
# Filter out all of the empty strings
places = [' ', 'Argentina', '  ', 'San Diego', '', '   ', '', 'Boston', 'New York']
list_filter = lambda nice_place: nice_place.isspace() == False and nice_place != ''
cleaned_list = list(filter(list_filter, places))
print(cleaned_list)

# Exercise #2
# make list sorted by last name
authors = ["Connor Milliken", "Victor aNisimov", "Andrew P. Garfield", "David HassELHOFF", "Oprah wInfrey"]
sorted_by_last = sorted([' '.join(name.split()[::-1]) for name in authors], key=str.lower)
print(sorted_by_last)

# Exercise #3
# Convert list from Celsius to Farenheit
places_temps = [('Nassau', 32), ('Boston', 12), ('Los Angeles', 44), ('Miami', 29)]
anon_func = lambda place: (place[0], (place[1] * 1.8) + 32)
fahren = list(map(anon_func, places_temps))
print(fahren)

# Exercise #4
# Worked on a more direction-specific solution with Justin 
# Write recursive function that returns fibonacci sequence up to the number passed in
fib_set = set()
def recursive_fib(n):
    if n <= 0:
        print("Sorry, the Fibonacci sequence starts at 1.")
    elif n == 1 or n == 2:
        fib_set.add(1)
        return 1
    else:
        new_fib_num = recursive_fib(n-1) + recursive_fib(n-2)
        fib_set.add(new_fib_num)
        return new_fib_num
recursive_fib(9)
fib_list = sorted(list(fib_set))
fib_list.insert(0, 1)
print(fib_list)

# First draft Fib recursive function that returns only the last value in the Fibonacci sequence. Works, but not following the instructions totally
def recursive_fib(n):
    if n <= 0:
        print("Sorry, the Fibonacci sequence starts at 1.")
    elif n == 1 or n == 2:
        return 1
    else:
        return recursive_fib(n-1) + recursive_fib(n-2)
print(recursive_fib(9))



