# Operator Aritmatika 
a = 10
b = 3

# Penjumlahan
hasil_tambah = a + b
print("Penjumlahan:", hasil_tambah)

# Pengurangan
hasil_kurang = a - b
print("Pengurangan:", hasil_kurang)

# Perkalian
hasil_kali = a * b
print("Perkalian:", hasil_kali)

# Pembagian
hasil_bagi = a / b
print("Pembagian:", hasil_bagi)

# Pembagian bulat
hasil_bagi_bulat = a // b
print("Pembagian Bulat:", hasil_bagi_bulat)

# Sisa bagi (modulus)
hasil_modulus = a % b
print("Sisa Bagi (Modulus):", hasil_modulus)

# Pangkat
hasil_pangkat = a ** b
print("Pangkat:", hasil_pangkat)


# Operator Perbandingan
x = 7
y = 5

print("Nilai x:", x)
print("Nilai y:", y)

# Sama dengan
print("x == y:", x == y)

# Tidak sama dengan
print("x != y:", x != y)

# Lebih besar dari
print("x > y:", x > y)

# Lebih kecil dari
print("x < y:", x < y)

# Lebih besar atau sama dengan
print("x >= y:", x >= y)

# Lebih kecil atau sama dengan
print("x <= y:", x <= y)


# Operator Penugasan

a = 10
print("Nilai awal a:", a)

# Penugasan dengan penjumlahan
a += 5  # sama dengan a = a + 5
print("Setelah a += 5:", a)

# Penugasan dengan pengurangan
a -= 3  # sama dengan a = a - 3
print("Setelah a -= 3:", a)

# Penugasan dengan perkalian
a *= 2  # sama dengan a = a * 2
print("Setelah a *= 2:", a)

# Penugasan dengan pembagian
a /= 4  # sama dengan a = a / 4
print("Setelah a /= 4:", a)

# Penugasan dengan modulus
a %= 3  # sama dengan a = a % 3
print("Setelah a %= 3:", a)

# Penugasan dengan pangkat
a **= 2  # sama dengan a = a ** 2
print("Setelah a **= 2:", a)

# Penugasan dengan pembagian bulat
a //= 2  # sama dengan a = a // 2
print("Setelah a //= 2:", a)


# Operator Logika 

a = True
b = False

print("Nilai a:", a)
print("Nilai b:", b)

# AND: True kalau kedua kondisi True
print("a and b:", a and b)

# OR: True kalau salah satu kondisi True
print("a or b:", a or b)

# NOT: Membalik nilai
print("not a:", not a)
print("not b:", not b)

# Contoh logika dengan perbandingan
x = 10
y = 5

print("\nContoh logika dengan angka:")
print("(x > 5) and (y < 10):", (x > 5) and (y < 10))
print("(x < 5) or (y < 3):", (x < 5) or (y < 3))
print("not (x == 10):", not (x == 10))


# Bitwise 

a = 5     # biner: 0101
b = 3     # biner: 0011

print("a =", a)
print("b =", b)

# AND: dua-duanya harus 1
print("a & b =", a & b)   # 0101 & 0011 = 0001 → hasil: 1

# OR: salah satu aja cukup
print("a | b =", a | b)   # 0101 | 0011 = 0111 → hasil: 7

# XOR: beda = 1, sama = 0
print("a ^ b =", a ^ b)   # 0101 ^ 0011 = 0110 → hasil: 6

# NOT: dibalik semua bit-nya (ingat, hasilnya bisa negatif)
print("~a =", ~a)         # ~0101 = -(0101 + 1) = -6

# Geser ke kiri (dikalikan 2)
print("a << 1 =", a << 1) # 0101 jadi 1010 → hasil: 10

# Geser ke kanan (dibagi 2)
print("a >> 1 =", a >> 1) # 0101 jadi 0010 → hasil: 2


# Cek keanggotaan

buah = ["apel", "jeruk", "mangga"]

# Apakah "apel" ada di dalam list?
if "apel" in buah:
    print("Apel ada di daftar buah.")

# Apakah "pisang" tidak ada di dalam list?
if "pisang" not in buah:
    print("Pisang nggak ada di daftar buah.")

# Cek di string
kalimat = "Belajar Python itu asik."

if "Python" in kalimat:
    print("Kalimat ini ngomongin Python.")

if "Java" not in kalimat:
    print("Kalimat ini nggak nyebut Java.")


    # Operator Identitas 

a = [1, 2, 3]
b = a  # b merujuk ke objek yang sama dengan a
c = [1, 2, 3]  # c adalah objek baru yang berisi nilai yang sama dengan a

print("a is b:", a is b)  # Mengecek apakah a dan b merujuk ke objek yang sama
print("a is c:", a is c)  # Mengecek apakah a dan c merujuk ke objek yang sama

print("a is not b:", a is not b)  # Mengecek apakah a dan b tidak merujuk ke objek yang sama
print("a is not c:", a is not c)  # Mengecek apakah a dan c tidak merujuk ke objek yang sama
