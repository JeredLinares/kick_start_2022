'''
Google Kick Start - Round D - 1
JD Linares
2022 07 10
'''
debug = True
#debug = False

def solve(input_data,cats):
    result_sum = [0]*cats
    result_count = [0]*cats

    for elm_i in range(cats): 
        result_sum[cats-1-elm_i] += input_data[len(input_data)-1-elm_i]
        result_count[cats-1-elm-i] += 1



    positiion_i = 0
    for elm_i in range(len(input_data)):
        searching = True
        while searching: 
            if



        pos_i < len(result_sum):
            if result_sum[elm_i] < result_sum[elm_i+1]:
                result_sum[elm_i] += input_data[elm_i]



        

    return result

for case_i in range(int(input())):
    if debug: print(f"\nStarting case: {case_i+1}")
    result = 0

    input_tests = [int(digit) for digit in input().split()]
    regions = input_tests[0]
    categories = input_tests[1]
    if debug: print(f"Regions: {regions} , Categories: {categories}")
    input_data = [int(digit) for digit in input().split()]
    sorted(input_data)
    if debug: print(input_data)

    if categories == 1:
        elm_sum = 0
        elm_count = 0
        for elm_i in input_data:
            elm_sum += elm_i
            elm_count += 1
        print(f"Case #{case_i+1}: {elm_sum / elm_count}")
    else: 
        result  = solve(input_data,categories)
        if debug: print(result)
        print(f"Case #{case_i+1}: {result}")
    
if debug: print()
    








