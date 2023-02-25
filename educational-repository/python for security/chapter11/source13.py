LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
def main():
    myMessage = """Alan Mathison Turing was a British mathematician,
logician, cryptanalyst, and computer scientist. He was highly influential in
the development of computer science, providing a formalisation of the concepts
of "algorithm" and "computation" with the Turing machine. Turing is widely
considered to be the father of computer science and artificial intelligence.
During World War II, Turing worked for the Government Code and Cypher School
(GCCS) at Bletchley Park, Britain's codebreaking centre. For a time he was head
of Hut 8, the section responsible for German naval cryptanalysis. He devised a
number of techniques for breaking German ciphers, including the method of the
bombe, an electromechanical machine that could find settings for the Enigma
machine."""
    myKey = 'BOOK'
    myMode = 'encrypt'
    translated = translateMessage(myKey, myMessage,myMode)
    print(translated)
    
def translateMessage(key, message, mode):
    translated = []
    keyIndex = 0
    key = key.upper()
    for symbol in message:
        num = LETTERS.find(symbol.upper())
        if num != -1:
            if mode == 'encrypt':
                num += LETTERS.find(key[keyIndex])
            elif mode == 'decrypt':
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

if __name__ == '__main__':
    main()
        
