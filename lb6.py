word = input("Введите строку: ").replace(" ", "").lower()
if word == word[::-1]:
    print("Это палиндром")
else:
    print("Это не палиндром")