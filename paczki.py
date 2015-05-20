import operator

zczytanie1=input()
zczytanie2=input()
imiona=zczytanie1.split()
kolejnosc=zczytanie2.split()

d=dict()

for i in range(len(imiona)):
	d[imiona[i]]=dict()
	liczba=0

for j in range(len(kolejnosc)):
	if imiona[i]==kolejnosc[j]:
		liczba+=1
		d[imiona[i]]=liczba
wynik = sorted(d.items(), key = operator.itemgetter(1), reverse=True)
print(wynik)
print("Witam")

