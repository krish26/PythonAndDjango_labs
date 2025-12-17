class salary:
    def __init__(self,base_value):
        self.base_value=base_value
        print(f'The base salary is : {self.base_value}')
    
class AddBonus(salary):
    bon=400
    def __init__(self, base_value):
        super().__init__(base_value)
        self.base_value +=self.bon
        print(f'The Added bonus is : {self.bon}')

class Apply_tax(salary):
    tax=100
    def __init__(self, base_value):
        super().__init__(base_value)
        self.base_value-=self.tax
        print(f'The tax deducted is : {self.tax}')

class Final_amount(AddBonus,Apply_tax):
    def __init__(self, base_value):
        super().__init__(base_value)
        print(f'The final salary is : {self.base_value}')

    def __str__(self):
        return f'Final salary: {self.base_value}'

s1=Final_amount(400)
print(s1)
print(Final_amount.mro())

        
