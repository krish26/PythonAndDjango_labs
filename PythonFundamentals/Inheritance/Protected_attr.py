class Details:
    _Userid=101   #protected attribute

class editDetails(Details):
    #_Userid=102    #overrides protected attr
    def change_id(self,new_id): # can write a method and edit the new id insted to avoid data mishandlin
        self._Userid=new_id

d1=Details()
d2=editDetails()

d2.change_id(102)

print(f'user id from parent {d1._Userid}')
print(f'userid from child class {d2._Userid}')

print(d1._Userid)  #orginal id is the same 

