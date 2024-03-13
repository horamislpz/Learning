class Spaceship:
    # Class attribute
    tractor_beam = 'off'
    
       # Instance attributes
    def __init__(self, name, kind, speed):
        self.name = name
        self.kind = kind
        self.speed = 900
        
          # Instance methods
    def warp(self, warp):
        self.speed = warp
        print(f'Warp {warp}, engage!')
        
    def tractor(self):
        if self.tractor_beam == 'off':
            self.tractor_beam = 'on'
            print('Tractor beam on.')
        else:
            self.tractor_beam = 'off'
            print('Tractor beam off')
            
ship = Spaceship('Mockingbird', 'rescue frigate', 'speed')

print(ship.name)
print(ship.kind)
print(ship.speed)
print(ship.tractor_beam)

ship.warp(1800)
ship.speed

ship.tractor()
print(ship.tractor_beam)


# For example, if the class were Spaceship, then attributes might be:

# name

# kind

# speed

# tractor_beam

# These attributes could be accessed by typing:

# Spaceship.name

# Spaceship.kind

# Spaceship.speed

# Spaceship.tractor_beam 

# Notice that these characteristics are accessed using only a dot. 

# On the other hand, methods of the Spaceship class might be:

# warp()

# tractor() 

# These methods could be used by typing:

# Spaceship.warp() 

# Spaceship.tractor()

# Notice that methods are followed by parentheses, and it’s possible for them to take arguments. For example, Spaceship.warp(7) could change the speed of the ship to warp seven.