from Animal import Animal

class Lion(Animal):   
    GROUP = "carnivore"

    def eat(self):
        print(f'{self.name} is Eating!!!')
        self.change_energy(25)
    
    def sleep(self):
        print(f'{self.name} is Sleeping....')
        if self.energy < 30:
           self.change_energy(15)
        else:
           self.change_energy(8)

class Wolf(Animal):
    GROUP = "carnivore"


    def eat(self):
        print(f'{self.name} is Eating!!!')
        self.change_energy(25)

    def sleep(self):
        print(f'{self.name} is Sleeping....')
        if self.energy < 30:
           self.change_energy(15)
        else:
           self.change_energy(8)

class Eagle(Animal):
    GROUP = "carnivore"

    def eat(self):
        print(f'{self.name} is Eating!!!')
        self.change_energy(25)
    
    def sleep(self):
        print(f'{self.name} is Sleeping....')
        if self.energy < 30:
           self.change_energy(15)
        else:
           self.change_energy(8)


    