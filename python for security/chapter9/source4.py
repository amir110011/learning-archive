import hashlib 
import time 
import itertools # Creating controled combinations
lowerCase = ['a','b','c','d','e','f','g','h']
upperCase = ['G','H','I','J','K','L']
numbers = ['0','1','2','3']
special = ['!','@','#','$']
# combine and create a final list
allCharacters = []
allCharacters = lowerCase + upperCase + numbers + special
DIR ='C:\\aa\\'
# salt value
SALT ="&45Bvx9"
PW_LOW = 2
PW_HIGH = 6
startTime = time.time()
pwList = []
for r in range(PW_LOW, PW_HIGH):
        for s in itertools.product(allCharacters, repeat=r):
                pwList.append(''.join(s))
try:
        # Open the output file to save generated password
        fp = open(DIR+'all','w')
        for pw in pwList:
                md5Hash = hashlib.md5()
                md5Hash.update(SALT+pw)
                md5Digest = md5Hash.hexdigest()
                # Write the hash, password pair to the file
                fp.write(md5Digest +':'+ pw +'\n')
                del md5Hash
except:
        print'File Processing Error'
fp.close()

pwDict = {}
try:
        fp = open(DIR+'all','r')
        for line in fp:
                pairs = line.split(":")
                pwDict.update({pairs[0] : pairs[1]})
        fp.close()
except Exception, e:
        print'File Handling Error' , str(e)
        fp.close()
        
elapsedTime = time.time() - startTime
print'Elapsed Time:', elapsedTime
print'Passwords Generated:', len(pwDict)
print
cnt = 0
for key,value in (pwDict.items()):
        print key, value
        cnt += 1
        if cnt > 10:
                break;
print
# Demonstrate the use of the Dictionary to Lookup a password using a
# Lookup a Hash Value
pw = pwDict.get('c6f1d6b1d33bcc787c2385c19c29c208')
print'Hash Value Tested = c6f1d6b1d33bcc787c2385c19c29c208'
print'Associated Password='+ pw


