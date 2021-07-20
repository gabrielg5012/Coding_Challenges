"""
A thief has managed to find out the four digits for an online PIN code, but doesn’t know the correct sequence 
needed to hack into the account.
Design and write a program that displays all the possible combinations for any four numerical digits entered by the
user. The program should avoid displaying the same
combination more than once.
Submit a fully detailed Showcase for your program.
"""
from itertools import permutations
pin = str(input("Input pin number: \n"))
  
a = permutations(pin, len(pin)) 
for i in a:
    print(str(i))
    
    
