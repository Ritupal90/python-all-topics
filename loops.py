# while loop
i=1
while i<=5:
    print("#")
    i+=1

# while loop 2
i=2
while i<=10:
    print(i)
    if(i==9):
        break
    i+=1
    continue

# while loop 3
i=0
while i<=10:
    if(i==5):
        continue
    print(i)
    break
i+=1
    

#for loop
fruits=["apple","bananas","cherry"]
for X in fruits:
    print(X)

# for loop 2
for x in "banana":
    print(x)

# for loop 3
adj=["red","big","tasty"]
fruits=["apple","banana"]
for x in adj:
    for y in fruits:
        print(x,y)