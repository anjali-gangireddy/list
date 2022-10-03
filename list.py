#print list
numbers = [33,44,55,66,77,88,99]
print(numbers)

#length list
number = [33,44,55,66,77,88,99]
print(len(number))

#index access
print(number[5])

#negative index access
print(number[-5])

#print empty list
num = []
print(num)

#sliceinf of a list
print(numbers[1:])#inclusive
print(numbers[1:5])
print(numbers[:5])#exclusive

#change items in a list
numbers[1]=22
print(numbers)
numbers[1:3]=[22,11,33,44,55]
print(numbers)
print(len(numbers))

#iterating through a list
print(55 in numbers)
print(5 in numbers)


#loop statement
for number in number:
    print(number)

# list methods
numbers.append(100)
print(numbers)
numbers.insert(2,25)
print(numbers)
numbers.remove(100)
print(numbers)
numbers1 = numbers.copy()
print(numbers1)


