cars = ['bmw', 'audi', 'toyata', 'subaru']
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)

cars2 = ['bmw', 'audi', 'toyata', 'subaru']
print('Here is the sorted list')
print(sorted(cars2))
print('here is the original list')
print(cars2)

# Reverse will sort the list in the reverse order that it is in the array 
# (not alphabetical order)

print(cars2)

cars2.reverse()
print(cars2)

# the reverse method reverses the list permanently, but you can reverse it back.

cars2.reverse()
print(cars2)

