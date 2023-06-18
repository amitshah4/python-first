#Better use of variables - Instead of mins we wnat seconds 

def conv_calc():
    return 24*60*60
#def a function, it has access to all variables defined earlier
def calculate_for_days():
    print(f"Total {covernsion_label} in a {how_many_days2} days: {how_many_days2*conversion_calc}") # Simpler to read with F


#def a function with parameters
def calculate_for_days_value(how_many):
    print(f"Total {covernsion_label} in a {how_many} days: {how_many*conversion_calc}") # Simpler to read with F


how_many_days = 1 # days 
how_many_days1 = 5 # days 
how_many_days2 = 10 # days 

conversion_calc =  conv_calc() # If you want seconds
covernsion_label ="seconds"

#How many {covernsion_label} in a day
#Note spaces are added when using comma 
print(f"Total {covernsion_label} in a {how_many_days} days: {how_many_days*conversion_calc}") # Simpler to read with F
print(f"Total {covernsion_label} in a {how_many_days1} days: {how_many_days1*conversion_calc}") # Simpler to read with F
print(f"Total {covernsion_label} in a {how_many_days2} days: {how_many_days2*conversion_calc}") # Simpler to read with F

calculate_for_days() # Calling a function

#Call function with params
calculate_for_days_value(1)
calculate_for_days_value(2)
calculate_for_days_value(3)
calculate_for_days_value(10)
calculate_for_days_value(20)