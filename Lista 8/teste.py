# import math

# def is_positive(num):
#     return num >= 0


# def sanitized_sqrt(numbers):
#     cleaned_iter = map(math.sqrt, filter(is_positive, numbers))
#     return list(cleaned_iter)


# print(sanitized_sqrt([25, 9, 81, -16, 0]))

def mapear(x):
    if x.isdigit() == False:
        return x 
        
def is_null(str):
    if str.isdigit() == False:
        return True
    else:
        return False

def cod_run_lenght(string):
	if type(string) == str:
	    resultado = map(mapear,filter(is_null,string))
	    resultado = list(resultado)
		return cod_run_lenght([resultado,[]])

	x = string[0]
	index = string[1]

	if len(x) != 0:
		letra = x[0]
		if index == []:
			index.append(letra)
			index.append(0)
		if index[-2] == letra:
			index[-1] = index[-1]+1
		if index[-2] != letra:
			index.append(letra)
			index.append(1)
		x.pop(0)
		return teste([x,index])
	else:
		return index
		
print(f'Decodificada = {cod_run_lenght("AAAAAABBAAACCAABVBB")}')
