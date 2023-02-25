LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
UPPERLETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
LETTERS_AND_SPACE = UPPERLETTERS + UPPERLETTERS.lower() + ' \t\n'
def main():
    ciphertext = """Bzox Nohrjgcx Uifsou kkt o Pbjhwci aodisakuwqsbb,
zyhwqsbb, qbzdhkoozith, oxe qcwqihos gqsfbhsth. Vo xog rjuvvz wbpmisxuwov jb
hrf rsffzcznsbd pt qyndidff gmjsbmf, dfywwrsou o ppfakmwgkuwcx pt hrf qcxdsddt
ct "kmucbjhvw" bbr "mpadeuohspb" ksuv hrf Hibjbu wbqvsos. Heswbq jg kseszi
dcbcjrsbfr hy cs hrf todisf yg qcwqihos gqsfbqo bbr kshwpjqwkm wbdfzzshsbmf.
Ribjbu Gpfzn Xof SJ, Hibjbu gpfyoe tcb uvs Qpjsboasxu Qcnf obn Dmdrff Gmiccv
(HQQC) bh Pvfhqrmsm Zbfy, Lswhkjb'g mprslssoujbu mfbhbf. Tcb b hwwf vs gbg vobr
cp Iih 8, dis godhwyo fscqcbcjpzo gcf Qffako bofbz qbzdhkoozitwg. Rf rsfjgsn b
biwcsf yg hsmibwavsg ppf pbfoysou Uosaox dwdrffg, soqzeewbq uvs wfhvye ct dis
pynps, ko szodhfynsqrbbwmbz akdvwxf hvku qcemr tsor gouhwxhg tys hvo Fbwqno
akdvwxf."""
    hackedMessage = hackVigenere(ciphertext)
    if hackedMessage == None:
        print "couldn't find the key"

def hackVigenere(ciphertext):
    fo = open('dictionary.txt')
    words = fo.readlines()
    fo.close()
    for word in words:
        word = word.strip()
        decryptedText = decryptMessage(word, ciphertext)
        if isEnglish(decryptedText, wordPercentage=40):
            print('Key ' + str(word) + ': ' + decryptedText)
            return decryptedText
            

def decryptMessage(key, message):
    translated = []
    keyIndex = 0
    key = key.upper()
    for symbol in message:
        num = LETTERS.find(symbol.upper())
        if num != -1:
                num -= LETTERS.find(key[keyIndex])
                num %= len(LETTERS)
                if symbol.isupper():
                    translated.append(LETTERS[num])
                elif symbol.islower():
                    translated.append(LETTERS[num].lower())
                keyIndex += 1
                if keyIndex == len(key):
                    keyIndex = 0
        else:
            translated.append(symbol)
    return ''.join(translated)



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
        
