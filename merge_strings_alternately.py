word1 = 'omar'
word2 = 'na'
res = 'onmaar'


res_list = list()
if len(word1) == len(word2):
	for i in range(len(word1)):
		var = word1[i] + word2[i]
		res_list.append(var)


	for letters in res_list:
		print(str(letters), end='')

elif len(word2) > len(word1):
	for i in range(len(word1)):
		var = word1[i] + word2[i]
		res_list.append(var)

	res_list.append(word2[len(word1)::])

	for i in res_list:
		print(str(i), end='')
		
		

else:
	for i in range(len(word2)):
		var = word1[i] + word2[i]
		res_list.append(var)

	res_list.append(word1[len(word2)::])

	for i in res_list:
		print(str(i), end='')
	