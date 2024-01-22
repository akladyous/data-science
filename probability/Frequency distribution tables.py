import numpy as np
import matplotlib.pyplot as plt

# scores=np.array([x for x in range(15,56)]).repeat(np.random.randint(1,10,size=1))
scores=[5,2,2,3,3,3,3,2,3,6,9,1,3,4,9,5,10,1,1,5,6,1,1,1,10,3,4,2,9,8,6,10,9,7,7,4,2,6,7,8,9,4]
# print(scores)

data,frequency = np.unique(scores, return_counts=True)
# relative_frequency = list(map(lambda x: x/frequency.sum(), frequency))
relative_frequency = np.array(list(map(lambda x: x/frequency.sum(), frequency)))
cumulativa_frequency = np.cumsum(frequency)
# print(frequency)
# print(relative_frequency)
# print(np.sum(relative_frequency))
# print(np.cumsum(frequency))

print(scores)
print(cumulativa_frequency)
plt.hist(cumulativa_frequency, bins=10)
plt.show()