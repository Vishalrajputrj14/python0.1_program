class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def show_deteils(self):
        print(f"Name: {self.name}")
        print(f"Species: {self.species}")

class Dog(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self, name, species="Dog")
        self.breed = breed

        def show_deteils(self):
            Animal.show_deteils(self)
            print(f"Breed: {self.breed}")
# Object of Dog

class GoldenRetriever(Dog):
    def __init__(self, name, color):
        Dog.__init__(self, name, breed="Golden Retriever")
        self.color = color

    def show_deteils(self):
        Dog.show_deteils(self)
        print(f"Color: {self.color}")

dog = GoldenRetriever("Buddy", "Golden")
dog.show_deteils()


        
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def show_deteils(self):
        print(f"Name: {self.name}")
        print(f"Species: {self.species}")


class Animal: 
    def __init__(self,name ,species):
        self.name = name
        self.species = species
