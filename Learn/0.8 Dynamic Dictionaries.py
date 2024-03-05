            # Dynamic Dictionaries
            
# To print every Key in a Dictionary

rainfall = {
    'november'.title() : 3.4,
    'december': 2.6,
    'january' : 8.9
}
for key in rainfall.keys():
    print(f'{key.title()}:{rainfall[key]} cm')
print('---------------------------------------------\n')

# Determine if a key exists in a dictionary

if 'may' in rainfall:
    rainfall['may'] = 9.8
else:
    rainfall.update({'may': 9.8})
print(rainfall)
print('\n')

if 'may' in rainfall:
    rainfall['may'] = round(rainfall['may'] + 156.9/3, 2)

print(rainfall)