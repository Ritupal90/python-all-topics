#here we are looking one parent class and multiple child class but all child class direct acces his parent clas

class sabhajit:
    money=4673465478645378
    land=4645646678
    house=10
class saniya(sabhajit):
    pass
class vikash(sabhajit):
    study='famacy'
class ritu(sabhajit):
    pass
class neha(sabhajit):
    pass

s=saniya()
print(s.money)