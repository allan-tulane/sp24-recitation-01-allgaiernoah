import tabulate
import time


def linear_search(mylist, key):
	for i,v in enumerate(mylist):
		if v == key:
			return i
	return -1


def binary_search(mylist, key):
	return _binary_search(mylist, key, 0, len(mylist)-1)

def _binary_search(mylist, key, left, right):
	if left <= right:
		mid = (left + right) // 2
		if mylist[mid] == key:
			return mid
		elif mylist[mid] < key:
			return _binary_search(mylist, key, mid + 1, right)
		else:
			return _binary_search(mylist, key, left, mid - 1)
	else:
		return -1

  

def time_search(search_fn, mylist, key):
	start_time = time.time()
	search_fn(mylist, key)
	end_time = time.time()
	return (end_time - start_time) * 1000

def compare_search(sizes=[1e1, 1e2, 1e3, 1e4, 1e5, 1e6, 1e7]):
	results = []
	for size in sizes:
		n = int(size)
		mylist = list(range(n))
		linear_time = time_search(linear_search, mylist, -1)
		binary_time = time_search(binary_search, mylist, -1)
		results.append((n, linear_time, binary_time))
	return results

def print_results(results):
	print(tabulate.tabulate(results, headers=['n', 'linear', 'binary'], floatfmt=".3f", tablefmt="github"))

print_results(compare_search())
