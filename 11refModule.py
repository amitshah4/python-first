from _01helper import string_clean_restart, user_message_list

import os
print(os.name)

import logging
logger = logging.getLogger("MAIN")
logger.error("Error happened")

user_input = input(f'{user_message_list} \n') #List input 

'''
You can inlcude entire module or just partial
import _01helper
_01helper.string_clean_restart(user_input)

Alternatively you can import everything
from 01_helper import * 

So what is the difference 
When you import everything with * you dont need to put module.functionname 

'''
string_clean_restart(user_input)


'''
import datetime
import math
import os
'''
