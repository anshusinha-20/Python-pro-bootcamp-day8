# def greet():
#     print("hello");
#     print("world");
#     print("it's me");

# greet()

# def greet(name):
#     print("hello");
#     print("world");
#     print(f"it's {name}");

# name = input("Enter your name: ")
# greet(name)

# def positionalKeyWord(a, b ,c):
#     print(f"Do this with {a}")
#     print(f"Do this with {b}")
#     print(f"Do this with {c}")

# positionalKeyWord(a = 1, b = 2, c = 3)

#####

# Day 8 Project: Caesar Cipher

import cc

logo = cc.logo

print(logo)

alphabet = [chr(i) for i in range(97, 123)]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = [' ', "!", "@", "#", "$", "&", "?"]
allCharacters = alphabet + numbers + symbols

def casesarCipher(command, message, shift):
    encodedMessage = []
    decodedMessage = []

    if (command == "e"):
        for i in message:
            index1 = allCharacters.index(i)
            index2 = index1 + shift
            if (index2 > 42):
                index3 = index2 - 42
                encodedMessage.append(allCharacters[index3 - 1])
            elif (index2 <= 42):
                encodedMessage.append(allCharacters[index2])
        print(f"Here's the encoded result: {''.join(i for i in encodedMessage)}")

    elif (command == "d"):
        for i in message:
            index1 = allCharacters.index(i)
            index2 = index1 - shift
            decodedMessage.append(allCharacters[index2])
        print(f"Here's the decoded result: {''.join(i for i in decodedMessage)}")

runGame = True
while (runGame):
    command = input("Type 'e' for 'encode' of 'd' for 'decode': ").lower()
    message = input("Type your message(make sure to add only these symbols:space, !, @, #, $, &, ?): ")
    shift = int(input("Type the shift number(0-42): "))

    casesarCipher(command, message, shift)

    goAgain = input("Type 'y' for 'yes' if you want to go again, else type 'n' for 'no': ")
    if (goAgain == 'n'):
        runGame = False
        print("Caesar Cipher says: 0mmb6w2bioiqvcbowwlbvqop?\nHint: Add all the numbers in above message and use the result \nas the shift number to get the decrypted message of Caesar Cipher 😉")
        







