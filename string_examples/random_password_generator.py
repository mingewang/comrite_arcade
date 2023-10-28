import random

def generate_pw(pw_len):
    characters= "!@#0123456789abcdefghijkmnlopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    total_chars = len(characters)
    new_pw = ""
    for i in range(0,pw_len):
        random_index_position = random.randint(0, total_chars-1)
        new_pw += characters[random_index_position] 
    return new_pw

pw_len1 = int (input ('number of characters for password1: '))
new_pw1 = generate_pw( pw_len1 ) 
print("your pw is: ", new_pw1)


def generate_pw2(pw_len):
    characters= ['!','@','#','$','%','^','&','*','+',':','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','g','h']
    # shuffle characters, this is a feature of the random function
    random.shuffle(characters) 
    #index out first character to the lenght entered 
    pw_char = (characters[0:pw_len]) 
    #joins the individual elements of char into a new string as password  
    new_pw = ''.join(pw_char) 
    return new_pw

pw_len2 = int (input ('number of characters for password 2: '))
new_pw2 = generate_pw( pw_len2 ) 
print("your pw is: ", new_pw2)