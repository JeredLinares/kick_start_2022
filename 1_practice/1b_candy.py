'''
Kickstart Practice 2022 
Practice 01.1
20220921
'''


for case_i in range(int(input())):
    bags_kids = [int(digit) for digit in input().split()]
    candy_sum = 0 
    for bag_i in input().split():
        candy_sum += int(bag_i)
    print(f"Case #{case_i + 1}: {candy_sum % bags_kids[1]}")

