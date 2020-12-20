MONSTER_NUMBER = 12345937597

def find_max_index(elements):
	max_index = 0
	max_e = -MONSTER_NUMBER
	n_elements = len(elements)
	for i in range(n_elements):
		e = elements[i]
		if e is not None and e > max_e:
			max_e = e
			max_index = i
	return max_index


def order_desc(original_elements):
	elements = compact(original_elements)
	elements.sort()
	elements.reverse()
	n_nones = len(original_elements) - len(elements)
	return elements + [None] * n_nones


def compact(elements):
	result = []
	for e in elements:
		if e is not None:
			result += [e]
	return result

def find_min_index(elements):
	min_index = 0
	min_e = None
	n_elements = len(elements)
	for i in range(n_elements):
		e = elements[i]
		if e is not None and (min_e is None or e < min_e):
			min_e = e
			min_index = i
	return min_index


def order_asc(original_elements):
	elements = list(original_elements)
	ordered_elements = list()  # []
	n_of_elements = len(elements)
	for i in range(n_of_elements):
		min_element_index = find_min_index(elements)
		min_element = elements[min_element_index]
		ordered_elements += [min_element]
		elements[min_element_index] = None
	return ordered_elements


def get_number(s):
	try: 
		return float(s)
	except ValueError:
		return None


def swap(a, i):
	a[i], a[i+1] = a[i+1], a[i]


def bubble_order(elements):
	n_elements = len(elements)
	need_to_order = True 
	counter = 0
	while need_to_order:
		need_to_order = False
		for i in range(n_elements-1):
			counter += 1
			if elements[i] > elements[i+1]:
				elements[i], elements[i+1] = elements[i+1], elements[i]
				need_to_order = True
		n_elements -= 1
	return counter
