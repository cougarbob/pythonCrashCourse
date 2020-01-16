places = ['paris', 'belgium', 'sri-lanka', 'london', 'switzerland']
print(places)

# print a sorted  list
print("Print the sorted list")
print(sorted(places))

# show original order
print("Original order of the list")
print(places)

# Reverse theorder of the list
places.reverse()
print("This is the reversed list")
print(places)

# Reverse again for original order
places.reverse()
print("Reversed agaion for original order")
print(places)

# Sort the list permanently in alphabetical order
places.sort()
print("Sorted to alphabetical order permanently")
print(places)

# Sort the list permanently in reverse alphabetical order
places.sort(reverse=True)
print("Sorted to reverse alphabetical order permanently")
print(places)
