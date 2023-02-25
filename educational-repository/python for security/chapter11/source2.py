message = 'This text wont be readable.'
key = 4
mode = 'encrypt'   # it can be changed to decrypt / encrypt
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

print translate

