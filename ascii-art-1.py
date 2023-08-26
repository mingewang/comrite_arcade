import sys

from colorama import init
init(strip=not sys.stdout.isatty()) # strip colors if stdout is redirected
from termcolor import cprint 
from pyfiglet import figlet_format

# use pyfiglet -l to get fonts
cprint("hello world", 'blue', 'on_white')
cprint(figlet_format('missile!', font='starwars'),
       'yellow', 'on_red', attrs=['bold'])


cprint(figlet_format('missile!', font='slant'),
       'yellow', 'on_red', attrs=['bold'])

cprint(figlet_format('missile!', font='3-d'),
       'yellow', 'on_red', attrs=['bold'])

cprint(figlet_format('missile!', font='alphabet'),
       'yellow', 'on_red', attrs=['bold'])