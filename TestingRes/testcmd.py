
def main(lib):
	print("Hello world")
	print('imp cmd works fine')
	x = input('9 plus 10 equals? ')
	if int(x) != 21:
		print("9 plus 10 is 21 you stupid fool you played yourself!")
	else:
		print("That's correct!")
	lib.display_all_lib()
