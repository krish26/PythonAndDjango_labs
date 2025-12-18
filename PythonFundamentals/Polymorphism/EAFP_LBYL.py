def Division(a,b):
        try:
                 return a//b
        except ZeroDivisionError:
                return 'Cant be divisible by 0 '  # EAFP easier to ask forgivness than permission
                
print(Division(10,2))



def Division1(c,d):
        if(c==0 or d==0):      #LBYL -look before you leap
                return 'Cant be divisible by 0 '
        else:
                return c//d
        
print(Division1(2,0))
    


