from abc import ABC, abstractmethod 
import random

class Animal(ABC):
    GROUP='none'

    def __init__(self,name,age,energy=60):
        self.name=name
        self.age=age
        self.energy=energy

    def __str__(self):
        return (
        f"{self.__class__.__name__:<10} | "
        f"Name: {self.name:<10} | "
        f"Age: {self.age:<2} | "
        f"Energy: {self.energy}"
    )


    #energy handling methods
    def change_energy(self, amount):
        self.energy += amount
        self.energy = max(0, min(self.energy, 100))

    def daily_drain(self):
        self.change_energy(-15)
      
    #abstract methods 

    @abstractmethod  
    def eat(self):
        pass

    @abstractmethod
    def sleep(self):
        pass

    #interaction methods 
    # 30% chance animal does NOT interact

    def interact(self, others):  

        if self.energy < 10:  #too tired to interact
            print(f"{self.name} is too exhausted to interact.")
            self.change_energy(-3)
            return
        
        if random.random() < 0.3:
            if Animal.GROUP == "carnivore":
                print(f"{self.name} growls and refuses to interact.")
                self.energy -= 10
            elif Animal.GROUP == "herbivore":
                print(f"{self.name} is shy and avoids interaction.")
                self.energy -= 25
            return

        same_group = [a for a in others if a.GROUP == self.GROUP]

        if same_group:
            partner = random.choice(same_group)
            print(f"{self.name} interacts with {partner.name} ({self.GROUP})")
            self.energy += 20
        else:
            print(f"{self.name} finds no one to interact with.")
            self.energy -= 20

        # Exhaustion check
        if self.energy <= 20:
            print(f"{self.name} is exhausted!")

    









