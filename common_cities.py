a = ["İzmir","Ankara","Muğla","Aydın"]
city_a = set(a)

b = ["Bursa","Ankara","Muğla","İstanbul"]
city_b = set(b)

common_city = sorted(city_a & city_b)

print(f"A turizm firmasında; {a} şehirlerine seferler bulunur iken,\nB turizm firmasında; {b} şehirlerine seferler bulunmaktadır.\nİki firmada da ortak seferlerin bulunduğu şehirler alfabetik sırayla şunlardır: {common_city}")