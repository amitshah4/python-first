import re
#Modules 
# Functions / Varilable that can be used inanother python File
covernsion_label = "h" ### Global VARIABLES 
conv_value = 0
total_wrong_inputs = 0

user_message_list="Please enter list of days";

#Making input dynamic based on user input 
def set_conv_calc(conversion_unit): 
    global conv_value
    global covernsion_label
    formulae = {'h':24,'m':24*60,'s':24*60*60,'e':'exit'}
    
    if conversion_unit in formulae.keys():
        if conversion_unit == 'e':
            return "exit"
        else:
            conv_value = formulae[conversion_unit]
            covernsion_label = conversion_unit
    else:
        conv_value = 0
        covernsion_label = "invalid unit, no conversion defined"
        
#Better use of variables - Instead of mins we wnat seconds 
def conv_calc():
    return conv_value

def string_clean_restart(user_input):

    conversion_unit = input('What is the coversion you need?\nSelect h: hours, m: mins, s: seconds, e:exit\n')    
    check_exit = set_conv_calc(conversion_unit)
    if(check_exit=='exit'):
        user_input='exit'
 
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
        return f"You have total 5 invalid input attemps, Current Count: {total_wrong_inputs}, String {how_many}"
