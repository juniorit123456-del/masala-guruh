kunlar = ["1-kun", "2-kun", "3-kun", "4-kun", "5-kun", "6-kun", "7-kun"]
xarajatlar = []

for kun in kunlar:
    xarajat = float(input(f"{kun} qancha pul sarfladingiz? "))
    xarajatlar.append(xarajat)

umumiy_xarajat = sum(xarajatlar)
eng_kop = max(xarajatlar)
eng_kam = min(xarajatlar)

eng_kop_kun = kunlar[xarajatlar.index(eng_kop)]
eng_kam_kun = kunlar[xarajatlar.index(eng_kam)]

ortacha = umumiy_xarajat / len(xarajatlar)
byudjet = float(input("Byudjet: "))
qolgan = byudjet - umumiy_xarajat

print("\nXarajatlar:", xarajatlar)
print("Umumiy:", umumiy_xarajat)
print("Eng ko'p:", eng_kop_kun, eng_kop)
print("Eng kam:", eng_kam_kun, eng_kam)
print("O'rtacha:", ortacha)
print("Qoldi:", qolgan)

if umumiy_xarajat > byudjet:
    print("Ogohlantirish: byudjetdan oshdingiz!")
else:
    print("Byudjetdan oshmadingiz.")
