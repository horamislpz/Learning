            # Functions
        # Functions without arguments
            

# def rocket_parts():
#     return('propeller, payload, structure')
# # output = rocket_parts()

#         # Functions with arguments
# destination = {
#     'Moon': 238855.00,
#     'Mercury': 23947883.90
# }

# # #-------------------------------------------------------------------------------------------------------------
#     # Function
# def distance_from_earth(destination):
#     if destination == "Moon":
#         return "238,855"
#     else:
#         return "Unable to compute to that destination"
    
# variable_salida = distance_from_earth(destination='Moon')
# #variable_salida = distance_from_earth('Moon') --> Its the same result.

#     # Distance for every planet on the dictionary above
# for planet in destination.keys():
#     distance_from_earth(planet) # Calling function with the planet argument (iterable)
#     output = distance_from_earth(planet)
#     # print('Planet: ', planet, '--> Distance: ', output)

#-------------------------------------------------------------------------------------------------------------
    
    # Time to complete the travel to every planet (Function)
    # We need distance to the planet and speed travel
    # Lets say speedTravel = 80 MPH and lets use the same distance from before but more planet (Real distance)
    # Moon = 238,855.00
    # Planets	Distance from the sun (miles)
    # Mercury	35,980,000
    # Veunus	67,240,000
    # Earth	92,960,000
    # Mars	141,600,00
    # Jupiter	483,800,000
    # Saturn	890,700,000
    # Uranus	1,787,000,000
    # Neptune	2,798,000,000
    
from turtle import distance, speed


planets = {
    'Moon':     238855.00,
    'Mercury': 	35980000.00,
    'Veunus': 	67240000.00,
    'Earth':  92960000.00,
    'Mars':  141600.00,
    'Jupiter': 	483800000.00,
    'Saturn': 	890700000.00,
    'Uranus': 	1787000000.00,
    'Neptune': 	2798000000.00
}

    #Function

def days_complete(distance, speed):
    time = float(distance)/float(speed)
    return time
    
for planet in planets.keys():
    distancePlanets = planets.get(planet)
    speed = 80.00
    days_complete(distancePlanets, speed)
    
    tripTime = days_complete(distancePlanets, speed)
    tripDays = tripTime/24
    print('From Sun to : ', planet, '---> Time in hours: ', '{:.3f}'.format(tripTime, 3), '---> Time in Days: ', '{:.3f}'.format(tripDays, 3))
    
    #print('Planet: ', planet, '--> Distance: ', '{:.3f}'.format((distancePlanets)))

    
