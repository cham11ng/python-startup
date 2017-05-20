# Statistics Module

import statistics

data = [1, 2, 3, 4, 5, 6, 2, 2, 3, 2, 1, 10]

mean = statistics.mean(data)
median = statistics.median(data)
mode = statistics.mode(data)
standardDeviation = statistics.stdev(data)

print('Mean of Following Data: ', mean)
print('Mode of Following Data: ', mode)
print('Median of Following Data: ', median)
print('Standard Deviation of Following Data: ', standardDeviation)
