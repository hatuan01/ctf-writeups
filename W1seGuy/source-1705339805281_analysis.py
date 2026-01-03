import random
import socketserver 
import socket, os
import string

# This XOR encoded text has flag 1: 207e7c283845575d3d3c314e45123c000252382b3558436029187a483b1d064248633d064e7e2135
hex_encoded = "207e7c283845575d3d3c314e45123c000252382b3558436029187a483b1d064248633d064e7e2135"
decoded_text = bytes.fromhex(hex_encoded).decode()
# print(decoded_text)
# print(len(decoded_text))
# print(decoded_text.encode().hex())


first_letter = chr(ord(decoded_text[0]) ^ ord("T"))
second_letter = chr(ord(decoded_text[1]) ^ ord("H"))
third_letter = chr(ord(decoded_text[2]) ^ ord("M"))
fourth_letter = chr(ord(decoded_text[3]) ^ ord("{"))
last_letter = chr(ord(decoded_text[39]) ^ ord("}"))
key = first_letter + second_letter + third_letter + fourth_letter + last_letter
#print(key)

xored = ""
for i in range(0,len(decoded_text)):
    xored += chr(ord(decoded_text[i]) ^ ord(key[i%len(key)]))
print(xored)