from abc import ABC, abstractmethod 
import random

class Animal(ABC):
    GROUP='none'

    def __init__(self,name,age,energy=1): #1-3 is low energy, 4-7 is medium, 8-10 is high
        self.name=name
        self.age=age
        self.energy=energy
        self.sick=False  #state flag for sickness
        self.alive=True  #state flag for alive/dead

    def __str__(self):
        return (
        f"{self.__class__.__name__:<10}"
        f"{self.name:<10}"
        f"{self.age:<10}"
        f"{self.energy:<10}"
        f"{self.energy_status()}"
    )

      
    #abstract methods 

    @abstractmethod  
    def eat(self):
        pass

    @abstractmethod
    def sleep(self):
        pass


    #interaction and behavior methods

    def interact(self, others):
        
        if self.energy < 3:
            print(f"{self.name} the {self.__class__.__name__} is too tired to interact.")
            self.change_energy(-2)
            return

        if self.sick:
           print(f"{self.name} is sick and rests instead of interacting.")
           self.change_energy(+1)
           return

        #60% chance not  to interact
        if(self.GROUP=='carnivore'):
            if random.random() < 0.6:
                print(f"{self.name} not in a mood to interact today.")
                self.change_energy(-1)
                return
        else:  #20% chance not to interact
            if random.random() < 0.2:
                print(f"{self.name} not in a mood to interact today.")
                self.change_energy(-3)
                return

            
        
        same_group=[a for a in others if a.GROUP == self.GROUP]  # filters only same group animals

        if not same_group:
            print(f"{self.name} found no one to interact with.")
            self.change_energy(-1)   
            return  
        
        partner = random.choice(same_group)
        print(f"{self.name} is interacting with {partner.name}.")
        self.change_energy(-2)


    #energy handling methods


    def change_energy(self, amount):
        self.energy += amount
        self.energy = max(0, min(self.energy, 10))  # Clamp between 0 and 10

    def daily_drain(self):
        self.change_energy(-1)  # Daily energy drain

    def energy_status(self):
        if self.energy >= 8:
            return "High"
        elif self.energy >= 4:
            return "Medium"
        else:
            return "Exhausted"
    
    def check_health(self):
      if random.random() < 0.2:
        self.sick = True
        print(f"\n {self.name} the {self.__class__.__name__} has become sick !")
      else:
        self.sick = False

    def recover(self):
      if self.sick and self.energy >= 5 and random.random() < 0.4:
         self.sick = False
         print(f"{self.name} has recovered and is healthy again")

           


