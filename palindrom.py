

def reverse_str(s):
  str = ""
  for i in s:
      str = i + str
  return str

# Function to reverse a string
def reverse_str2(s):
  string = s[::-1]
  return string

def is_palindrome(s):
  reversed_s = reverse_str(s)

  if reversed_s == s:
    return True

  return False

def is_palindrome2(s):
  s_len = len(s)
  # 0 ,1 ... s_len/2-1 ....
  #for i in range(0,int(s_len/2-1)):
  for i in range(0,s_len//2):
    # check the 0---middle s 
    if s[i] != s[ s_len-1 - i ]:
      return False
  return True 


test = input("please input word to check: " )
print("check palindrome: ", test , " is :",  is_palindrome(test) )
print("check palindrome2: ", test , " is :",  is_palindrome2(test) )

