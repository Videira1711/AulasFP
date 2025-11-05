ATP1  = float(input( "Nota da ATP1?"))
ATP2  = float(input( "Nota da ATP2?"))
API = float(input( "Nota da API"))
APF = float(input( "Nota da APF?"))
CTP = (15% ATP1 + 15% ATP2) / 30
if CTP < 6.5:
	print("Reprovado por nota mínima")
if API > APF :
	CP = (20% API + 50% APF) / 70
else: CP = APF

if CP == APF or API <= APF:
	NF = 30% CTP + 70% CP
else: print("Reprovado por nota mínima")
print ,NF