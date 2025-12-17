class Info:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def show_info(self):
        print(f'name is {self.name} and age is {self.age}')
 
class Edit_info(Info):
    def __init__(self, name, age,occupation):
        self.occupation=occupation
        super().__init__(name, age)

    def show_info(self):
        super().show_info()
        print(f'occupation is {self.occupation}')

print('<-using method overriding->')
p=Edit_info('kk',20,'dev')
p.show_info()


print('<-Using __str__ overriding->')
class Info:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def __str__(self):
        return f'name is {self.name} and age is {self.age}'
 
class Edit_info(Info):
    def __init__(self, name, age,occupation):
        self.occupation=occupation
        super().__init__(name, age)

    def __str__(self):
        return f'{super().__str__()} and occupation is {self.occupation}'
      

i=Info('kk',20)
p=Edit_info('kk',20,'dev')
print(i)
print(p)





