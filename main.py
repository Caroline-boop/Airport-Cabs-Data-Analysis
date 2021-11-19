import numpy as np

taxi = np.genfromtxt('nyc_taxis.csv', delimiter = ',', skip_header=True)

speed = taxi[:, 7]/ (taxi[:,8]/3600)

mean_speed = speed.mean()
print(mean_speed)

''' Calculate the number of rides taken in the month of February '''

rides_feb = taxi[taxi[:, 1] == 2, 1]
print(rides_feb.shape[0])

''' Calculate the number of rides with a tip greater then $50 '''

print(taxi[taxi[:, -3] > 50, -3].shape[0])

''' Calculate the number of rides where drop was JFK airport '''

print(taxi[taxi[:, 6] == 2, 6].shape[0])