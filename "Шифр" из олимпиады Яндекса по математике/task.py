message = "ФЗНУЗХ"
alphabet = [chr(ord("А") + i) for i in range(32)]
alphabet.insert(6, "Ё")

# минус (макс на 8)
for key in range(0, 9):
    for char in message:
        print(alphabet[ord(char) - key - 1039], end='')
    print()

print()

# плюс (макс на 10)
for key in range(1, 11):
    for char in message:
        print(alphabet[ord(char) + key - 1039], end='')
    print()

# Ищем среди получившегося адекватное слово.
