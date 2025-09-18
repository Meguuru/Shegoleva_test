n= 3
with open('text1.txt', 'r', encoding='utf-8') as f_in:
    text = f_in.read()
    encrypted = ''

    for char in text:
        if 'a' <= char <= 'z':
            encrypted += chr((ord(char) - ord('a') + n) % 26 + ord('a'))
        elif 'A' <= char <= 'Z':
            encrypted += chr((ord(char) - ord('A') + n) % 26 + ord('A'))
        else:
            encrypted += char

with open('cipher_text.txt', 'w', encoding='utf-8') as f_out:
    f_out.write(encrypted)

print("Файл зашифрован!")