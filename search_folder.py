import os
from main import *
import cv2
path = "/Users/CJ/Desktop/data/"
i = 0

MAX = 100

while True:
    dirs = os.listdir( path )
    for file in dirs:
        image_path = path + "file" + str( i ) +".jpg"
        if file == "file" + str( i ) +".jpg":
            if i > (MAX - 1):
                j = i - MAX
                os.remove( path + "file" + str( j ) + ".jpg" )
            i += 1
            while cv2.imread(image_path) is None:
              g=0
            main(image_path)


