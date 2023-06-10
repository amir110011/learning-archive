import sys
SYMBOLS = 'abcdefghijklmnopqrstuvwxyz'
def main():
    myMessage = "a computer would deserve to be called intelligent if it could deceive a human into believing that it was human -alan Turing"
    keyA = 7
    keyB = 10
    if gcd(keyA,len(SYMBOLS)) != 1:
        sys.exit("Your key is not relatively prime")
        
    myMode = 'encrypt'
    if myMode == 'encrypt':
        translated = encryptMessage(keyA,keyB, myMessage)
    elif myMode == 'decrypt':
        translated = decryptMessage(keyA,keyB, myMessage)

    print translated

def encryptMessage(keyA,keyB, message):
    ciphertext = ''
    for symbol in message:
        if symbol in SYMBOLS:
            symIndex = SYMBOLS.find(symbol)
            ciphertext += SYMBOLS[(symIndex * keyA + keyB) % len(SYMBOLS)]
        else:
            ciphertext += symbol
    return ciphertext

def decryptMessage(keyA,keyB, message):
    plaintext = ''
    modInverseOfKeyA = findModInverse(keyA, len(SYMBOLS))
    for symbol in message:
        if symbol in SYMBOLS:
            symIndex = SYMBOLS.find(symbol)
            plaintext += SYMBOLS[(symIndex - keyB) * modInverseOfKeyA % len(SYMBOLS)]
        else:
            plaintext += symbol
    return plaintext


def gcd(a, b):
    while a != 0:
        a, b = b % a, a
    return b

def findModInverse(a, m):
    if gcd(a, m) != 1:
        return None # no mod inverse exists if a & m aren't relatively prime
    u1, u2, u3 = 1, 0, a
    v1, v2, v3 = 0, 1, m
    while v3 != 0:
        q = u3 // v3 
        v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3
    return u1 % m

if __name__ == '__main__':
    main()

    
            
        
