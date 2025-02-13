#in this we have one parent class and multiple child classes he acces one to another

class Class:
    teachers=input('teachers:=')

class div1(Class):
    Cltname1="shivam"

class div2(div1):
    Cltname2="saniya"

class div3(div2):
    Cltname3="pagal"

d=div2()
print(d.teachers)         