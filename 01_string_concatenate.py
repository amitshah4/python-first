#First Example - Variable  
first_number=2
string_number='5'
float_number = 0.99


how_many_days = 10

print("Data types and conversion: ", first_number+int(string_number)+float_number) # Data type conversion

#How many mins in a day
#Note spaces are added when using comma 
print("Total mins in a", how_many_days, "days:", how_many_days*24*60) #String concatenation 

print("Total mins in a " + str(how_many_days) + " days: "+ str(how_many_days*24*60))  #String concatenation with conversion

print(f"Total mins in a {how_many_days} days: {how_many_days*24*60}") # Simpler to read with F
