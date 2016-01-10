import os,sys
from PIL import Image
scaleFactorX = 10 
scaleFactorY = 20 #x by y pixels -> one char
#charSet = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
charSet = " .:-=+*#%@"[::-1] #want darker-> lighter
path= 'picture.jpg'

def readImage(path):
    img = Image.open(path).convert('L')
    #img.save('grayscale.png')
    return img    

def convert(img, charSet):
    ans = [""]
    for row in range(0,img.height-img.height%scaleFactorY,scaleFactorY):
        for col in range(0,img.width-img.width%scaleFactorX,scaleFactorX):
            acc = 0            
            for col1 in range(col,col+scaleFactorX):
                for row1 in range(row,row+scaleFactorY):
                    acc+=img.getpixel((col1,row1))
            ans[row/scaleFactorY]+=mapStr(acc/float(scaleFactorX*scaleFactorY), charSet)
        ans.append("")
    return ans

def mapStr(gray, charSet):#higher number means lighter
    if gray==255.0:
        return charSet[len(charSet)-1]
    else:
        return charSet[int(gray/(255.0/len(charSet)))]

print "\n".join(convert(readImage(path), charSet))
