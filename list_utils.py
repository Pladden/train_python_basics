def sum(a):
	s = 0
	for e in a:
		s = s + e
	return s


def average(a):
	av = sum(a) / len(a)
	return av


def multiply(a):
	m = 1
	for e in a:
		m = m * e
	return m


def median(a):
	a.sort()
	mid_i = len(a) / 2
	mid_i = int(mid_i)
	return a[mid_i]


def make_positive(a):
	n_elements = len(a)
	for i in range(n_elements):
		if a[i] <= 0:
			a[i] = 1
	return a


def no_bad_marks(m):
	n_elements = len(m)
	for i in range(n_elements):
		if m[i] < 5:
			m[i] = 5
	return m