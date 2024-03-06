            ## Creating a Dictionary
            
# Python uses curly braces ({ }) and the colon (:) to denote a dictionary. 
# You can either create an empty dictionary and add values later, or populate it at creation time. 
# Each key/value is separated by a colon, and the name of each key is contained in quotes as a string literal. 
# Because the key is a string literal, you can use whatever name is appropriate to describe the value.

from os import name


planets = {
    'name' : 'Earth',
    'moons': float(1)
}

            ## Reading Dictionary values

print(planets.get('name'))
print(planets.get('moons'))
print(planets['name']) #With brackets it shows the keys contained in the variable planets

            ## Get values on dictionary
print(planets.get('name'))
#print(planets['moon']) #--> Throws error because it does not exists

            ## Updating dictionary
planets.update({'name': 'Earth_1'})
print(planets)

planets['name'] = 'Earth_01'
print(planets)

            ## Add and Remove keys
## Add
planets['orbital_period'] = float(4333.00)
print(planets)
## Remove
planets.pop('orbital_period')
print(planets)

            ## Complex Data Types
## Dictionary within dictionary

planets['diameter (km)'] = {
    'polar' : float(133709.00),
    'equatorial' : float(142984.00)   
}
print(planets)
for planet in planets:
    print(planet)
    
print(f'{planets["name"]} polar diameter: {planets["diameter (km)"] ["polar"]}')