import sys
import os
import urllib2
from operator import methodcaller



from Crypto.Hash import SHA256


#--------------------------------------------------------------
# padding oracle
#--------------------------------------------------------------
class PaddingOracle(object):
    def __init__(self):
        self.targetURL = 'http://crypto-class.appspot.com/po?er='

    def query(self, q):
        target = self.targetURL + urllib2.quote(q)    # Create query URL
        req = urllib2.Request(target)         # Send HTTP request to server
        try:
            f = urllib2.urlopen(req)          # Wait for response
        except urllib2.HTTPError, e:          
            return e.code == 404

#--------------------------------------------------------------
# Smart Char Guesser
#--------------------------------------------------------------
class CharGuesser(object):
    def __init__(self):
        self.letterFrequencyOrder = ['e', 't', 'a', 'o', 'i', 'n', 's', 'h', 'r', 'd', 'l', 'c', 'u', 'm', 'w', 'f', 'g', 'y', 'p', 'b', 'v', 'k', 'j', 'x', 'q', 'z']
        self.firstLetterFrequencyOrder = ['T', 'A', 'S', 'H', 'W', 'I', 'O', 'B', 'M', 'F', 'C', 'L', 'D', 'P', 'N', 'E', 'G', 'R', 'Y', 'U', 'V', 'J', 'K', 'Q', 'Z', 'X']
        self.otherCharsOrder = [' ','0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.', ',', '!', '?', '&']
        self.commonBigramsOrder = ['th', 'en', 'ng', 'he', 'ed', 'of', 'in', 'to', 'al', 'er', 'it', 'de', 'an', 'ou', 'se', 're', 'ea', 'le', 'nd', 'hi', 'sa', 'at', 'is', 'si', 'on', 'or', 'ar', 'nt', 'ti', 've', 'ha', 'as', 'ra', 'es', 'te', 'ld', 'st', 'et', 'ur']
        self.charsUsed = []


    def guessPrecedingChar(self, currentChar=None):
        if(currentChar):
            for bigram in self.commonBigramsOrder:
                if bigram[1] == currentChar.lower():
                    if not self.checkUsed(bigram[0]):
                        return self.setUsed(bigram[0])
                    if not self.checkUsed(bigram[0].upper()):
                        return self.setUsed(bigram[0].upper())

        for char in self.letterFrequencyOrder:
            if not self.checkUsed(char):
                return self.setUsed(char)

        for char in self.firstLetterFrequencyOrder:
            if not self.checkUsed(char):
                return self.setUsed(char)

        for char in self.otherCharsOrder:
            if not self.checkUsed(char):
                return self.setUsed(char)
                
        for char in map(lambda x: chr(x), range(0,256)):
            if not self.checkUsed(char):
                return self.setUsed(char)   
        
        return None

    def checkUsed(self,char):
        return char in self.charsUsed

    def setUsed(self,char):
        self.charsUsed.append(char)
        return char

def splitCount(s, count):
     return [''.join(x) for x in zip(*[list(s[z::count]) for z in range(count)])]

def buildCryptoString(cryptoText, position, newBlock):
    return cryptoText[position]


if __name__ == "__main__": 

    cryptoText = "f20bdba6ff29eed7b046d1df9fb7000058b1ffb4210a580f748b4ac714c001bd4a61044426fb515dad3f21f18aa577c0bdf302936266926ff37dbf7035d5eeb1".decode('hex')
    blockSize = 16 
    cryptoBlocks  = splitCount(cryptoText, blockSize) 
    messageBlocks = splitCount(("00" * blockSize * (len(cryptoBlocks)-1)).decode('hex'),  blockSize) 
    lastChar = None



    po = PaddingOracle()

    for blockNum in reversed(range(0,len(cryptoBlocks))):
        for position in reversed(range(0, blockSize)):
            paddingNum = blockSize - position
            cryptoSourceBlock = cryptoBlocks[blockNum]
            
            for pl in range(1, paddingNum): 
                plPos = position + pl
                messageValue = messageBlocks[blockNum][plPos]
                cryptoSourceBlock[plPos] ^= messageValue ^ paddingNum

            charGuesser = CharGuesser()

            counter = 0
            while counter < 10:
                cryptoSourceBlock_bak = cryptoSourceBlock
                guess = charGuesser.guessPrecedingChar(lastChar)

                if(guess == None):
                    print "Nothing found"
                    break;

                print guess
                print paddingNum
                print cryptoSourceBlock.encode('hex')

                cryptoSourceBlock[position] ^= ord(guess) ^ paddingNum
                cryptoGuess = buildCryptoString(cryptoText, (blockNum * blockSize), cryptoSourceBlock)
                if(po.query(cryptoGuess)):
                    print "found char ", guess
                    messageBlocks[blockNum][position] = guess
                    break;

                counter += 1
