def my_long_word(number, text):
    words = text.split()
    result = ""

    for word in words:
        word_length = 0
        for char in word:
            if char.isalpha():  # Vérifie si le caractère est une lettre
                word_length += 1
        
        if word_length > number:
            result += word + " "

    return result.strip()  # Supprime l'espace à la fin s'il y en a un

# Exemple d'utilisation
output = my_long_word(3, "La peur est le chemin vers le côté obscur, la peur mène à la colère, la colère mène à la haine, la haine mène à la souffrance")
print("Output:", output)