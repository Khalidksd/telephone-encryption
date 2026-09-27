Telephone Encryption System With Python

About This Project:-

I created this project while learning Python and wanted to build something simple that would help me understand how encryption works.

The idea came from the old telephone keypad, where each number represents several letters. I used Python if, elif, and for loops to create a simple system that can encrypt and decrypt messages.

This is mainly a learning project. It is not meant to be used as secure encryption for private or sensitive information.
How the Telephone Keypad Works

The program uses the letters on a normal telephone keypad:

+-----+-----+-----+
|  1  |  2  |  3  |
|     | ABC | DEF |
+-----+-----+-----+
|  4  |  5  |  6  |
| GHI | JKL | MNO |
+-----+-----+-----+
|  7  |  8  |  9  |
| PQRS| TUV | WXYZ|
+-----+-----+-----+
|  *  |  0  |  #  |
+-----+-----+-----+

I used the number of times a key would normally be pressed to represent each letter.

For example:

A = 2
B = 22
C = 222

D = 3
E = 33
F = 333

The same idea continues through the alphabet.
Letter Codes

A = 2       B = 22      C = 222
D = 3       E = 33      F = 333
G = 4       H = 44      I = 444
J = 5       K = 55      L = 555
M = 6       N = 66      O = 666
P = 7       Q = 77      R = 777
S = 7777    T = 8       U = 88
V = 888     W = 9       X = 99
Y = 999     Z = 9999

I also added some basic punctuation:

Space = 0
. = 00
, = 000
? = 0000

How Encryption Works

When I enter a message, the program goes through it one character at a time.

For example, if I enter:

HELLO

the program looks at each letter:

H = 44
E = 33
L = 555
L = 555
O = 666

So the encrypted message becomes:

44-33-555-555-666

The - is used to separate each character so the program knows where one encrypted letter ends and the next one starts.
How Decryption Works

The program can also take the encrypted message and turn it back into normal text.

For example:

44-33-555-555-666

is separated into:

44
33
555
555
666

The program then checks each part using if and elif.

For example:

if part == "44":
    decrypted_message = decrypted_message + "H"

elif part == "33":
    decrypted_message = decrypted_message + "E"

The result is:

HELLO

Why I Used if / elif

I wanted this project to help me understand the basics of Python, so I intentionally used if and elif instead of making the program more complicated.

For example:

if letter == "A":
    encrypted_message = encrypted_message + "2"

elif letter == "B":
    encrypted_message = encrypted_message + "22"

elif letter == "C":
    encrypted_message = encrypted_message + "222"

This makes it easy for me to see exactly what the program is doing with each letter.
The for Loop

I also used a for loop to go through the message one character at a time.

For example:

for letter in message:

If the message is:

ABC

the loop processes:

A
B
C

one at a time.

Then the if and elif statements decide which number should be added.
Converting the Message to Uppercase

I used:

.upper()

so that lowercase and uppercase letters can be handled the same way.

For example:

message = input("Enter a message: ").upper()

If I enter:

hello

the program changes it to:

HELLO

before processing it.
Telephone Number Encryption

I also experimented with encrypting telephone numbers.

The program gives each digit its own code:

0 = 10
1 = 11
2 = 12
3 = 13
4 = 14
5 = 15
6 = 16
7 = 17
8 = 18
9 = 19

For example:

123

becomes:

111213

This is a separate part of the project from the letter encryption.
Running the Program

You need Python 3 to run the project.

First, check that Python is installed:

python3 --version

Then run the program:

python3 telephone_encryption_ifelif.py

The program will display the telephone keypad and ask me to choose an option.

Choose 1 to Encrypt or 2 to Decrypt:

Encryption Example

I can choose:

1

Then enter a message such as:

HELLO

The program converts the letters into their telephone keypad codes.

Example:

HELLO

becomes:

44-33-555-555-666

Decryption Example

I can choose:

2

Then enter:

44-33-555-555-666

The program converts it back to:

HELLO

What I Learned

While working on this project, I practiced several Python basics:

    Variables
    input()
    print()
    if
    elif
    else
    for loops
    Strings
    .upper()
    .split()
    String concatenation

The biggest thing I learned was how a program can take something I enter, process it one character at a time, and produce a different result.
Testing

I tested the alphabet using the telephone keypad codes.

ABCDEFGHIJKLMNOPQRSTUVWXYZ

The corresponding encrypted codes are:

2-22-222-3-33-333-4-44-444-5-55-555-6-66-666-7-77-777-7777-8-88-888-9-99-999-9999

I also tested spaces and punctuation such as:

.
,
?

What I Want to Improve

There are still things I can improve as I learn more Python.

Some ideas I have are:

    Make the program easier to use
    Add better error handling
    Add more supported characters
    Organize the code into functions
    Add more testing
    Improve the telephone number encryption
    Eventually learn how to use proper cryptography for real security

For now, I wanted to keep the project simple so I could understand the code instead of using complicated methods that I don't fully understand yet.
Important Note

This project is for learning Python and understanding basic encryption/encoding ideas.

The telephone keypad method is not secure encryption. Someone who knows the rules can easily convert the numbers back into letters.

I built this project to practice programming and understand how the different parts of Python work together.
