import sort


def test_find_max_index():
	# given
	elements = [3, 14, 8]
	# when
	result = sort.find_max_index(elements)
	# then
	expected = 1
	assert expected == result 


def test_find_max_index_when_empty_elements():
	# given
	elements = [None, 3, 14, None, 8]
	# when
	result = sort.find_max_index(elements)
	# then
	expected = 2
	assert expected == result 


def test_order_desc():
	elements = [7, 19, 34]
	result = sort.order_desc(elements)
	expected = [34, 19, 7]
	assert expected == result


def test_order_desc_when_empty_elements():
	elements = [None, 7, 19, None, 34]
	result = sort.order_desc(elements)
	expected = [34, 19, 7, None, None]
	assert expected == result


def test_order_asc():
	elements = [34, 7, 19]
	result = sort.order_asc(elements)
	expected = [7, 19, 34]
	assert expected == result


def test_order_asc_when_several_equal_elements():
	elements = [34, 7, 19, 34]
	result = sort.order_asc(elements)
	expected = [7, 19, 34, 34]
	assert expected == result


def test_order_asc_when_empty_elements():
	elements = [None, 34, 7.0, None, 19]
	result = sort.order_asc(elements)
	expected = [7, 19, 34, None, None]
	assert expected == result


def test_find_min_index_when_first_empty():
	elements = [None, 34, 7, None, 19]
	result = sort.find_min_index(elements)
	expected = 2
	assert expected == result


def test_find_min_index_in_texts():
	texts = ['petrov', 'ivanov', 'sokolov', 'aksenov']
	result = sort.find_min_index(texts)
	expected = 3
	assert expected == result


def test_find_min_index_in_texts_when_min_first():
	texts = ['aksenov', 'petrov', 'ivanov', 'sokolov']
	result = sort.find_min_index(texts)
	expected = 0
	assert expected == result


def test_order_asc_in_texts():
	texts = [None, 'petrov', 'ivanov', None, 'sokolov', 'aksenov']
	result = sort.order_asc(texts)
	expected = ['aksenov', 'ivanov', 'petrov', 'sokolov', None, None]
	assert expected == result
