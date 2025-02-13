light=input("enter here light:")
if(light=="red"):
    print("stop")
elif(light=="yellow"):
    print("Look here")
elif(light=="green"):
    print("Go")
else:
    print("Some issue found here sorry for that")

# we are find student grade here
marks=int(input("marks:"))

if(marks>80 and marks<101):
    print('A')

elif(marks>60 and marks<80):
    print(grade='B')

elif(marks>50 and marks<60):
    print('C')

elif(marks>45 and marks<50):
    print('d')

else:
    print("Sorry to saying you are fail")