class Pet:
    PET_TYPES = ['dog', 'cat', 'rodent', 'bird', 'reptile', 'exotic']
    
    all = []

    def __init__(self, name, pet_type, owner=None):
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        Pet.all.append(self)
    
    @property
    def pet_type(self):
        return self._pet_type
    
    @pet_type.setter
    def pet_type(self, pet_type):
        if pet_type in self.PET_TYPES:
            self._pet_type = pet_type
        else:
            raise Exception(
                'Pet must be of an approved type.'
            )
    
    def __repr__(self):
        return f'Pet: {self.name}'

class Owner:
    def __init__(self, name):
        self.name = name
    
    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]

    def add_pet(self, pet):
        if isinstance(pet, Pet):
            pet.owner = self
        else: 
            raise Exception (
                'Pet must be of the class Pet.'
            )
    
    def get_sorted_pets(self):
        return sorted(self.pets(), key=lambda pet: pet.name)
    
    def __repr__(self):
        return f'Owner: {self.name}'

owner = Owner("Ben")
pet1 = Pet("Fido", "dog", owner)
pet2 = Pet("Clifford", "dog", owner)

owner.get_sorted_pets()