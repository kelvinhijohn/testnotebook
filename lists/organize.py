#lists will always be in an unpredicted order since you cant predict how your users will iput the data
#sort method

cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
print("before sorting\n\n")
cars.sort()
print(cars)
print("after sorting\n\n")

#sort is permanent but can be reversed using .sort(reverse=true)
#for temporary sorting use sorted() method function
#print list in reverse order
print("\n\nprint cars list in reverse order")
cars.reverse()
print(cars)

#finding the length of the lists
print('\n\nlists length')
length = len(cars)
print(length)
