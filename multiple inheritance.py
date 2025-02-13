 #in this we are look multiple parents and one child class who access both parent 
class father:
    money=4000000
    sirname='pal'

class mother:
    eyecolor='black'
    behaviour='good'
    working='properly,hard'

class child(father,mother):
    study='MCA'
    job='software'

c=child()
print(c.behaviour)
print(c.sirname)
