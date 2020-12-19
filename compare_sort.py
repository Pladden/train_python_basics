import timeit

import sort

def check_order_asc():
	a = [5, 7, 2, 18, 65, 5, 7, 2, 18, 65, 5, 7, 2, 18, 65, 5, 7, 2, 18, 65]
	sort.order_asc(a)

t = timeit.timeit(check_order_asc)
print(t)

def bubble_order():
	a = [5, 7, 2, 18, 65, 5, 7, 2, 18, 65, 5, 7, 2, 18, 65, 5, 7, 2, 18, 65]
	sort.bubble_order(a)

t = timeit.timeit(bubble_order)
print(t)