import random
import statistics
list =[]
for i in range(1, 11):
    list.append(round(random.uniform(0.00, 10.00),2))
    result = 1
    for x in list:
        result = result * x
        
sum = sum(list)

print(list)
print(f'multiplication:', result)
print(f'sum:', sum)
a = statistics.mean(list)
print(f'Average:', a)
print(f'min:', min(list))
print(f'max:', max(list))