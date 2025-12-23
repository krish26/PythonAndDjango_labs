from abc import ABC, abstractmethod 
import random

class Animal(ABC):
    GROUP='none'

    def __init__(self,name,age,energy=1): #1-3 is low energy, 4-7 is medium, 8-10 is high
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
        self.energy = max(0, min(self.energy, 10))  # Clamp between 0 and 10

    def daily_drain(self):
        self.change_energy(-1)  # Daily energy drain
      
    #abstract methods 

    @abstractmethod  
    def eat(self):
        pass

    @abstractmethod
    def sleep(self):
        pass

    def interact(self, others):
        
        if self.energy < 3:
            print(f"{self.name} the {self.__class__.__name__} is too tired to interact.")
            self.change_energy(-2)
            return []

        if(random.random() < 0.3):  # 30% chance to not be in the mood
            print(f"{self.name} the {self.__class__.__name__} is not in the mood to interact.")
            self.change_energy(-3)
            if(self.GROUP == "carnivore"):
                self.change_energy(-1)
            else:
                self.change_energy(-3)
            return []
        
        interacted = random.sample(others, min(2, len(others)))
        for animal in interacted:
            print(f"{self.name} the {self.__class__.__name__} interacts with {animal.name} the {animal.__class__.__name__}")
            self.change_energy(+2)
        return interacted


