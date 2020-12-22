import dict_utils

def test_get_moldovan_contacts():
	numbers = {'petrov': '+373 764 36 54', 'ivanov': '+8 800 555 3 555'}
	result = dict_utils.get_moldovan_contacts(numbers)
	expected = {'petrov': '+373 764 36 54'}
	assert expected == result