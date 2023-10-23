import random

characters= ['!','@','#','$','%','^','&','*','+',':','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','g','h']

lenght = int (input ('number of characters: '))

# shuffle characters, this is a feature of the random function
random.shuffle(characters) 

#index out first character to the lenght entered 
pw_char = (characters[0:lenght]) 

#joins the individual elements of char into a new string as password  
new_pw = ''.join(pw_char) 

print("your pw is: ", new_pw)
