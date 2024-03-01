                # PERCENT SIGN (%) FORMATTING
                
mass_percent = "1/6"
print("On the moon, you would weight about %s of your wight." % mass_percent) 

print("""Both sides of the %s get the same amount of sunlight, but only one side is seen from %s because the %s rotates around its own axis when it orbits %s.""" % ("Moon", "Earth", "Moon", "Earth"))

                # FORMAT METHOD
                
mass_percent = '1/6'
print("On the Moon, you would weigh about {} of your weight on Earth.".format(mass_percent))

mass_percentage = "1/6"
print("""You are lighter on the {0}, because on the {0} you would weigh about {1} of your weight on Earth.""".format("Moon", mass_percentage))

        # F-strings
        
print(f"On the Moon, you would weigh about {round(1/6, 2)}% of your weight on Earth.")

subject = "interesting facts about the moon"
heading = f"{subject.title()}"
print(heading)