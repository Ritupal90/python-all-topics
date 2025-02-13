# that mean father property take child class

class Father:
    money=20000000
    land=234567

class son(Father):
    name="ritu"

F=Father()
print(F.money)
s=son()
print(s.money)
print(s.name)