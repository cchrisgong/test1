'''
This script allows one to scramble some text and gives out a key
'''
def scramble(str_string):
	string_list = str_string.split()

	num = 0
	string_list_total = []
	for s in string_list:
		string_list2 = list(s)
		for s2 in string_list2:
			num += 1
			string_list_total.append((s2, num))
	
	string_list_total.sort()
	key = [y for (x,y) in string_list_total]
	scrambled_list = [x for (x,y) in string_list_total]
	scrambled_string = ''.join(scrambled_list)
	return scrambled_string, key
	
if __name__ == "__main__":
	str_string = "Mit Thermomix kann mann wirklich alles zubereiten!"
	scrambled_string, key = scramble(str_string)
	print (scrambled_string)
