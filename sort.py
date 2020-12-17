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
	elements = list(original_elements)
	ordered_elements = list()  # []
	n_of_elements = len(elements)
	for i in range(n_of_elements):
		max_element_index = find_max_index(elements)
		max_element = elements[max_element_index]
		if max_element == -MONSTER_NUMBER:
			max_element = None
		ordered_elements += [max_element]
		elements[max_element_index] = -MONSTER_NUMBER
	return ordered_elements


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
