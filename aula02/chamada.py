x1 = float(input("Quanto tempo foi a chamada(em segundos)? "))

if x1 > 60:
	x2 = x1 - 60

x3 = x2 * 0.002

print("O valor total da chamada são: ", 0.12 + x3, "€")
