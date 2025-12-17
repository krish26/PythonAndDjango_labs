class Number:
    def __init__(self,num):
        self.num=num

    def __str__(self):
        return f'The number is {self.num}'

class square(Number):
    def __init__(self, num):
        super().__init__(num)
        self.num*=self.num    #2. 20*20=400

class addTen(square):
    def __init__(self, num):
        super().__init__(num)
        self.num+=10   #3.400+10

a1=addTen(20)  # 1. goes to square()
print(a1)  #410
print(addTen.mro())