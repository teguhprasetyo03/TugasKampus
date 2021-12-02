i =  0 
nama = []
nim =[]
tugas=[]
uts=[]
uas=[]
nilaiakhir=[]

while True:
    nama1=input("Nama  : m. irvan zaeni ")
    nama.append(nama1)
    nim1=input("NIM   : 312110024 ")
    nim.append(nim1)
    tugas1=input("Nilai Tugas :  85")
    tugas.append(tugas1)
    uts1=input("Nilai UTS : 70 ")
    uts.append(uts1)
    uas1=input("Nilai UAS : 78 ")
    uas.append(uas1)

    nilaiakhir1=(int(tugas1)*0.30)+(int(uts1)*0.35)+(int(uas1)*0.35)
    nilaiakhir.append(nilaiakhir1)

    more=""
    while more!="y" and more!="t":
        more=input("Tambah Data(y/t) ?")
    i+=1
    if more=="t":
        break
print("._____________________________________________________________________________________________________________.")
print("|                                             Daftar Mahasiswa                                                |")
print("|_____________________________________________________________________________________________________________|")
print("|  No.  |      Nama      |      NIM        |     Tugas      |      UTS      |      UAS      |      Akhir      |")
print("|-------------------------------------------------------------------------------------------------------------|")
for n in range(i):
    print("| ",n+1,"   |  ",nama[n],"  |  ",nim[n],"    |      ",tugas[n],"      |      ",uts[n],"     |     ",uas[n],"      |    ",nilaiakhir[n],"      |")
    print("|-------------------------------------------------------------------------------------------------------------|")