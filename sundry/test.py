import numpy as np
from itertools import permutations

sample_space = {x for x in range(1, 11)}

# Count the number of even numbers in the sample space
possible_outcomes = len([num for num in sample_space if num % 2 == 0])

event_A = {x for x in sample_space if x % 2 == 0}
event_B = {x for x in sample_space if x % 2 != 0}
event_A_complement = sample_space - event_A
event_B_complement = sample_space - event_B

print("Sample Space:", sample_space)
print("Possible Outcomes (even numbers):", possible_outcomes)
print("Even Numbers:", event_A)
print("event A 'Even Numbers' (sorted):", sorted(event_A))
print("event B 'Odd Numbers' (sorted):", sorted(event_B))
print("Sample Space Complement:", sample_space - event_A)
print(event_A_complement.union(event_B_complement) == sample_space)
