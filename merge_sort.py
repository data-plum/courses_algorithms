def merge_sort(alist):
	print("Splitting ",alist)

	if len(alist) > 1:
		mid = len(alist) // 2
		lefthalf = alist[:mid]
		righthalf = alist[mid:]

		merge_sort(lefthalf)
		merge_sort(righthalf)

		i = 0
		j = 0
		k = 0

		while i < len(lefthalf) and j < len(righthalf):
			if lefthalf[i] < righthalf[j]:
				alist[k] = lefthalf[i]
				i += 1
				k += 1
			else:
				alist[k] = righthalf[j]
				j += 1
				k += 1

		while i < len(lefthalf):
			alist[k] = lefthalf[i]
			i += 1
			k += 1

		while j < len(righthalf):
			alist[k] = righthalf[j]
			j += 1
			k += 1
	return(alist)

alistt = [[54, 26, 93, 17, 77, 31, 44, 55, 20,], [1, 3, 1, 3, 4, 5, 5, 6, 6, 10], [1, 1, 2, 1, 1, 3, 2, 0]]
sorted_alist = []
for alist in alistt:
	sorted_alist.append(merge_sort(alist))
print(sorted_alist)
