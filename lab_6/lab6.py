# Create set to store basketball team with 5 people
basketball_team = {'one', 'two', 'three', 'four', 'five'}

# Create set to store baseball team with 9 people
baseball_team = {'one', 'two', 'three','four','five','six','seven','eight'}

# Create set to store soccer team with 11 people with some overlapping with basketball and baseball team
soccer_team = {'one', 'three', 'five', 'fix', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen'}

# Write all files to the data directory, e.g. data/basketball_set.txt
basketball_file = 'data/basketball_set.txt'
baseball_file = 'data/baseball_set.txt'
soccer_file = 'data/soccer_set.txt'

# Use with statement to write basketball_set.txt, baseball_set.txt, and soccer_set.txt
try:
    with open(basketball_file, 'w+') as f:
        f.write('\n'.join(basketball_team))
except:
    print(' basketball error')

try:
    with open(baseball_file, 'w+') as f:
        f.write('\n'.join(baseball_team))
except:
    print('baseball error')

try:
    with open(soccer_file, 'w+') as f:
        f.write('\n'.join(soccer_team))
except: 
    print('soccer error')

# Define file paths for intersection, union, and difference files
intersection_basketball_soccer_file = 'data/intersection_basketball_soccer.txt'
union_basketball_baseball_file = 'data/union_basketball_baseball.txt'
difference_basketball_soccer_file = 'data/difference_basketball_soccer.txt'
difference_baseball_basketball_file = 'data/difference_baseball_basketball.txt'

# Use with statement and set intersection to write intersection_basketball_soccer.txt
try: 
    with open(intersection_basketball_soccer_file, 'w') as f:
        intersection = basketball_team.intersection(soccer_team)
        f.write('\n'.join(intersection))
except:
    print('basketball soccer intersection error')

# Use with statement and set union to write union_basketball_baseball.txt
try:
    with open(union_basketball_baseball_file, 'w') as f:
        union = basketball_team.union(baseball_team)
        f.write('\n'.join(union))
except:
    print('basketball baseball union error')

# Use with statement and set difference to write difference_basketball_soccer.txt
try: 
    with open(difference_basketball_soccer_file, 'w') as f:
        difference = basketball_team.difference(soccer_team)
        f.write('\n'.join(difference))
except: 
    print('basketball soccer difference union')

with open(difference_baseball_basketball_file, 'w') as f:
    difference = baseball_team.difference(basketball_team)
    f.write('\n'.join(difference))
# Create 3 level nested tuple e.g. (1, 2, (3, 4, (6, 7)))
nested_tuple = (1, 2, (3, 4, (6, 7)))

# Use with statement to write nested tuple to file
nested_tuple_file = 'data/nested_tuple.txt'
with open(nested_tuple_file, 'w') as f:
    f.write(str(nested_tuple))
# Use loop to create flattened tuple and write to file using with
# Ensure files are closed and exceptions caught
# Flatten the nested tuple
def flatten_tuple(nested_tuple):
    flattened = []
    for item in nested_tuple:
        if isinstance(item, tuple):
            flattened.extend(flatten_tuple(item))
        else:
            flattened.append(item)
    return tuple(flattened)

flattened_tuple = flatten_tuple(nested_tuple)

# Write the flattened tuple to a file
flattened_tuple_file = 'data/flattened_tuple.txt'
with open(flattened_tuple_file, 'w') as f:
    f.write(str(flattened_tuple))
# Ask user for range for numbers
start = int(input("Enter start number: "))
end = int(input("Enter end number: "))

# Use list comprehension to generate even numbers in range and write to file
even_numbers = [x for x in range(start, end + 1) if x % 2 == 0]
even_numbers_file = 'data/even_numbers.txt'
with open(even_numbers_file, 'w') as f:
    f.write('\n'.join(map(str, even_numbers)))

# Ask user for range for numbers
start = int(input("Enter start number: "))
end = int(input("Enter end number: "))

# Use list comprehension to square numbers in range and write to file
squared_numbers = [x**2 for x in range(start, end + 1)]

squared_numbers_file = 'data/squared_numbers.txt'
with open(squared_numbers_file, 'w') as f:
    f.write('\n'.join(map(str, squared_numbers)))