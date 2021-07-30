def raiz_quad(n,estimativa=1):
	if abs(estimativa**2 - n)<= (10**-12):
		return estimativa
	else:
		estimativa2 = (estimativa + (n/estimativa))/2
		return raiz_quad(n,estimativa2)

print(raiz_quad(64))