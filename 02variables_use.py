#Better use of variables - Instead of mins we wnat seconds 

how_many_days = 10 # days 

conversion_calc = 24*60*60 # If you want seconds
covernsion_label ="seconds"

#How many mins in a day
#Note spaces are added when using comma 
print("Total mins in a", how_many_days, covernsion_label, ":", how_many_days*conversion_calc) #String concatenation 
print("Total mins in a " + str(how_many_days) +" " + str(covernsion_label) +" : "+ str(how_many_days*conversion_calc))  #String concatenation with conversion
print(f"Total mins in a {how_many_days} {covernsion_label}: {how_many_days*conversion_calc}") # Simpler to read with F
