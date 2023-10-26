def encrypt_rail_fence(text, key):
    # Membuat matriks kosong dengan jumlah baris sesuai dengan kunci
    rail = ['' for _ in range(key)]

    # Inisialisasi indeks baris dan arah
    row, down = 0, True

    # Mengisi matriks dengan karakter dari pesan
    for char in text:
        rail[row] += char
        if down:
            row += 1
            if row == key - 1:
                down = False
        else:
            row -= 1
            if row == 0:
                down = True

    # Menggabungkan baris-baris matriks untuk mendapatkan teks terenkripsi
    encrypted_text = ''.join(rail)

    return encrypted_text


def decrypt_rail_fence(ciphertext, key):
    # Membuat matriks kosong dengan ukuran yang sama dengan pesan terenkripsi
    rail = ['' for _ in range(len(ciphertext))]

    # Menghitung panjang dari setiap baris Rail Fence
    row_lengths = [0] * key
    row, down = 0, True
    for i in range(len(ciphertext)):
        row_lengths[row] += 1
        if down:
            row += 1
            if row == key - 1:
                down = False
        else:
            row -= 1
            if row == 0:
                down = True

    # Mengisi matriks Rail Fence dengan karakter dari pesan terenkripsi
    index = 0
    for r in range(key):
        for i in range(row_lengths[r]):
            rail[r] += ciphertext[index]
            index += 1

    # Mendekripsi pesan dengan membaca baris-baris matriks
    row, down = 0, True
    decrypted_text = ''
    for i in range(len(ciphertext)):
        decrypted_text += rail[row][0]
        rail[row] = rail[row][1:]
        if down:
            row += 1
            if row == key - 1:
                down = False
        else:
            row -= 1
            if row == 0:
                down = True

    return decrypted_text


# Contoh penggunaan
plaintext = "Ardafa"
key = 3
encrypted_text = encrypt_rail_fence(plaintext, key)
decrypted_text = decrypt_rail_fence(encrypted_text, key)

print("Pesan Asli:", plaintext)
print("Pesan Terenkripsi:", encrypted_text)
print("Pesan Terdekripsi:", decrypted_text)
