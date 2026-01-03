import random
import socketserver 
import socket, os
import string

flag = open('flag.txt','r').read().strip()

def send_message(server, message):
    enc = message.encode()
    server.send(enc)

def setup(server, key):
    # flag = 'THM{thisisafakeflag}' 
    # A => 36
    flag = 'A' 
    xored = ""

    for i in range(0,len(flag)):
        xored += chr(ord(flag[i]) ^ ord(key[i%len(key)]))

    hex_encoded = xored.encode().hex()
    return hex_encoded

def decode_setup(hex_encoded):
    original_str = bytes.fromhex(hex_encoded).decode()

    return original_str
    
def start(server):
    # key = random 5 characters
    res = ''.join(random.choices(string.ascii_letters + string.digits, k=5))
    key = str(res)

    hex_encoded = setup(server, key)
    send_message(server, "This XOR encoded text has flag 1: " + hex_encoded + "\n")
    
    send_message(server,"What is the encryption key? ")
    key_answer = server.recv(4096).decode().strip()

    try:
        send_message(server, key_answer + "\n")
        send_message(server, key + "\n")
        send_message(server, decode_setup(hex_encoded) + "\n")

        # key_answer & key have the same length
        if key_answer == key:
            send_message(server, "Congrats! That is the correct key! Here is flag 2: " + flag + "\n")
            server.close()
        else:
            send_message(server, 'Close but no cigar' + "\n")
            server.close()
    except:
        send_message(server, "Something went wrong. Please try again. :)\n")
        server.close()

class RequestHandler(socketserver.BaseRequestHandler):
    def handle(self):
        start(self.request)

if __name__ == '__main__':
    socketserver.ThreadingTCPServer.allow_reuse_address = True
    #server = socketserver.ThreadingTCPServer(('10.64.157.228', 1337), RequestHandler)
    server = socketserver.ThreadingTCPServer(('127.0.0.1', 1337), RequestHandler)
    server.serve_forever()

# This XOR encoded text has flag 1: 3721271f460b00190d41020f0b0f5705050b034f
# What is the encryption key? THM{thisisafakeflag}
# Close but no cigar

# This XOR encoded text has flag 1: 1c181a3e4379313b2b470d282304473c64342e50093e257652241c2e2d663a242e75463a2818374e