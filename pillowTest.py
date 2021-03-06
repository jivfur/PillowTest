#!/usr/bin/env python3
import sys
import os
import glob
from PIL import Image

"""
Rotate 90 degrees the images in the path.
Resize to 128,128
There are only images in the path
"""
def transformImages(path):
  #for im in glob.glob(os.path.join(path,"*")):
    #print(im)
  for im in os.listdir(path):
    img = Image.open(os.path.join(path,im)).convert('RGB')
    img = img.rotate(90)
    img = img.resize((128,128))
    img.save("/opt/icons/" + im, "JPEG")



def main():
  transformImages("./images/")

if __name__ == '__main__':
  main()
