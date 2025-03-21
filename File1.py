class car:
    def __init__(self, color:str , horsepower:int) ->None:
        self.color = color
        self.horsepower = horsepower




volvo : car = car('red',200)
print(volvo.color)
print(volvo.horsepower)

print()

bmw : car = car('blue',400)
print(bmw.color)
print(bmw.horsepower)




#creating a tuple
letter = ("a","b","c","d","e","f","g","h")
print(letter)#printing a tuple
print(letter[2])#prnting a specific letter based on indexing - c will bee dsplayed
print(letter[1:6])#Displays a range of elements from index 1 to 5 


#creating dictionary
capital_cities = {
    "Kenya":"Nairobi",
    "Nigeria":"Abuja",
    "Tanzania":"Dodoma",
    "Uganda":"Kampala"



}
print(capital_cities)
print(capital_cities["Tanzania"])

