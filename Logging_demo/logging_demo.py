# 5 levels of logging
# 1. DEBUG
# 2. INFO
# 3. WARNING (Default)
# 4. ERROR(Default)
# 5. CRITICAL

import logging


#using logger method
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(name)s:- %(levelname)s: %(asctime)s: %(message)s')
filenamehandler = logging.FileHandler('debug.log')
filenamehandler.setFormatter(formatter)
logger.addHandler(filenamehandler)

#using basic config method
#logging.basicConfig(level=logging.DEBUG)
#logging.basicConfig(filename='debug.log', level=logging.DEBUG)
#logging.basicConfig(filename='debug.log', level=logging.DEBUG, format = '"%(levelname)s: %(asctime)s: %(message)s"')

def add(x,y):
    return x + y

def sub(x,y):
    return x - y


num1 = 20
num2 = 15

add_result = add(num1,num2)
logger.debug(f'Adding {num1} + {num2} = {add_result}')
# logging.debug(f'Adding {num1} + {num2} = {add_result}')
#calling logging methods should be lowercase and only in basicconfig method, parameter should be upper case

sub_result = sub(num1,num2)
logger.warning(f'Subtracting {num1} - {num2} = {sub_result}')
# logging.debug(f'Adding {num1} + {num2} = {add_result}')

