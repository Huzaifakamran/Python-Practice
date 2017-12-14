##PRACTICE##
## Ch#4 ##
##for loop##
for value in range(1,6):
    print(value)

##Using range() to Make a List of Numbers ##
numbers=list(range(1,6))
print(numbers)

##Using range() to print even numbers##
even_numbers=list(range(0,11,2))
print(even_numbers)
##Using range() to print odd numbers##
odd_numbers=list(range(1,11,2))
print(odd_numbers)
##square##
squares=[]
for value in range(1,11):
    square=value**2
    squares.append(square)
print(squares)
##OR##
sqrs=[value**2 for value in range(1,11)]
print(sqrs)
##SLICING##
list=['hk','kammo','habibi','majid','rajjo']
print("The First Three player of My Team is ")
print(list[0:3])
## Copying a List ##
My_List=[1,2,3,4,5,6,7,8]
your_list=My_List[:]
print(your_list)
