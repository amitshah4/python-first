covernsion_label = "hours" ### Global VARIABLES 
total_wrong_inputs = 0

#Better use of variables - Instead of mins we wnat seconds 
def conv_calc():
    return 24

#def a function with to calculate user input  
def calculate_for_days_value(how_many):
    # isnumeric < Only checks for whole numbers greater than 0
    # isinstance(how_many,(int,float))
    global total_wrong_inputs
    try:
        how_many = float(how_many)
        if(how_many>0):
            return f">>> {how_many} day(s): {how_many*conv_calc()} {covernsion_label}" # Simpler to read with F
        elif(how_many==0):
            return ">> Nothing to convert"
        else:
            return ">>> Do no enter negative day(s)"  
    except ValueError:
        total_wrong_inputs+=1
        return f"You input invalid string. Please enter a valid number. TOTAL TIMES INPUT INVALID: {total_wrong_inputs}"
        
        
    #if(how_many.isnumeric()):
    # Note - IF YOU DID NOT HAVE ELSE CONDITION < NONE > would be returned
# INFINITE RUN while True:
 
user_input = input('How about you let us konw how many days? \n') #nested function call 
print(calculate_for_days_value(user_input))
