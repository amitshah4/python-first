covernsion_label ="seconds" ### Global VARIABLES 

#Better use of variables - Instead of mins we wnat seconds 
def conv_calc():
    return 24*60*60

#def a function with multiple parameters & local varialbles 
def calculate_for_days_value(how_many,new_variable_sample):
    local_test_variable=10; #LOCAL SOPE OF VARIABLE 
    print(f"Total {covernsion_label} in a {how_many} days: {how_many*conversion_calc}") # Simpler to read with F
    print(new_variable_sample, local_test_variable)

conversion_calc =  conv_calc() # If you want seconds

#Call function with params
calculate_for_days_value(1,'New text')
calculate_for_days_value(2,'New text2')
calculate_for_days_value(3,'New text again')
calculate_for_days_value(10,'Wow')
calculate_for_days_value(20,'How about you let us konw how many days?')