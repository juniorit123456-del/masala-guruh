matn = input("Matn kiriting: ")
qidiriladigan_soz = input("Qidiriladigan so'zni kiriting: ")

tinish_belgilari = ".,!?;:()[]{}\"'“”‘’"
sozlar = [
	soz.strip(tinish_belgilari)
	for soz in matn.split()
	if soz.strip(tinish_belgilari)
]

unlilar = "A,O,U,I,O',E"
unlilar_soni = sum(harf.casefold() in unlilar for harf in matn)

if sozlar:
	eng_uzun_soz = max(sozlar, key=len)
	print("So'zlar soni:", len(sozlar))
	print("Eng uzun so'z:", eng_uzun_soz)
	print("Unli harflar soni:", unlilar_soni)
	print("So'zlarning teskari tartibi:", " ".join(sozlar[::-1]))

	qidiriladigan_soz = qidiriladigan_soz.strip(tinish_belgilari).casefold()
	qatnashish_soni = sum(soz.casefold() == qidiriladigan_soz for soz in sozlar)
	print("Qidirilgan so'z qatnashgan soni:", qatnashish_soni)
else:
	print("Matnda so'z topilmad.")
