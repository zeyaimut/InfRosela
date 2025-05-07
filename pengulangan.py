#while loop
limit = int(input("Masukkan angka batas hitungan: "))

count = 0
while count <= limit:
    print("The count is:", count)
    count += 1

print("Good bye!")

#for loop
# Contoh pengulangan for dengan list nama
nama = ["ros", "sel", "laa"]
for n in nama:
    print("Halo,", n)

# Contoh pengulangan for dengan list minuman
minuman = ["teh", "kopi", "susu"]
for m in minuman:
    print("Saya suka minum", m)

# Contoh pengulangan for dengan range angka kelipatan 3
for i in range(3, 16, 3):
    print(i)

#nested loop
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=' ')
    print()