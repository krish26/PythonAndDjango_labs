from carnivour import Lion,Wolf,Eagle
from Herbivour import Elephant,Deer,Giraffe
from Visitor import Visitor

animals=[Lion('Simba',2),
         Wolf('Ghost',10),
         Eagle('Garud',1),
         Elephant('Dumbo',30),
         Deer('Bambi',6),
         Giraffe('Tally',2)
         ]

Visitor=Visitor(animals)

n = int(input('Enter number of days you want to simulate :'))

for day in range(1,n+1):
    for animal in animals:
        animal.daily_drain()

    print(f'Morning : Food Time ')
    for animal in animals:
        animal.eat()
        
    print('Afternoon : Interaction Time ')
    for i, animal in enumerate(animals):
        others = animals[:i] + animals[i+1:]
        animal.interact(others)

    print('Visitor Time ')
    Visitor.Visit(animals)

    print('Night: Sleeping time ')
    for animal in animals:
        animal.sleep()
        
    print("Zoo day simulation completed")
    print("End of day Summary : ")
    for animal in animals:
        print(animal)
     
     






'''


lion= Lion()
Wolf=Wolf()
Eagle=eagle()

elephant=Elephant()
deer= Deer()
giraffe=Giraffe()


lion.eat()
Wolf.eat()
Eagle.eat()

lion.sleep()
Wolf.sleep()
Eagle.sleep()






'''
