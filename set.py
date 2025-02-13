 #set is the collection of the unordered items.
 #each element in the set ust be unique & mutable
 #repeated elementstored only once so it is count only one time
num1={1,2,3,4,5}
num2={2,2,4,5,7,8}

num1.add(10)
print(num1)

print(num1.union(num2))
print(num1.intersection(num2))

num1.pop()
print(num1)

num1.remove(10)
print(num1)

num1.clear()
print(num1)

