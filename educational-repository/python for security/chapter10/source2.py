import re
def findCreditCard(raw):
    xyzco= re.findall("5[67][0-9]{10}",raw)
    if xyzco:
        print "[+] Found XYZ Credit Card: "+xyzco[0]
    else:
        print "failed"
        
def main():
    tests = []
    tests.append('this number 378585 is the luckiest one')
    tests.append('my card: 588282246310')
    tests.append('my second card: 578282246310')
    for test in tests:
        findCreditCard(test)
if __name__ == "__main__":
    main()


    
