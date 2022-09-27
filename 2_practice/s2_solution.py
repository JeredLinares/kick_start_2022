'''
Google Kick Start - Practice 2 - 2
JD Linares
2022 07 10
remember: list.copy()   
'''
debug = False
debug = True

def subF1(raw_data):
    if debug: print(raw_data)
    base_char_arr = [0]*26
    return_arr = []
    for char_i in raw_data:
        base_char_arr[ord(char_i)-65] += 1
        return_arr.append(base_char_arr.copy())
    return return_arr
        

def subF2(data,params):
    unmatched_letters = 0

    if params[0]==0 and params[0]==params[1]:
        for char_i in range(26):
            unmatched_letters += data[params[0]][char_i] % 2
    else:
        for char_i in range(26):
            unmatched_letters += (data[params[1]][char_i] - data[params[0]][char_i]) % 2

    return unmatched_letters < 2


for case_i in range(int(input())):
    if debug: print(f"\nStarting case: {case_i+1}")
    result = 0

    input_test = [int(digit) for digit in input().split()]

    input_data = input()
    processed_data = subF1(input_data)
    if debug: print(*processed_data,sep='\n')
    

    for test_i in range(input_test[1]):
        test_i_params = [int(digit)-1 for digit in input().split()]
        if debug: print(test_i_params)
        result += subF2(processed_data,test_i_params)

    print(f"Case #{case_i+1}: {result}")

    
