# WORKING WITH PYTHON LISTS

planets = ['Mercury', 'Earth', 'Venus', 'Mars', 'Saturn', 'Uranus', 'Neptune', 'Jupiter']

print('First planet on the list is: ' + planets[0])
print('Second planet on the list is: ' + planets[1])
print('Third planet on the list is: ' + planets[2])

planets[1] = 'Tierra'
print(planets)

                # # Lenght of a list
                
number_of_planets = len(planets)
print('Number of planets: ' + str(number_of_planets))

                # # Append to list .append(value)

planets.append('New Planet')
new_number_of_planets = len(planets)
print("New number of planets: ", new_number_of_planets)

                # # finding a value in a list (jupiter)
                
planets_loweredCase = [x.lower() for x in planets]
jupiter_find_index = planets_loweredCase.index('jupiter')
print('Jupiter is the ', jupiter_find_index + 1, 'planet from the sun')

                ## Slice Lists
                
planets = ['Mercury', 'Earth', 'Venus', 'Mars', 'Saturn', 'Uranus', 'Neptune', 'Jupiter']
planets_before_earth = planets[0:1]
print(planets_before_earth)

planets_after_earth = planets[2:]
# OR ---> planets_after_earth = planets[2::]
print(planets_after_earth)

                ## Joining and sorting lists

planets = ['Mercury', 'Earth', 'Venus', 'Mars', 'Saturn', 'Uranus', 'Neptune', 'Jupiter']
amalthea_group = ["Metis", "Adrastea", "Amalthea", "Thebe"]
new_list_joined = planets + amalthea_group
print(new_list_joined)

                ## Sort list
                
list_to_sort = planets + amalthea_group
print('List not sorted: ', list_to_sort)
list_to_sort.sort()
print('\nSorted list: ', list_to_sort, '\n')