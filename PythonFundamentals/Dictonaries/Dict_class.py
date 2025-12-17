class Itself:
    def __init__(self, data:dict):
        self.__dict__=data
    def __str__(self):
        return ','.join([f'{key}={value}' for key,value in self.__dict__.items()])

data={
    'name':'koumudi',
    'age':20,
    'email':'koumudi@gmail.com'
}

person=Itself(data)
print(person)

    

        
