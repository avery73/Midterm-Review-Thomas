import oopReviewClass as o

def main():

    # type, weight, limbs, age, name
    dog = o.Pet("Dog", 100, 4, 3, "Spots")
    cat = o.Pet("Cat", 30, 4, 12, "Kitty")
    turtle = o.Pet("Turtle", 5, 4, 8, "Ralph")

    pets = {}

    pets[dog.get_name()] = [dog.get_typePet(),dog.get_weight(),dog.get_limbs(),dog.get_age()]
    pets[cat.get_name()] = [cat.get_typePet(),cat.get_weight(),cat.get_limbs(),cat.get_age()]
    pets[turtle.get_name()] = [turtle.get_typePet(),turtle.get_weight(),turtle.get_limbs(),turtle.get_age()]

    #print(pets)

    dog.move(10) # 10 = num variable
    print(dog.get_move())
    cat.move(3)
    print(cat.get_move())
    turtle.move(8)
    print(turtle.get_move())

    outfile = open("pets.csv","w")
    outfile.write("name, type, weight, limbs, age \n \n")
    
    #print(pets)

    for key in pets: # key is each pet name
        outfile.write(key + ", ") # spots, kitty, ralph
        outfile.write(pets[key][0] + ", ") # dog, cat, turtle
        outfile.write(str(pets[key][1]) + ", ") # weight
        outfile.write(str(pets[key][2]) + ", ") # limbs
        outfile.write(str(pets[key][3])) # age
        outfile.write("\n")

main()

# 1) create a class called 'Pet' and give it the following attributes. The user should assign the values of the attributes. Make sure the attributes are hidden
# 2) in your class, create get methods for each of the attributes
# 3) Create 3 different instances of your class. These can be whatever you would like them to be, as long as they are different.
# 4) Create a dictionary called 'pets' that has the pet name as the key, and the rest of the attributes as the values in a list
# 5) Create a new method of your class called 'move.' This should have the user assign a value and the method will multiply it by the limbs attribute.
# create a get attribute for this method.
# 6) print out the distance each of your pets move
# 7) create a csv file with the following format:
'''
name,type,weight,limbs,age
'''

'''
type (string) ex: 'dog'
weight (string) ex: '24.7 lbs'
limbs (int) ex: 4
age (float) ex: 2.5
name (string) ex: 'Dug'
'''
    #typePet = input("What type of pet do you have? ")
    #weight = float(input("What is your pet's weight? "))
    #limbs = float(input("How many limbs does your pet have? "))
    #age = float(input("How old is your pet? "))
    #name = input("What is your pet's name? ")