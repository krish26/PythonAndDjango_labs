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
    print(f'\n--- Day {day} ---\n')
    for animal in animals:
        animal.daily_drain()

    for animal in animals:
        animal.recover()

    print(f'\n--- MORNING---\n')
    for animal in animals:
        animal.eat()
        
    print(f'\n--- AFTERNOON ---\n')
    for i, animal in enumerate(animals):
        others = animals[:i] + animals[i+1:]
        animal.interact(others)

    print(f'\n--- VISITOR TIME ---\n')
    Visitor.Visit()

    print(f'\n--- NIGHT ---\n')
    for animal in animals:
        animal.sleep()

    for animal in animals:
        animal.check_health()
        
    print(f"\n Zoo day simulation completed \n")
    print(f'\n--- STATUS AT END OF DAY {day} ---\n')
    print(f"{'Type':<10} {'Name':<10} {'Age':<10} {'Energy':<10} {'Status'}")
    print("-" * 60)
    for animal in animals:
        print(animal)

