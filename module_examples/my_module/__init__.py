
print(f'Invoking __init__.py for {__name__}') 
MY_CONSTS = ['A', 'B', 'C']

#import my_greet
import my_module.my_greet as my_greet
#this does NOT work, always complains
# ModuleNotFoundError: No module named 'my_greet2'
# import my_greet2

# strange, the second import need this format
import my_module.my_greet2 as my_greet2