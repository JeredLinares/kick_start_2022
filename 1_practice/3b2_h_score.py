'''
Google Kick Start
H-Index
JD Linares
20201006
1. iterate through citation count
2. if count >= index, add to heap and increment score
3. while heap[0] < index, pop

'''

# Min heap will hold past elements higher than index 
import heapq


for case_i in range(int(input())):
    input()
    dataset = [int(i) for i in input().split()]
    
    score = 0
    prio_q = []
    # Iterate through citation counts
    for i in range(len(dataset)):
        if dataset[i] > score:
            heapq.heappush(prio_q,dataset[i])
        while prio_q and prio_q[0] <= score:
            heapq.heappop(prio_q)
        if len(prio_q) > score:
            score += 1
        print(score) 


    print(f"Case {case_i+1}: ")


