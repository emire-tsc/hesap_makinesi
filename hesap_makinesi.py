import math

def toplama(x, y):
    return x + y

def cikarma(x, y):
    return x - y

def carpma(x, y):
    return x * y

def bolme(x, y):
    if y != 0:
        return x / y
    else:
        return "Bölme işlemi tanimsiz (0'a bölme hatasi)"


while True:
    print("\nYapmak istediğiniz işlemi seçin:")
    print("-" * 40)
    print("1. Toplama")
    print("2. Cİkarma")
    print("3. Carpma")
    print("4. Bölme")
    print("5. Cikis")
    print("-" * 40)

    secim = input("Seciminizi yapin (1-5): ")

    if secim =='5':
        print("proramdan cikiliyor...")
        break

    if secim in ('1', '2', '3', '4', '5'):
        sayi1 = float(input("Birinci sayiyi girin: "))
        if secim != '5':
            sayi2 = float(input("İkinci sayiyi girin: "))
    print("-" * 40)


    if secim == '1':
        print(f"{sayi1} + {sayi2} = {toplama(sayi1, sayi2)}")
    elif secim == '2':
        print(f"{sayi1} - {sayi2} = {cikarma(sayi1, sayi2)}")
    elif secim == '3':
        print(f"{sayi1} * {sayi2} = {carpma(sayi1, sayi2)}")
    elif secim == '4':
        print(f"{sayi1} / {sayi2} = {bolme(sayi1, sayi2)}")
    else:
        print("Geçersiz bir seçim yaptiniz. Lütfen 1, 2, 3, 4, veya 5 sayilarini  girin!!")