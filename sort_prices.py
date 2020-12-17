import sort

def main():
	# prices = [440.14, 1010.63, 186.4, 434.89, 66.8, 104.81]
	prices = []
	for i in  range (1000):
		user_input = input('Enter a price or empty enter to finish: ')
		price = sort.get_number(user_input)
		if price is None:
			break
		prices += [price]
	ordered_prices = sort.order_desc(prices)
	print ('ordered prices: ', ordered_prices)
	print ('original prices: ', prices)


main()

