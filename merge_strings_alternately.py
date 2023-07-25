word1 = 'omar'
word2 = 'na'



class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res_list = list()
		#case 1 - same lenght 
        if len(word1) == len(word2):
            for i in range(len(word1)):
                var = word1[i] + word2[i]
                res_list.append(var)

            for letters in res_list:
                print(str(letters), end='')
		#case 2 - one word is longer
        elif len(word2) > len(word1):
            for i in range(len(word1)):
                var = word1[i] + word2[i]
                res_list.append(var)

            res_list.append(word2[len(word1)::])

            for i in res_list:
                print(str(i), end='')
                
                
		#case 3 - the other one is longer
        else:
            for i in range(len(word2)):
                var = word1[i] + word2[i]
                res_list.append(var)

            res_list.append(word1[len(word2)::])

            for i in res_list:
                print(str(i), end='')
            
        
        result = ''.join(res_list)
        return result
	