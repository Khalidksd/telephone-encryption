print("+-----+-----+-----+")
print("|  1  |  2  |  3  |")
print("|     | ABC | DEF |")
print("+-----+-----+-----|")
print("|  4  |  5  |  6  |")
print("| GHI | JKL | MNO |")
print("+-----+-----+-----+")
print("|  7  |  8  |  9  |")
print("| PQRS| TUV | WXYZ|")
print("+-----+-----+-----+")
print("|  *  |  0  |  #  |")
print("+-----+-----+-----+")

choice = input("Choose 1 to Encrypt or 2 to Decrypt:")
print("You chose:", choice)

if choice == "2":
    encrypted_input = input("Enter encrypted message: ")
    decrypted_message = ""
    parts = encrypted_input.split("-")

    for part in parts:
        if part == "2":
            decrypted_message = decrypted_message + "A"
        elif part == "22":
            decrypted_message = decrypted_message + "B"
        elif part == "222": 
            decrypted_message = decrypted_message + "C"
        elif part == "3": 
            decrypted_message = decrypted_message + "D"
        elif part == "33": 
            decrypted_message = decrypted_message + "E"
        elif part == "333": 
            decrypted_message = decrypted_message + "F"
        elif part == "4": 
            decrypted_message = decrypted_message + "G"
        elif part == "44": 
            decrypted_message = decrypted_message + "H"
        elif part == "444": 
            decrypted_message = decrypted_message + "I"
        elif part == "5": 
            decrypted_message = decrypted_message + "J"
        elif part == "55": 
            decrypted_message = decrypted_message + "K"
        elif part == "555": 
            decrypted_message = decrypted_message + "L"
        elif part == "6": 
            decrypted_message = decrypted_message + "M"
        elif part == "66": 
            decrypted_message = decrypted_message + "N"
        elif part == "666": 
            decrypted_message = decrypted_message + "O"
        elif part == "7": 
            decrypted_message = decrypted_message + "P"
        elif part == "77": 
            decrypted_message = decrypted_message + "Q"
        elif part == "777": 
            decrypted_message = decrypted_message + "R"
        elif part == "7777": 
            decrypted_message = decrypted_message + "S"
        elif part == "8": 
            decrypted_message = decrypted_message + "T"
        elif part == "88": 
            decrypted_message = decrypted_message + "U"
        elif part == "888": 
            decrypted_message = decrypted_message + "V"
        elif part == "9": 
            decrypted_message = decrypted_message + "W"
        elif part == "99": 
            decrypted_message = decrypted_message + "X"
        elif part == "999": 
            decrypted_message = decrypted_message + "Y"
        elif part == "9999": 
            decrypted_message = decrypted_message + "Z"
        elif part == "0": 
            decrypted_message = decrypted_message + " "
        elif part == "00": 
            decrypted_message = decrypted_message + "."
        elif part == "000": 
            decrypted_message = decrypted_message + ","
        elif part == "0000": 
            decrypted_message = decrypted_message + "?"
        
    print("Decrypted message:", decrypted_message)                                            
    if encrypted_input == "2":
        print("Decrypted:", "A")
    elif encrypted_input == "22":
        print("Decrypted:", "B")
    elif encrypted_input == "222":
        print("Decrypted:", "C")
    elif encrypted_input == "3":
        print("Decrypted:", "D")
    elif encrypted_input == "33":
        print("Decrypted:", "E")
    elif encrypted_input == "333":
        print("Decrypted:", "F")
    elif encrypted_input == "4":
        print("Decrypted:", "G")
    elif encrypted_input == "44":
        print("Decrypted:", "H")
    elif encrypted_input == "444":
        print("Decrypted:", "I")
    elif encrypted_input == "5":
        print("Decrypted:", "J")
    elif encrypted_input == "55":
        print("Decrypted:", "K")
    elif encrypted_input == "555":
        print("Decrypted:", "L")
    elif encrypted_input == "6":
        print("Decrypted:", "M")
    elif encrypted_input == "66":
        print("Decrypted:", "N")
    elif encrypted_input == "666":
        print("Decrypted:", "O")
    elif encrypted_input == "7":
        print("Decrypted:", "P")
    elif encrypted_input == "77":
        print("Decrypted:", "Q")
    elif encrypted_input == "777":
        print("Decrypted:", "R")
    elif encrypted_input == "7777":
        print("Decrypted:", "S")
    elif encrypted_input == "8":
        print("Decrypted:", "T")
    elif encrypted_input == "88":
        print("Decrypted:", "U")
    elif encrypted_input == "888":
        print("Decrypted:", "V")
    elif encrypted_input == "9":
        print("Decrypted:", "W")
    elif encrypted_input == "99":
        print("Decrypted:", "X")
    elif encrypted_input == "999":
        print("Decrypted:", "Y")
    elif encrypted_input == "9999":
        print("Decrypted:", "Z")

    exit()

