bicycles = ['trek', 'cannondale', 'redline', 'specialized' ]

print(bicycles)
print(bicycles[0].title())

names = ['Frank', 'Tom', 'Dave', 'Jon']
for i in range (0, len(names)):
    print("Good morning " + names[i] + "! How are you?")


# Create a list of motorcycle brands
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

# replace the first element, honda, with ducati
motorcycles[0] = 'ducati'
print(motorcycles)

# append honda back to the end of the list
motorcycles.append('honda')
print(motorcycles)

# Insert a motorcycle bransd into the list
motorcycles.insert(0, 'harley-davidson')
print(motorcycles)

# lets remove an element from the list - try ducati
del motorcycles[1]
print(motorcycles)

# pop allows you to remove the last item from the list, but still allows you to work 
# with it.  Save it to a variable to be able to access it later.  Pop always goes 
# for the last one in the list.

poppedCycle = motorcycles.pop()
print(motorcycles)
print(poppedCycle)

# you can pop others from the list by adding their index to the parenthesis
poppedCycle2 = motorcycles.pop(0)
print(motorcycles)
print('I ride a ' + poppedCycle2.title() + '!')

# You can remove a list item by value also
motorcycles.remove('suzuki')
print(motorcycles)

