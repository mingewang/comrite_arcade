# use lib https://github.com/sepandhaghighi/art

from art import *

Art=text2art("art")
print(Art)

Art=text2art("art",font='block',chr_ignore=True)
print(Art)

art1 = text2art("art",decoration="barcode1") 
print(art1)


tprint("art")
tprint("art",font="block",chr_ignore=True) # print ASCII text (block font)

tprint("test","random") # random font mode

tprint("1","wizard")

tprint("1"*15,"wizard")
