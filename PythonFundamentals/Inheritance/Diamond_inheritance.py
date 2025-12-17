class A:
    def __init__(self):
        print('this is class a')

class B(A):
    def __init__(self):
        super().__init__()
        print('this is class B derived from A')

class C(A):
    def __init__(self):
        super().__init__()
        print('This is class c derived from A')

class D(C,B):
    def __init__(self):
        super().__init__()  # without super() A runs twice 
        print('this is class D from B,C classes')

d1=D()
print(D.mro())
#D-C-B-A-obj

'''
D.__init__()
→ super() → next in MRO → C

C.__init__()
→ super() → next in MRO → B

B.__init__()
→ super() → next in MRO → A

A.__init__()
→ prints
→ returns back up

'''
