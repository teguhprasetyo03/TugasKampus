list=["a", "r","t","u","n"]

print("Tampilkan elemen ke3: ",list[2])
print("Ambil elemen ke2 sampai ke4: ", list[1:4])
print("Ambil elemen terakhir: ", list[-1])

# Merubah elemen ke4 dengan nilai lain 
list[3] = "f"
print("Meruubah elemen ke 4 dengan nilai lain: ", list)

# Merubah elemen ke4 sampai terakhir
list[3:] = "s","d"
print("Merubah elemen ke4 sampai terakhir: ", list)





# Tambah elemen list
a =[1,2,3,4,5]
b =[6,7,8,9,10]

# Ambil 2 buah bagian list A ke ist B
b.append(a[1:3])
print("2 bagian dari list A dijadikan list B: ", b)

# Tambah list B dengan nilai string
b.append("arjun")
print("Tambah list B dengan string: ",b)

# Tambah list B dengan 3 nilai
print("Tambah list B dengan 3 nilai: ", b+[11,12,13])

# Menggabungkan list B dengan list A
c=b+a
print("Gabungan dari list B dan list A: ", c)