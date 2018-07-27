import numpy as np


#hist_less_4 = np.zeros((50,1))
#hist_4_to_10 = np.zeros((50,1))
#hist_10_to_25 = np.zeros((50,1))
#hist_25_to_50 = np.zeros((50,1))
#hist_50_to_100 = np.zeros((50,1))


#def add_in_histogram(value, vector):
#	index = int(value * 10)
#	vector[index] = vector[index] + 1

cum_diff_4 = 0
cum_diff_10 = 0
cum_diff_25 = 0
cum_diff_50 = 0
cum_diff_100 = 0

count_4 = 0
count_10 = 0
count_25= 0
count_50 = 0
count_100 = 0

for i in range(0, 1000000):
	l = np.random.randint(1, 10)
	L = np.random.randint(1, 10)
	M = np.random.rand(l, L) * 5
	A = M.mean()

	if l*L < 4:
		cum_diff_4 = cum_diff_4 + np.absolute(2.5 - A)
		count_4 = count_4 + 1
	elif l*L < 10:
		cum_diff_10 = cum_diff_10 + np.absolute(2.5 - A)
		count_10 = count_10 + 1
	elif l*L < 25:
		cum_diff_25 = cum_diff_25 + np.absolute(2.5 - A)
		count_25 = count_25 + 1
	elif l*L < 50:
		cum_diff_50 = cum_diff_50 + np.absolute(2.5 - A)
		count_50 = count_50 + 1
	else:
		cum_diff_100 = cum_diff_100 + np.absolute(2.5 - A)
		count_100 = count_100 + 1

avg_diff_4 = cum_diff_4/count_4
avg_diff_10 = cum_diff_10/count_10
avg_diff_25 = cum_diff_25/count_25
avg_diff_50 = cum_diff_50/count_50
avg_diff_100 = cum_diff_100/count_100

print("avg_diff_4: " + str(avg_diff_4))
print("avg_diff_10: " + str(avg_diff_10))
print("avg_diff_25: " + str(avg_diff_25))
print("avg_diff_50: " + str(avg_diff_50))
print("avg_diff_100: " + str(avg_diff_100))
