import sys

def encrypt(message, k):
    #Empty string to be used later to store encrypted characters
    EncryptedMessage = ""
    
    #for loop to iterate through every letter in the message
    for Character in message:

        #Checking if the letter is uppercase
        if Character.isupper():

            #Setting the value of A to keep track of the starting point for the uppercase Alphabet
            UpperAlphaStart = ord("A")

            #Getting the position of the character, capital A is the starting point(0)
            Position = ord(Character) - UpperAlphaStart

            #Adding k to the Position to get the value after the caesar cipher k value is applied
            #Modding by 26 to keep the results within the range of 0 to 25 for the 26 letters of the alphabet
            Numeric = (Position + k) % 26

            #using chr to convert the numeric back to a character
            EncryptedCharacter = chr(Numeric + ord("A"))

        #if the letter is lowercase
        else:

            #Setting the value of a to keep track of the starting point for the lowercase Alphabet
            LowerAlphaStart = ord("a")

            #Getting the position of the character, lowercase a is the starting point(0)
            Position = ord(Character) - LowerAlphaStart

            #Adding k to the Position to get the value after the caesar cipher k value is applied
            #Modding by 26 to keep the results within the range of 0 to 25 for the 26 letters of the alphabet
            Numeric = (Position + k) % 26

            #using chr to convert the numeric back to a character
            EncryptedCharacter = chr(Numeric + ord("a"))

        EncryptedMessage = EncryptedMessage + EncryptedCharacter

    return EncryptedMessage


def decrypt(message, k):

   #Empty string to be used later to store decrypted characters
    DecryptedMessage = ""
    
    #for loop to iterate through every letter in the message
    for Character in encrypted:
            
        #Checking if the letter is uppercase
        if Character.isupper():

            #Setting the value of A to keep track of the starting point for the uppercase Alphabet
            DeUpperAlphaStart = ord("A")

            #Getting the position of the character, capital A is the starting point(0)
            DePosition = ord(Character) - DeUpperAlphaStart

            #Modding by 26 to keep the results within the range of 0 to 25 for the 26 letters of the alphabet
            #Subtracting k instead of adding it in order to get back to the original message(decrypt the message)
            DeNumeric = (DePosition - k) % 26

            #using chr to convert the numeric back to a character
            DecryptedCharacter = chr(DeNumeric + ord("A"))

        
        #if the letter is lowercase
        else:

            #Setting the value of a to keep track of the starting point for the lowercase Alphabet
            DeLowerAlphaStart = ord("a")

            #Getting the position of the character, lowercase a is the starting point(0)
            DePosition = ord(Character) - DeLowerAlphaStart

            #Modding by 26 to keep the results within the range of 0 to 25 for the 26 letters of the alphabet
            #Subtracting k instead of adding it in order to get back to the original message(decrypt the message)
            DeNumeric = (DePosition - k) % 26

            #using chr to convert the numeric back to a character
            DecryptedCharacter = chr(DeNumeric + ord("a"))

        
        DecryptedMessage = DecryptedMessage + DecryptedCharacter

    return DecryptedMessage


if __name__ == "__main__":
    # take in first arg as word
    message = sys.argv[1]
    # take in second arg as int key
    key = int(sys.argv[2])

    # encrypt your word
    encrypted = encrypt(message, key)

    # decrypt your encrypted word
    decrypted = decrypt(encrypted, key)

    print("Your encrypted word is", encrypted)
    print("Your decrypted word is", decrypted)
