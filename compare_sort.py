import random
import timeit

import sort

def random_list():
	n = 1000
	a = [0] * n
	for i in range(n):
		a[i] = random.random()
	return a

def check_order_asc():
	a = random_list()
	sort.order_asc(a)

t = timeit.timeit(check_order_asc, number=100)
print(t)

def bubble_order():
	a = random_list()
	sort.bubble_order(a)

t = timeit.timeit(bubble_order, number=100)
print(t)


def check_native_sort():
	a = random_list()
	a.sort()

t = timeit.timeit(check_native_sort, number=100)
print(t)
