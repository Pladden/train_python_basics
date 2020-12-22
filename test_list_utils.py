import list_utils

def test_sum():
	a = [5, 3, 7, 2]
	result = list_utils.sum(a)
	expected = 17
	assert expected == result


def test_average():
	a = [5, 3, 7, 2]
	result = list_utils.average(a)
	expected = 4.25
	assert expected == result


def test_multiply():
	a = [5, 3, 7, 2]
	result = list_utils.multiply(a)
	expected = 210
	assert expected == result


def test_multiply_2():
	a = [5, 3, 7, 0, 2]
	result = list_utils.multiply(a)
	expected = 0
	assert expected == result


def test_median():
	a = [5, 7, 7, 7, 9, 9, 10, 8, 8, 8, 8]
	result = list_utils.median(a)
	expected = 8
	assert expected == result


def test_make_positive():
	a = [5, 3, -7, 2, 0 ]
	result = list_utils.make_positive(a)
	expected = [5, 3, 1, 2, 1 ]
	assert expected == result


def test_no_bad_marks():
	m = [9, 8, 4, 2]
	result = list_utils.no_bad_marks(m)
	expected = [9, 8, 5, 5]
	assert expected == result