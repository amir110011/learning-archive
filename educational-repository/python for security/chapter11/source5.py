import math
def main():
    myMessage = 'ltrue ett shi e7t  eccsop'
    myKey = 8
    plaintext = decryptMessage(myKey, myMessage)
    print(plaintext)


def decryptMessage(key, message):
    numOfColumns = int(math.ceil(float(len(message)) / key))
    numOfRows = key
    numOfShadedBoxes = (numOfColumns * numOfRows) - len(message)
    plaintext = [''] * numOfColumns
    col = 0
    row = 0
    for symbol in message:
        plaintext[col] += symbol
        print plaintext
        col += 1
        if (col == numOfColumns) or (col == numOfColumns - 1 and row >= numOfRows - numOfShadedBoxes):
            col = 0
            row += 1
    return ''.join(plaintext)

if __name__ == '__main__':
    main()


