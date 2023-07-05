import matplotlib.pyplot as plt
import numpy as np

size_and_count = { 17: 10, 22: 10, 27: 18, 32: 6, 37: 8, 42: 10, 47: 5, 52: 3, 57: 4 }


class_size  = [k for k,v in size_and_count.items()]
class_count = [v for k,v in size_and_count.items()]
class_pmf   = [round(v/sum(class_count),3) for k,v in size_and_count.items()]
class_mean  = np.round(np.array(class_pmf).mean(), 2)
mean=round(sum(list(map(lambda x,y: x*y,class_size,class_pmf))),2)

print("class size: \t", class_size)
print("class count: \t", class_count)
print("class pmf: \t", class_pmf)
print("probability :\t", sum(class_pmf))
print("Mean: \t",mean)

plt.style.use('ggplot')
plt.figure(figsize=(5,5))
plt.title("A Probability Mass Function")
plt.bar(class_count,class_pmf)
plt.show()

