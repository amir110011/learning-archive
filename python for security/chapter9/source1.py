from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS

pilImage =Image.open("c:\\image1.jpeg")
EXIFData=pilImage._getexif()
catEXIF = EXIFData.items()
catEXIF.sort()
print catEXIF
