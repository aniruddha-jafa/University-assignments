
1) Running the code

All code will be run in the __main__ function.
The key is obtained in __main__ from key.txt

Assume: we're opertaint gwith ASCII characters

:: Encryption
- Set initialisation_vector in the variable initialisation_vector given in  __main__

- Uncomment the following two lines of code:

    plaintext =  get_text_as_string_from_file("plaintext.txt")
    set_of_ciphertexts = des_encryption(plaintext, key, initialisation_vector)

- check ciphertext.txt for the ciphertext in 64 bit blocks, each block in a new line.


:: Decryption
- Comment the ablove two lines of code used fro encryption in  __main__
- Uncomment the following two lines of code:

    ciphertext_stream = get_text_as_string_from_file("ciphertext.txt")
    des_decryption(ciphertext_stream, key, initialisation_vector)

- the plaintext will appear in plaintext.txt


2) Clarifications on code

:: Representing bits in the program
- Each bit, based on ASCII to binary conversion, is represented as a character in a string.
e.g. a 64 char string (string of len 64) represents 64 bits.

:: Conversions from ASCII to binary, binary to Ascii, XORING
The following funtions were used to convert between different types and data representations:

- ord() and chr()  functions were used to move from  character to integer, integer to character respectively.
- bin() was used to convert decimal integers to binary string e.g. bin(3) = '0b11'
- zfill(a) pads the output string 0s from the left until the length is .
- XORING relied on conversion of binary strings to integers, using the inbuilt XOR in python ("a ^ b"), and converting back to binary.
e.g. bin(int(string1, 2) ^ int(string2, 2))[2:].zfill(length)


:: Padding used
PKCS5 padding, as suggested in the problemset.


:: ** Removing padding from the last cipherblock when decrypting ciphertext to plaintext
Used in function padded_plaintext_in_binary_to_ASCII_chars(). In the last 8 bytes of padded plaintext, if you encounter ANY byte whose int representation is =< 8,
substitute is with a space [ chr(32) ]. Not foolproof, but works for human-readable messages.

Relevant code:

    block_number = 0
    number_64_bit_blocks =  len(padded_plaintext_in_bytes)

    for byte in padded_plaintext_in_bytes: # set of bytes as all bytes of the padded plaintext
        byte_as_int = int(byte,2)

        if block_number <  (number_64_bit_blocks - 8) or byte_as_int > 8:
            plaintext_ASCII = plaintext_ASCII + chr(byte_as_int)

        else:                                     # take care of last few padding bytes (at most 8) in present in the last 64-bit block in plaintext, which are in decimal are ints from 1 to 8 in decimal
            plaintext_ASCII = plaintext_ASCII +  chr(32)      # chr(32) is a space; insert a space by default.
        block_number += 1


3) References and external code looked at

Ascii table: https://www.cs.cmu.edu/~pattis/15-1XX/common/handouts/ascii.html
XORing strings, xfill(): https://stackoverflow.com/questions/19414093/how-to-xor-binary-with-python


DES references:
https://academic.csuohio.edu/yuc/security/Chapter_06_Data_Encription_Standard.pdf
https://www.nku.edu/~christensen/DESschneier.pdf
https://en.wikipedia.org/wiki/Data_Encryption_Standard

AES references:
https://kavaliro.com/wp-content/uploads/2014/03/AES.pdf
http://www.moserware.com/2009/09/stick-figure-guide-to-advanced.html
https://en.wikipedia.org/wiki/Advanced_Encryption_Standard
