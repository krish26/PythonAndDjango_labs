from Animal import Animal

class Visitor:
    def __init__(self, animals):
        self.animals = animals

    
    def Visit(self,animals):
        print("Welcome to the Zoo! Enjoy your visit.")
        print('1. Feed an animal')
        print('2.just walk around and see the animals')
        print('3.Exit the zoo')
        choice = input('Enter your choice (1-3): ').strip()

        if(choice == '1'):
            self.feed(animals)
        elif(choice == '2'):
            print('Enjoy watching the animals!')        
        elif(choice == '3'):
            print('Thank you for visiting the zoo! Goodbye!')

        healthy_animals = [a for a in animals if not a.sick]


  #sick_animal is ignored while visitor is feeding animals
    def feed(self,healthy_animals):
        print('Animals available to feed:')
        for animal in healthy_animals:
            print(f'- {animal.name} the {animal.__class__.__name__}')
        animal_choice= input(f'which animal do you want to feed?').strip()
        for animal in healthy_animals:
            if animal_choice.lower() == animal.name.lower():
                print(f'{animal.name} has been fed by the visitor.')
                animal.change_energy(2)
                animal.eat()
                return
        print(f'No healthy animal named {animal_choice} found in the zoo.')