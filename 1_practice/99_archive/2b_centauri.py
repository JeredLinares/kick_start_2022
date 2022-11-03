'''
Kickstart Practice 2022 
Practice 1 - Centauri Prime
20220921
'''
import re

for case_i in range(int(input())):
    #bags_kids = [int(digit) for digit in input().split()]
    
    nation = input()
    last_letter = nation[-1]

    if last_letter in "Yy":
        print(f"Case #{case_i + 1}: {nation} is ruled by nobody.")
    elif last_letter in "AaEeIiOoUu":
        print(f"Case #{case_i + 1}: {nation} is ruled by Alice.")
    else:
        print(f"Case #{case_i + 1}: {nation} is ruled by Bob.")
