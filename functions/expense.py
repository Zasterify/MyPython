def apartment_cost(nights):  
  '''to define the function called apartment'''
  return 25 * nights  # to know how much spent per nights

def snack_price(snack):
  ''' to define the funtion called snack_price'''
  if snack == 'cookie':  # if you prefer to consume cookie
    return 2.25
  elif snack == 'pizza':  # if you prefer to consume pizza
    return 10.45
  elif snack == 'crisp':  # if you prefer to consume crisp
    return 3.30
  elif snack == 'candy':  # if you prefer to consume candy
    return 7.40

def cab_cost(days): 
  '''to define the function called cab_cost'''
  costs = 40 * days  # to notice how many days you spent per ride
  if days <= 4:  # if it is less than 4 days
    costs -= 30  # to discount your price
  elif days >= 5:  # if it is more than 5 days
    costs -= 50  # to discount your price
  return costs 

def total_cost(snack, days, expenditure):  
  '''to define the function called total_cost with 3 arguments'''
  return cab_cost(days) + apartment_cost(days - 1) + snack_price(snack) + expenditure  # to calculate the amount of prices