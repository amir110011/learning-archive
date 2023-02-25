import os
import _modEXIF

TS = 0
MAKE = 1
MODEL = 2

# define a directory to scan
scanDir = "C:\\pics\\"
try:
        picts = os.listdir(scanDir)
except:
        print "error invalid directory"
        exit(0)
for aFile in picts:
        targetFile = scanDir + aFile
        if os.path.isfile(targetFile):
                gpsDictionary, EXIFList = _modEXIF.ExtractGPSDictionary(targetFile)
                if (gpsDictionary):
                        # Obtain the Lat Lon values from the gpsDictionary
                        # Converted to degrees
                        # The return value is a dictionary key value pairs
                        dCoor = _modEXIF.ExtractLatLon(gpsDictionary)
                        lat = dCoor.get("Lat")
                        latRef = dCoor.get("LatRef")
                        lon = dCoor.get("Lon")
                        lonRef = dCoor.get("LonRef")
                        
                        if ( lat and lon and latRef and lonRef):
                                print targetFile + ":" + EXIFList[TS] + ":"  + EXIFList[MAKE]+ ":" +
                                EXIFList[MODEL]+ ":" +  str(lat)+','+str(lon)
                        else:
                                print "WARNING", "no GPS EXIF Data for "
                else:
                        print "no dictionary found in " + targetFile
        






