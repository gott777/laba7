sentence = input("Введите строку: ")
vowels = "aeiou"
consonants = "bcdfghjklmnpqrstvwxyz"
vowel_count = sum(1 for char in sentence if char.lower() in vowels)
consonant_count = sum(1 for char in sentence if char.lower() in consonants)
print("Количество гласных:", vowel_count)
print("Количество согласных:", consonant_count)