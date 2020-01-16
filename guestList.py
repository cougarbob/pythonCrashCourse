guestList = ['Jimi Hendrix', 'Janis Joplin', 'Jim Morrison']
print(guestList)
for i in range (0, len(guestList)):
    print("Please come to dinner, " + guestList[i])

# Jim Morrison is indisposed and will not be there, 
# but Ozzy should be able to come.
cantMakeIt = guestList.pop(2)
print (cantMakeIt + " can't make it")
guestList.append ('Ozzy Osbourne')

for i in range (0, len(guestList)):
    print("Please come to dinner, " + guestList[i])

# invite 2 more people to dinner - table got bigger

guestList.append('Leon Russell')
guestList.append('Miles Davis')

print('The table got a little bigger')
for i in range (0, len(guestList)):
    print("Please come to dinner, " + guestList[i])

for i in range (0, len(guestList)-2):
    poppedGuest = guestList.pop(i)
    print ("sorry, " + poppedGuest + ".  No room at the table for you.")

for i in range (0, len(guestList)):
    print("Welcome, " + guestList[i] + "! You are still invited.")

# for i in range (0, len(guestList)):
#     del guestList[i]

del guestList[1]
del guestList[0]

print(guestList)
print('I am all alone for Christmas!')