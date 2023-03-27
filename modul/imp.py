import rumus

print("---WELCOME---")
print("Pilih Opsi: ")
print("1. Menghitung Luas 2 Dimensi")
print("2. Menghitung Volume 3 Dimensi")

opt = input("1 atau 2 : ")

#opsi 2 dimensi
if opt == "1":
    print("--2 Dimensi--")
    print("1. persegi")
    print("2. persegi panjang")
    print("3. segitiga")
    print("4. lingkaran")
    print("5. jajar genjang")
    print("6. trapesium")
    
    dua_dimensi=input("pilih bangun datar : ") #input opsi 2 dimensi
    
    if dua_dimensi=="1":
        pjgsisi=int(input("masukkan panjang sisi : "))
        print(rumus.persegi(pjgsisi)) #import peregi
        
    elif dua_dimensi=="2":
        pjg=int(input("masukkan panjangnya : "))
        lbr=int(input("masukkan lebarnya : "))
        print(rumus.p_panjang(pjg,lbr)) #import peregi panjang
   
    elif dua_dimensi=="3":
        als=int(input("masukkan alasnya : "))
        tg=int(input("masukkan tinggi : "))
        print(rumus.segitiga(als,tg)) #import segitiga
        
    elif dua_dimensi=="4":
        rad=int(input("masukkan jari-jarinya : "))
        print(rumus.slingkaran(rad)) #import lingkaran
        
    elif dua_dimensi=="5":
        alsjg=int(input("masukkan alasnya : "))
        tgjg=int(input("masukkan tinggi : "))
        print(rumus.jajargenjang(alsjg,tgjg)) #import jajar genjang
        
    elif dua_dimensi=="6":
        ats=int(input("masukkan sisi atasnya : "))
        bwh=int(input("masukkan sisi bawahnya : "))
        tgt=int(input("masukkan tinggi : "))
        print(rumus.trapesium(ats,bwh,tgt)) #import trapesium

    else: print("maaf pilihan tidak terdefinisi")
    
#opsi 3 dimensi
elif opt == "2":
    print("--3 Dimensi--")
    print("1. Kubus")
    print("2. Balok")
    print("3. Tabung")
    print("4. Kerucut")
    print("5. Limas")
    print("6. Prisma")

    tiga_dimensi=input("pilih bangun ruang : ") #input opsi 3 dimensi
    
    if tiga_dimensi=="1":
        sisi=int(input("masukkan panjang sisi : "))
        print(rumus.kubus(sisi)) #import kubus
        
    elif tiga_dimensi=="2":
        pjgblk=int(input("masukkan panjangnya : "))
        lbrblk=int(input("masukkan lebarnya : "))
        print(rumus.balok(pjgblk,lbrblk)) #import balok
        
    elif tiga_dimensi=="3":
        radt=int(input("masukkan jari-jarinya : "))
        tgtab=int(input("masukkan tingginya : "))
        print(rumus.tabung(radt,tgtab)) #import tabung
        
    elif tiga_dimensi=="4":
        radk=int(input("masukkan jari-jarinya : "))
        tgk=int(input("masukkan tingginya : "))
        print(rumus.kerucut(radk,tgk)) #import kerucut
        
    elif tiga_dimensi=="5":
        lalas=int(input("masukkan luas alas : "))
        tgli=int(input("masukkan tinggi : "))
        print(rumus.limas(lalas,tgli)) #import limas
        
    elif tiga_dimensi=="6":
        luasalas=int(input("masukkan luas alas : "))
        tgp=int(input("masukkan tinggi : "))
        print(rumus.prisma(luasalas,tgp)) #import prisma
    
    else: print("maaf pilihan tidak terdefinisi")
    
else: print("pilihan tidak ada")
        
        
    