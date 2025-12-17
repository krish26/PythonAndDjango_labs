class Number:
    num=10
   

class changeTo20(Number):
    num=20
  

class Nochnage(Number):
    pass
  

n1=Number()
c1=changeTo20()
nc1=Nochnage()

print(f'orginal num {n1.num}')
print(f'changed num {c1.num}')
print(f'unchanged num {nc1.num}')
