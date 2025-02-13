class A:
    age=20# ye constructor ke bahar hai

    def __init__(self):
        name="ritu"
        print(name)

        print(self.age)# isiliye ise constructor iska bap hai dikhane ke liye self use kiya 

    def show(self):#ye normal constructor hai
        print(self.age)#isiliye ye yaha use mhi hoga

obj=A()
obj.show()