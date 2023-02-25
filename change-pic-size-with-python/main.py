from PIL import Image

img = Image.open('1.jpg')
# img.show()
print(f'image format: {img.format}')
print(f'image mod: {img.mode}')
print(f'image size: {img.size}')
# print(img.palette)

# img.save('resized/new.png')

width = int(input('enter the width: '))
length = int(input('enter the length: '))
new_img = img.resize((width, length))
# If you want to resize images and keep their aspect ratios
# img.thumbnail((400, 400))
new_img.save(f'resized/{width} in {length}.jpg')

"""
#for create logo in your pic
image = Image.open('demo_image.jpg')
logo = Image.open('logo.png')
image_copy = image.copy()
position = ((image_copy.width - logo.width), (image_copy.height - logo.height))
image_copy.paste(logo, position)
image_copy.save('pasted_image.jpg')
"""
