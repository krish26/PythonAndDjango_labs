class Forest:
    def __init__(self):
        print('This is the base class :forest ')

class Trees(Forest):
    def __init__(self):
        super().__init__()
        print('This is the derived class1 : Trees')

class Animals(Forest):
    def __init__(self):
        super().__init__()
        print('This is the derived class2 : Animals')
    
    def __str__(self):
        return 'im a animal obj of forest '

a1=Animals()
print(a1)
    