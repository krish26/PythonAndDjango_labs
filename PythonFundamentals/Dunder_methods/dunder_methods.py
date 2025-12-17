class Dunder:
    def __init__(self,a):  
        self.a=a
    
    def __eq__(self, value):  
        return self.a==value.a
    
    def __lt__(self,value):
        return self.a< value.a
    
    def __add__(self,value):
        return self.a+value.a
    
    def __len__(self):
        return len(self.a)
    
    def __contains__(self,item):
        return item in self.a
    
    def __getitem__(self,index):
        return self.a[index]
        
        
    
        
d1=Dunder(20)
d2=Dunder(10)
print(d1==d2)
print(d1<d2)
print(d1+d2)

d1=Dunder('koumudi')
print(len(d1))

n=Dunder([1,2,34])
print(2 in n)
print(n[0])

    
