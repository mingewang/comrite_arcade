
print(f'Invoking __init__.py for {__name__}') 
MY_CONSTS = ['A', 'B', 'C']

# https://docs.python.org/3/tutorial/modules.html
# user need to use from my_module import * as convention
# system will import all modules
# just import my_mdoule will not work
__all__ = [ "my_greet", "my_greet2"]

# the following works 
# import my_module
#import my_greet
import my_module.my_greet as my_greet

#this does NOT work, always complains
# ModuleNotFoundError: No module named 'my_greet2'
# import my_greet2

# strange, the second import need this format
import my_module.my_greet2 as my_greet2