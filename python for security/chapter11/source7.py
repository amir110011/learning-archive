import math,time, os, sys

def main():
    inputFilename = '1.txt'
    outputFilename = '2.encrypted.txt'
    myMode = 'decrypt'
    myKey = 10
    myKey2 = 3
    if not os.path.exists(inputFilename):
        print('The file %s does not exist...' % (inputFilename))
        sys.exit()
    fileObj = open(inputFilename)
    content = fileObj.read()
    fileObj.close()
    print('%sing...' % (myMode.title()))
    startTime = time.time()
    if myMode == 'encrypt':
        txt = substitute(myKey2,content,myMode)
        translated = encryptMessage(myKey, txt)
    elif myMode == 'decrypt':
        txt = substitute(myKey2,content,myMode)
        translated = decryptMessage(myKey, txt)
    totalTime = round(time.time() - startTime, 2)
    print('%sion time: %s seconds' % (myMode.title(), totalTime))

    outputFileObj = open(outputFilename, 'w')
    outputFileObj.write(translated)
    outputFileObj.close()

    print('Done %sing %s (%s characters).' % (myMode, inputFilename,len(content)))


def decryptMessage(key, message):
    numOfColumns = int(math.ceil(float(len(message)) / key))
    numOfRows = key
    numOfShadedBoxes = (numOfColumns * numOfRows) - len(message)
    plaintext = [''] * numOfColumns
    col = 0
    row = 0
    for symbol in message:
        plaintext[col] += symbol
        #print plaintext
        col += 1
        if (col == numOfColumns) or (col == numOfColumns - 1 and row >= numOfRows - numOfShadedBoxes):
            col = 0
            row += 1
    return ''.join(plaintext)

def encryptMessage(key, message):
    ciphertext = [''] * key
    print ciphertext
    for col in range(key):
        pointer = col
        while pointer < len(message):
            ciphertext[col] += message[pointer]
            pointer += key
    return ''.join(ciphertext)

def substitute(key,message,mode):
    LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    translate = ''
    message = message.upper()
    for symbol in message:
        if symbol in LETTERS:
            num = LETTERS.find(symbol)
            if mode == 'encrypt':
                num = num +key
            elif mode == 'decrypt':
                num = num - key
            if num >= len(LETTERS):
                num = num - len(LETTERS)
            elif num < 0:
                num = num + len(LETTERS)

            translate = translate + LETTERS[num]
        else:
            translate = translate + symbol

    return translate

if __name__ == '__main__':
    main()


