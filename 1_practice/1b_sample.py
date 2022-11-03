'''
Kick Start Practice 1 - Sample
JD Linares
11/3/2022
'''

# Iterate through each case for solution
for case in range(int(input())):
    # number of candy bags and kids
    line1 = [int(x) for x in input().split()]
    # number of candies in each bag
    line2 = [int(x) for x in input().split()]
    # sum the candies
    candy_total = 0
    for element in line2:
        candy_total += element
#    print(candy_total)

    print(f"Case #{case+1}: {candy_total%line1[1]}")

