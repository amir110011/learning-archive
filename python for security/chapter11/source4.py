
def main():
    myMessage = 'lets test the core i7 cpu'
    myKey = 8
    ciphertext = encryptMessage(myKey, myMessage)
    print(ciphertext + '|')

def encryptMessage(key, message):
    ciphertext = [''] * key
    print ciphertext
    for col in range(key):
        pointer = col
        while pointer < len(message):
            ciphertext[col] += message[pointer]
            pointer += key
        print ciphertext
    return ''.join(ciphertext)

if __name__ == '__main__':
    main()

