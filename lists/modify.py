#items in a list can be removed, modified, changed or added

motorcycles = ['honda','yamaha', 'suzuki', 'kawasaki']
print(motorcycles)


#change
print("\n\nWe are changing the first index value")
motorcycles[0] = 'ducati'
print(motorcycles)

#adding elements in the list
print("\n\n Adding new elemts in the list")
motorcycles.append('honda')
print(motorcycles)

#inserting an element in a specific index
print("\n\nWe are adding an element at index [2]")
motorcycles.insert(2, 'husquvana')
print(motorcycles)

#removing elements from the list
print("\n\nRemoving elements from the list")
del motorcycles[3]
print(motorcycles)

#elements can also be removed by popping them out a list
print("\n\n")
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle + " got popped out of the list")

#above pops the last element in the list
#items cam be popped from any position motorcycles.pop(0)

#items can also be removed by name
print("\n\n Removing itmes by name")
motorcycles.remove('husquvana')
print(motorcycles)
