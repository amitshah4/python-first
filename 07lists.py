import re
covernsion_label = "hours" ### Global VARIABLES 
total_wrong_inputs = 0

#Better use of variables - Instead of mins we wnat seconds 
def conv_calc():
    return 24

def string_clean_restart(user_input):
 
    re_count = 0
    # python string replace space with comma
    user_input = re.sub("\s+", ",", user_input.strip())
    user_input = user_input.split(",") #Default takes spaces 

    # using remove() to perform removal
    while("" in user_input):
        user_input.remove("")
        
    for every_input in user_input:
        re_count+=1
        #run till user input to exit
        if every_input!='exit' and total_wrong_inputs<5:
            print(calculate_for_days_value(every_input))
        else:
            break
        if(re_count == len(user_input)):
            re_count=0
            user_input = input('"All inputs are completed, you need to enter new values" \n') #List input 
            string_clean_restart(user_input)
            
    
#def a function with to calculate user input  
def calculate_for_days_value(how_many):
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
        return f"You have total 5 invalid input attemps, Current Count: {total_wrong_inputs}"
        
user_input = input('How about you pass a list of days \n') #List input 
string_clean_restart(user_input)



