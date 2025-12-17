d1 ={
    1:'acrylic',
    2 :'water',
    3 :'oil'
}
d2 ={
    3 :'charcol',
    4 :'markers'
}

d3=d1|d2
print(d3)  #method 1 , no change in orginal

d1.update(d2)
print(d1) #method 2 changes d1

