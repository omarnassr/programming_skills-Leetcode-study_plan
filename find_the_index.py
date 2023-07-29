needle = 'omar'
haystack = 'hebaomar'

def foo(string1 , string2):

    if string1 in string2:
        index =  string2.find(string1)
        result = index
    else:
        return -1
    
    return result

test =foo(needle, haystack)
print(test)

