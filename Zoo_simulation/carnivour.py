from Animal import Animal

class Lion(Animal):   
    GROUP = "carnivore"

    def eat(self):
        print(f'{self.name} is Eating!!!')
        self.change_energy(5)
    
    def sleep(self):
        print(f'{self.name} is Sleeping....')
        if self.energy < 7:
           self.change_energy(3)
        else:
           self.change_energy(1)

class Wolf(Animal):
    GROUP = "carnivore"


    def eat(self):
        print(f'{self.name} is Eating!!!')
        self.change_energy(5)

    def sleep(self):
        print(f'{self.name} is Sleeping....')
        if self.energy < 7:
           self.change_energy(3)
        else:
           self.change_energy(1)


class Eagle(Animal):
    GROUP = "carnivore"

    def eat(self):
        print(f'{self.name} is Eating!!!')
        self.change_energy(5)
    
    def sleep(self):
        print(f'{self.name} is Sleeping....')
        if self.energy < 7:
           self.change_energy(3)
        else:
           self.change_energy(1)

    