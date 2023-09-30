#import my_greet
#my_greet = my_greet.greet("alex")

#from my_module.my_greet import greet
import my_module.my_greet
import my_module.my_greet2
#my_greet = my_module.my_greet.greet("alex")
my_greet = my_module.my_greet.greet1("alex")
print(my_greet)

my_greet2 = my_module.my_greet2.greet2("alex")
print(my_greet2)
