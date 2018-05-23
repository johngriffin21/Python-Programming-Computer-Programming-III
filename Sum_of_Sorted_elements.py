def sum_to_k(lst, k):
	i = len(lst)-1
	for num in lst:
		if num + i == k:
			print(num, i)
		i = i - 1
