
# Importing library
import qrcode

# Data to be encoded
data = input("anter a link to build QRcode: ")

# Encoding data using make() function
img = qrcode.make(data)

save = input("select name to save QRcode: ")
# Saving as an image file
img.save(f'{save}.png')
print(f'link converted to QRcode and saved to {save}')
