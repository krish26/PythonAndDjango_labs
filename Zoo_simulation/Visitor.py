class Visitor:
    def feed(self, animal):
        print("Visitor feeds the animal")
        animal.eat()
    
