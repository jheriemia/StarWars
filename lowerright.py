def main(size):
	i = 1

	while i <= size:
		j = 1
		while j <= size:
			if j >= i:
				print('*', end='')
			else:
				print(' ', end='')
			j += 1
		print()
		i += 1
	
main(5)
