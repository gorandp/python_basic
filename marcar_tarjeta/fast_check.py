import check_time

if __name__ == "__main__":
	with open("next_turn", 'r') as f:
		x = f.readline()
	if 's' in x:
		x = 's'
	elif 'e' in x:
		x = 'e'
	else:
		raise ValueError("File 'next_turn' does not have a valid turn type")
	check_time.addTurnNow(x)
	with open("next_turn", 'w') as f:
		x = 's' if x=='e' else 'e'
		f.write(x)
