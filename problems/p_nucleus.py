# implement a function that
# sum(p_vector) = 1, len(p_vector) >= 1, p is a float between (0,1], within p_vector, find the n largest elements in p_vector such that their sum >= p
# within the n picked numbers, do a random sampling with weight
import random
from collections import Counter

def p_sample(p_vector:list[float], p:float) -> int:
    new_p = []
    for i in range(len(p_vector)):
        new_p.append((p_vector[i], random.random(), i))
    new_p.sort()
    p_sum = 0
    for i in range(len(new_p)):
        p_sum += new_p[i][0]
        new_p[i] = p_sum, new_p[i][1], new_p[i][2]
        if p_sum >= p:
            new_p = new_p[:i+1]
            break 
    rand_float = random.random() * p_sum
    for p_cap, _, i in new_p:
        if rand_float < p_cap:
            return i 


#  print(p_sample([0.1 for i in range(10)], 0.67))
p_vec =  [0.1 for i in range(10)]
counter = Counter()
for i in range(1000):
    idx = p_sample(p_vec, 0.67)
    counter[(idx, p_vec[idx])] += 1
    
for key, val in counter.items():
    print(f"{key}: {val / 1000: .3f}")