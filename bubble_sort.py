def bubble_sort(data):
	length = len(data)
	for i in xrange(0, length):
		for j in xrange(i+1, length):
			if (data[j] < data[i]):
				tmp = data[j]
				data[j] = data[i]
				data[i] = tmp

def test_func():
	arr = [4, 88, 5, 21, 92, 37, 56, 13, 75, 19, 64, 57, 94, 34, 8, 12, 71, 99, 102, 38]
	# print "before:"
	# print arr
	bubble_sort(arr)
	# print "after:"
	# print arr
test_func()