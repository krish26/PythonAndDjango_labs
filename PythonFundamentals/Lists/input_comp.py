
list1= [int(n) for n in input('enter list of number with spaces:  ').split()]

class Tran:

    def __init__(self,data:list):
        self.data=data

    def even(self):
        return [n for n in list1 if n %2==0]
    
    
    
t=Tran(list1)
evens=t.even()
print(evens)




        

    
