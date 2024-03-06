        # Keyword Arguments - 
        
from datetime import date, timedelta, datetime

def arrival_time(hours=51):
    now = datetime.now()
    arrival = now + timedelta(hours=hours)
    return arrival.strftime("Arrival: %A %H:%M")
output = arrival_time(hours=50)
print(output)
#-----------------------------------------------------------------------#
        #Exercise from one of the Functions file
        
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

def days_complete(distance, speed=80): #Keyword Arguments
    time = float(distance)/float(speed)
    return time
    
for planet in planets.keys():
    distancePlanets = planets.get(planet)
    days_complete(distancePlanets) 
    #The functions needs at least one argument, but not the one thats specified in the definition
    #Thats why the argument 'speed' does not need to be present when callin the function
    # days_complete(distancePlanets, speed) --> days_complete(distancePlanets) --> Line 30
    
    tripTime = days_complete(distancePlanets)
    tripDays = tripTime/24
    print('From Sun to : ', planet, '---> Time in hours: ', '{:.3f}'.format(tripTime, 3), '---> Time in Days: ', '{:.3f}'.format(tripDays, 3))
    
    #print('Planet: ', planet, '--> Distance: ', '{:.3f}'.format((distancePlanets)))
    

                #--------- Variable Arguments --------- #-
                


