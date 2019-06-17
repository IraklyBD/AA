
from colorama import init
from colorama import Fore, Back, Style

init()

print(Back.WHITE)
print(Fore.BLACK)
print(Style.NORMAL)
what = input('What do? (+/-): ')

a = float(input ('Input first unit: '))
b = float(input ('Input second unit: '))

if what  == '+':
    c = a + b
    print('Result is: ' +  str(c))
elif what == '-':
    c = a - b
    print('Result is: ' +  str(c))
else:
    print('You are moron')