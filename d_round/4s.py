'''
Google Kick Start - Round D
JD Linares
2022 07 10
'''
debug = True
#debug = False

def who_2(st_list,guest_n):
    clear = [0]*guest_n
    for elm in st_list:
        clear[elm[1]] += 1
    for elm_i in range(clear):
        if 


for case_i in range(int(input())):
    if debug: print(f"\nStarting case: {case_i+1}")
    result = 0

    input_data = [int(digit) for digit in input().split()]  # guests, witness statements, max cookie stealers
    guest_n = input_data[0]
    statements_n = input_data[1]
    stealers_n = input_data[2]
    if debug: print(f"Guests: {guest_n} Statements: {statements_n} Stealers {stealers_n}")
    
    statements_list = []
    for element_i in range(statements_n):
        statements_list.append([int(i) for i in input().split()])
    
    if debug: print(*statements_list,sep="\n")

    who_2(statements_list,guest_n)



    print(f"Case #{case_i+1}: {result}")

if debug: print()
