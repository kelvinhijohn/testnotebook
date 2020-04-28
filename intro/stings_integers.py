#integers dont require quotes
add = 1 + 2 + 3
print(add)

#when used in the same line as strings, issues may arise
age = 23
name = "Eric"

#print(name + " is " + age + " old")
#this results into an error. age must be converted into string
print(name + " is " + str(age) + " old")
