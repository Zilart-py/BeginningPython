'''
Let us now write a code for Caesar Cipher.
Read more about Ceaser Cipher here:
http://practicalcryptography.com/ciphers/caesar-cipher/
It is basically a substitution cipher, which each letter gets substituted by
another letter as specified by the key.
Eg: 'ABC' is my message, and key = 1
Then it'll become 'BCD' as
'A' will be substituted by 'B'
'B' will be substituted by 'C'
'C' will be substituted by 'D'
See the image "CaesarCipher1.jpg" to understand
'''

MAX_KEY_SIZE = 26  # MAX_KEY_SIZE is a constant that stores the integer 26 in it.


# MAX_KEY_SIZE reminds us that in this program, the key used in the cipher should be between 1 and 26


def getMode():
    while True:
        print("Do you wish to Encrypt(e) or Decrypt(d) the message? ")
        mode = input().lower()
        if mode in 'encrypt e decrypt d'.split():
            return mode
        else:
            print("Enter either 'encrypt' or 'e' or 'decrypt' or 'd' ")


'''
The getMode() function will let the user type in if they want encryption or decryption mode for the program.
The value returned from input() and lower() is stored in mode. 
The if statement’s condition checks if the string stored in mode exists in the list 
returned by 'encrypt e decrypt d'.split().

This list is ['encrypt', 'e', 'decrypt', 'd'], but it is easier for the programmer 
to type 'encrypt e decrypt d'.split() and not type in all those quotes and commas. 
Use whichever is easiest for you; they both evaluate to the same list value.

This function will return the first character in mode 
as long as mode is equal to 'encrypt', 'e', 'decrypt', or 'd'. 
Therefore, getMode() will return the string 'e' or the string 'd' 
(but the user can type in either “e”, “encrypt”, “d”, or “decrypt”.)
'''


def getMessage():
    print("Enter the message: ")
    return str(input())


'''
The getMessage() function simply gets the message to encrypt or decrypt from the user and returns it.
'''


def getKey():
    key = 0
    while True:
        print("Enter Key by which you want to Encrypt or Decrypt (1 - %s): " % (MAX_KEY_SIZE))
        key = int(input())
        if (key >= 1 and key <= MAX_KEY_SIZE):
            return key


'''
The getKey() function lets the player type in the key they will use to encrypt or decrypt the message. 
The while loop ensures that the function keeps looping until the user enters a valid key.

A valid key here is one that is between the integer values 1 and 26 
(remember that MAX_KEY_SIZE will only ever have the value 26 because it is constant). 
It then returns this key. 
Line 61 (int(input) line) sets key to the integer version of what the user typed in, 
so getKey() returns an integer.
'''


def translatedText(mode, message, key):
    if mode[0] == 'd':
        key = -key
    translated = ""

    '''
    getTranslatedMessage() does the encrypting and decrypting. It has three parameters:
    · mode sets the function to encryption mode or decryption mode.
    · message is the plaintext (or ciphertext) to be encrypted (or decrypted).
    · key is the key that is used in this cipher.
    Line "if mode[0] == 'd':" checks if the first letter in the mode variable is the string 'd'. 
    If so, then the program is in decryption mode. 
    The only difference between the decryption and encryption mode 
    is that in decryption mode the key is set to the negative version of itself. 
    If key was the integer 22, then in decryption mode set it to -22. 
    The reason why will be explained later. 
    translated is the string of the result: either the ciphertext (if you are encrypting) 
    or the plaintext (if you are decrypting). 
    It starts as the blank string and has encrypted or decrypted characters 
    concatenated to the end of it.
    '''

    for symbol in message:
        if symbol.isalpha():
            num = ord(symbol)
            num += key

            '''
            The isalpha() string method will return True if the string is an uppercase or lowercase letter from A to Z. 
            If the string contains any non-letter characters, then isalpha() will return False.
            '''

            if symbol.isupper():  # works in the same way as "isalpha()"
                if (num > ord('Z')):
                    num -= 26
                elif (num < ord('A')):
                    num += 26
            elif symbol.islower():
                if (num > ord('z')):
                    num -= 26
                elif (num < ord('a')):
                    num += 26

                    '''
                    Line "symbol.isupper():" checks if the symbol is an uppercase letter. 
                    If so, there are two special cases to worry about. 
                    What if symbol was 'Z' and key was 4? If that were the case, 
                    the value of num here would be the character '^' (The ordinal of '^' is 94). 
                    But ^ isn’t a letter at all. You want the ciphertext to “wrap around” to the beginning of the alphabet.
                    Check if num has a value larger than the ordinal value for “Z”. 
                    If so, then subtract 26 (because there are 26 letters in total) from num. 
                    After doing this, the value of num is 68. 68 is the correct ordinal value for 'D'
                    
                    If the symbol is a lowercase letter, 
                    the program runs code that is similar to lines 111 through 114. 
                    The only difference is that it uses ord('z') and ord('a') instead of ord('Z') 
                    and ord('A').
                    In decrypting mode, then key would be negative. 
                    The special case would be where num -= 26 is less than the ASCII value for “a”. 
                    In that case, add 26 to num to have it “wrap around” to the end of the alphabet.
                    
                    '''

            translated += chr(num)  # concatenates the encrypted/decrypted character to the translated string.
        else:
            translated += symbol  # If the symbol was not an uppercase or lowercase letter, then this line concatenates the original symbol to the translated string. Therefore, spaces, numbers, punctuation marks, and other characters won’t be encrypted or decrypted.
    return translated  # returns translated message


mode = getMode()
message = getMessage()
key = getKey()

if mode == 'encrypt' or mode == 'e':
    print("Your Encrypted message by key {:d} is: ".format(key))
    print(translatedText(mode, message, key))
else:
    print("Your Decrypted message by key {:d} is: ".format(key))
    print(translatedText(mode, message, key))
