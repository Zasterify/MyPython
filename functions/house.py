def house_paid(bungalow, duplex, hut):
    '''
    To define the function called 'house_paid' with 3 arguments
    '''
    if bungalow and not duplex and not hut:  # if bungalow is true, duplex and hut are false
        return ('Congratulations! You got it.')
    elif not bungalow and duplex and not hut:  # if duplex is true, bungalow and hut are false
        return ('Cool! You tried it.')
    elif not bungalow and not duplex and hut:  # if hut is true, bungalow and duplex are false
        return ('Ah! Shame on you.')
    else:
    



