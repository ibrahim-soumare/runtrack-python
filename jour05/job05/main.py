def chiffrement_cesar(message, decalage):
    resultat = ""
    for caractere in message:
        if caractere.isalpha():
           
            if caractere.isupper():
                resultat += chr((ord(caractere) - ord('A' ) + decalage) % 26 + ord('A'))
          
            else:
                resultat += chr((ord(caractere) - ord('a' ) + decalage) % 26 + ord('a'))
        else:
           
            resultat += caractere
    return resultat


message_original = "Bonjour, Cesar!"
decalage = 3
message_chiffre = chiffrement_cesar(message_original, decalage)

print(f"Message original : {message_original}")
print(f"Message chiffré : {message_chiffre}")