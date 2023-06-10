import sys
SYMBOLS = 'abcdefghijklmnopqrstuvwxyz'
SILENT_MODE = False
def main():
    myMessage = "k yeqlunmz ieujf fmgmzbm ne rm ykjjmf oxnmjjoamxn ot on yeujf fmymobm k huqkx oxne rmjomboxa nhkn on ikg huqkx -kjkx Tuzoxa"
    
    
        
    translated = hackAffine(myMessage)

    print translated

def hackAffine(message):
    for key in range(len(SYMBOLS) ** 2):
        if gcd(key, len(SYMBOLS)) != 1:
            continue
        print key
        for keyB in range(1,50):
            decryptedText = decryptMessage(key,keyB, message)
            
            if isEnglish(decryptedText):
                print('Tried Key %s... (%s)' % (key, decryptedText[:40]))
                print('Key: %s  keyB: %s' % (key,keyB) )
                return decryptedText
        if not SILENT_MODE:
                print('Tried Key %s... (%s)' % (key, decryptedText[:40]))
    return None


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


UPPERLETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
LETTERS_AND_SPACE = UPPERLETTERS + UPPERLETTERS.lower() + ' \t\n'


def loadDictionary():
    dictionaryFile = open('dictionary.txt')
    englishWords = {}
    for word in dictionaryFile.read().split('\n'):
        englishWords[word] = None
    dictionaryFile.close()
    return englishWords

ENGLISH_WORDS = loadDictionary()

def getEnglishCount(message):
    message = message.upper()
    message = removeNonLetters(message)
    possibleWords = message.split()
    if possibleWords == []:
        return 0.0
    matches = 0
    for word in possibleWords:
        if word in ENGLISH_WORDS:
            matches += 1
    return float(matches) / len(possibleWords)

def removeNonLetters(message):
    lettersOnly = []
    for symbol in message:
        if symbol in LETTERS_AND_SPACE:
            lettersOnly.append(symbol)
    return ''.join(lettersOnly)

def isEnglish(message, wordPercentage=20, letterPercentage=85):
    wordsMatch = getEnglishCount(message) * 100 >= wordPercentage
    numLetters = len(removeNonLetters(message))
    messageLettersPercentage = float(numLetters) / len(message) * 100
    lettersMatch = messageLettersPercentage >= letterPercentage
    return wordsMatch and lettersMatch

if __name__ == '__main__':
    main()
