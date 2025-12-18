def Name(name):
    return name.upper()
     


class Buff:
    def __init__(self,name):
        self.name=name
    def upper(self):
        return self.name.upper() +'!!!'
    

print(Name('koumudi'))   #attribute error
print(Name(Buff('koumudi')))

#print(Name(10))  #error

