'''
H Score
JD Linares
20220922
'''

import pdb
import heapq    
    # heapify(x)            turn list x into a heap
    # heappush(x, item)     add item to the heap
    # heappop(x)            pop and return smallest item

for case_i in range(int(input())):

    # Length not needed
    input()     

    data = [int(i) for i in input().split()]
    heap_data = []
    
    h_index = 0
    result = ""
    for i in range(len(data)):
        if data[i] > h_index:
            heapq.heappush(heap_data,data[i])
        while heap_data and heap_data[0] <= h_index:
            heapq.heappop(heap_data)
        if len(heap_data) > h_index:
            h_index += 1
        result += " " + str(h_index)

    print(f"Case #{case_i+1}:{result}")




