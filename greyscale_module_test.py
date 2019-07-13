import cv2
import numpy as np
from sys import argv

def usage():
    print('python greyscale.py <filename> <height in px> <width in px> [og] for original or grey')
    print('eg: python greyscale.py image.jpg 32 32 g')
def main(filename, height, width, mode):
    # filename = 'image.jpg'
    if mode == 'g':
        img = cv2.imread(filename,cv2.IMREAD_GRAYSCALE)
    if mode == 'o':
        img = cv2.imread(filename)
    img = cv2.resize(img,(height,width),interpolation=cv2.INTER_CUBIC)
    cv2.imwrite('test.jpg', img)

    # cv2.imwrite('test.jpg', canvas)

if __name__ == "__main__":
    if len(argv) != 5:
        usage()
    else:
        main(argv[1], int(argv[2]), int(argv[3]), argv[4])