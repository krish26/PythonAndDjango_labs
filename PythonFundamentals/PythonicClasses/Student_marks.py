class Student_marks:

    def __init__(self,**kwargs):
        self.marks=kwargs
    
    @property
    def update_values(self):
        return self.marks
    
    @update_values.setter
    def update_values(self,values):
        self.marks=values
    
    def __str__(self):
        return (','.join(f'{key}:{value}' for key,value in self.marks.items()))
    
    def high_division(self):
        return(','.join(f'{key}:{value}' for key,value in self.marks.items() if value>75))

d1={
    'st1':100,
    'st2':66,
    'st3':80,
    'st4':77,
    'st6':68
}

s1=Student_marks(**d1)
print(s1)
print(s1.high_division())





