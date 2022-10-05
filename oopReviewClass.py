# your class goes here
class Pet:
    def __init__(self, typePet, weight, limbs, age, name):
        self.__typePet = typePet
        self.__weight = weight
        self.__limbs = limbs
        self.__age = age
        self.__name = name

    def get_typePet(self):
        return self.__typePet
    
    def get_weight(self):
        return self.__weight

    def get_limbs(self):
        return self.__limbs

    def get_age(self):
        return self.__age

    def get_name(self):
        return self.__name

    def move(self, num):
        self.__dist = self.__limbs * num

    def get_move(self):
        return self.__dist

# Don't need set because we aren't asking the user anything

    