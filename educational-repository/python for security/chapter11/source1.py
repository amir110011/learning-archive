#message = 'This text is encrypted by python.'
message = '.nohtyp yb detpyrcne si txet sihT'

translated = ''

i = len(message) - 1
while i >= 0:
    translated = translated + message[i]
    i = i - 1

print(translated)