if choice == "1":
    number = input("Enter a telephone number: ")

if choice == "1":
    message = input("Enter a message: ").upper()

if choice == "1":
    print("You entered:", number)

encrypted = ""
encrypted_message = ""

for digit in number:
    if digit == "7":
        encrypted = encrypted + "17"
    elif digit == "8":
        encrypted = encrypted + "18"
    elif digit == "9":
        encrypted = encrypted + "19"
    elif digit == "6":
        encrypted = encrypted + "16"
    elif digit == "5":
        encrypted = encrypted + "15"
    elif digit == "4":
        encrypted = encrypted + "14"
    elif digit == "3":
        encrypted = encrypted + "13"
    elif digit == "2":
        encrypted = encrypted + "12"
    elif digit == "1":
        encrypted = encrypted + "11"
    elif digit == "0":
        encrypted = encrypted + "10"
    else:
        encrypted = encrypted + digit

for letter in message:
    if letter == "A":
        encrypted_message = encrypted_message + "2"
    elif letter == "B":
        encrypted_message = encrypted_message + "22"
    elif letter == "C":
        encrypted_message = encrypted_message + "222"
    elif letter == "D":
        encrypted_message = encrypted_message + "3"
    elif letter == "E":
        encrypted_message = encrypted_message + "33"
    elif letter == "F":
        encrypted_message = encrypted_message + "333"
    elif letter == "G":
        encrypted_message = encrypted_message + "4"
    elif letter == "H":
         encrypted_message = encrypted_message + "44"
    elif letter == "I":
        encrypted_message = encrypted_message + "444"
    elif letter =="J":
        encrypted_message = encrypted_message + "5"
    elif letter == "K":
        encrypted_message = encrypted_message + "55"
    elif letter == "L":
        encrypted_message = encrypted_message + "555"
    elif letter == "M":
        encrypted_message = encrypted_message + "6"
    elif letter == "N":
        encrypted_message = encrypted_message + "66"
    elif letter == "O":
        encrypted_message = encrypted_message + "666"
    elif letter == "P":
        encrypted_message = encrypted_message + "7"
    elif letter == "Q":
        encrypted_message = encrypted_message + "77"
    elif letter == "R":
        encrypted_message = encrypted_message + "777"
    elif letter == "S":
        encrypted_message = encrypted_message + "7777"
    elif letter == "T":
        encrypted_message = encrypted_message + "8"
    elif letter == "U":
        encrypted_message = encrypted_message + "88"
    elif letter == "V":
        encrypted_message = encrypted_message + "888"
    elif letter == "W":
        encrypted_message = encrypted_message + "9"
    elif letter == "X":
        encrypted_message = encrypted_message + "99"
    elif letter == "Y":
        encrypted_message = encrypted_message + "999"
    elif letter == "Z":
        encrypted_message = encrypted_message + "9999"
    elif letter == " ":
        encrypted_message = encrypted_message + "0"
    elif letter == ".":
        encrypted_message = encrypted_message + "00"
    elif letter == ",":
        encrypted_message = encrypted_message + "000"
    elif letter == "?":
        encrypted_message = encrypted_message + "0000"
    else:
        print("Unsupported character:", letter)

print("Encrypted message:", encrypted_message)
print("Encrypted:", encrypted)
