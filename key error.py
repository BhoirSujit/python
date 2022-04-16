Rate = { 'bottle' : 5, 'chair' : 1200, 'pen' : 50}
item = input('Enter the item: ')
try:
    print(f'The rate of {item} is {Rate[item]}')
except KeyError:
    print(f'The price of {item} is not found')