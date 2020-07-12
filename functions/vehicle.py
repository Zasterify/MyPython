vehicle = input('Enter your transport: ')  
'''to discover transport as you like'''
if vehicle == 'cab':  # if you pick a cab for going to work
    print('It will take you to work for 15 minutes.')
elif vehicle == 'bus':  # if you pick a bus for going to work
    print('It will take you there for 45 minutes.')
elif vehicle == 'bicycle':  # if you pick a bicycle for going to work
    print('It will take you there for an hour.')
else:  # if not, you have no options for going to work
    print('Oops, you are late to work.')

