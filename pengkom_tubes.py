gol1 = [[0,9500,29500,8500,56500,66500],[9500,0,20000,18000,47500,57000],[29500,20000,0,38000,27000,37000],[8500,18000,38000,0,65000,75000],[56500,47500,27000,65000,0,9500],[66500,57000,37000,75000,9500,0]]
gol2 = [[0,14000,44500,13000,85000,99500],[14000,0,30500,26500,71000,85500],[44500,30500,0,57000,41000,55500],[13000,26500,57000,0,98000,112500],[85000,71000,41000,98000,0,14500],[99500,85500,55500,112500,14500,0]]
gol3 = [[0,14000,44500,13000,85000,99500],[14000,0,30500,26500,71000,85500],[44500,30500,0,57000,41000,55500],[13000,26500,57000,0,98000,112500],[85000,71000,41000,98000,0,14500],[99500,85500,55500,112500,14500,0]]
gol4 = [[0,18500,59000,17000,113500,133000],[18500,0,40500,35500,95000,114500],[59000,40500,0,76000,54500,74000],[17000,35500,76000,0,130500,150000],[113500,95000,54500,130500,0,19500],[133000,114500,74000,150000,19500,0]]
gol5 = [[0,18500,59000,17000,113500,133000],[18500,0,40500,35500,95000,114500],[59000,40500,0,76000,54500,74000],[17000,35500,76000,0,130500,150000],[113500,95000,54500,130500,0,19500],[133000,114500,74000,150000,19500,0]]
print("")
gol=int(input("Masukkan golongan: "))
if(1<=gol<=5):
    print(f"Kode Kota Ungaran = 1 \nKode Kota Bawen = 2 \nKode Kota Salatiga = 3 \nKode Kota Banyumanik = 4 \nKode Kota Boyolali = 5 \nKode Kota Kartasura = 6 \n")
    awal=int(input("Masukkan kode kota masuk: "))
    if(1<=awal<=6):
        akhir = int(input("Masukkan kode kota keluar"))
        if(1<=akhir<=6):
            saldo=int(input("Masukkan saldo: "))
            if(gol==1):
                harga = gol1[awal-1][akhir-1]
            elif(gol==2):
                harga = gol2[awal-1][akhir-1]
            elif(gol==3):
                harga = gol3[awal-1][akhir-1]
            elif(gol==4):
                harga = gol4[awal-1][akhir-1]
            elif(gol==5):
                harga = gol5[awal-1][akhir-1]
            while(saldo<harga):
                print("Saldo anda tidak mencukupi, silahkan topup.")
                saldo+=int(input("Nominal top up anda "))
            print(f"Sisa saldo anda = {saldo-harga}")

            print