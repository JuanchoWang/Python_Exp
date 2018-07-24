# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 10:14:47 2017

@author: huz4hi
"""

import cv2
import os
import glob
import numpy as np
from Tkinter import *
import tkSimpleDialog

# directory for saving
path1 = '/mnt/Projects/CV-008_Students/wan4hi/Internal_Dataset/AEON_CheckIn/CheckIn_tenSec'
path2 = '/mnt/Projects/CV-008_Students/wan4hi/Internal_Dataset/AEON_CheckIn/CheckIn_tenSec/cropped/'

## read h264 video
#cap = cv2.VideoCapture('C:/Users/huz4hi/.spyder/Simpsons.h264')
#while(cap.isOpened()):
#    # frame number
#    print cap.get(1)
#    # read every frame
#    ret, frame = cap.read()
#    # save one of every 50 frames
#    if (cap.get(1) % 50) == 0:
#        cv2.imwrite(os.path.join(path1, 'f'+str(cap.get(1))+'.png'), frame)
#    # no more frame is captured or press q on keyboard, quit the playback
#    if (ret == False) or (cv2.waitKey(1) & 0xFF == ord('q')):
#        break
#    # show every frame
#    cv2.imshow('frame',frame)
## release object
#cap.release()
## clear all windows
#cv2.destroyAllWindows()

boxes = []
def on_mouse(event, x, y, flags, params):
    # global rot, path
    # record top left point when left button down
    if event == cv2.EVENT_LBUTTONDOWN:
        print 'Start Mouse Position: '+str(x)+', '+str(y)
        boxes.append([x, y])
    # record bottom right point when left button up
    elif event == cv2.EVENT_LBUTTONUP:
        print 'End Mouse Position: '+str(x)+', '+str(y)
        boxes.append([x, y])
        print boxes
        # crop image
        crop = rot[boxes[-2][1]:boxes[-1][1],boxes[-2][0]:boxes[-1][0]]
        cv2.imshow('crop',crop)
        # save cropped image when press w
        if cv2.waitKey(0) & 0xFF == ord('w'):
            # input Person ID and #point of view
            root = Tk()
            w = Label(root, text='Id & View')
            w.pack()
            name = tkSimpleDialog.askstring('Person Id', 'Id (2 digits)')
            view = tkSimpleDialog.askstring('Points of View', 'View (2 digits)')
            root.destroy()
            print 'Written to file'
            # name format 000031_00000005_0001.png => Person id 31, View 5, Camera 1
            cv2.imwrite(os.path.join(path2, '0000'+name+'_000000'+view+'_0001.png'), crop)

def rotate_bound(image, angle):
    # dimension of image
    (h, w) = image.shape[:2]
    # rotation center
    (cX, cY) = (w//2, h//2)
    # rotation matrix
    M = cv2.getRotationMatrix2D((cX, cY), -angle, 1.0)
    # sine and cosine of rotation
    cos = np.abs(M[0, 0])
    sin = np.abs(M[0, 1])
    # new bounding dimensions of rotated image
    nW = int((h * sin) + (w * cos))
    nH = int((h * cos) + (w * sin))
    # adjust rotation matrix considering translation
    M[0, 2] += (nW / 2) - cX
    M[1, 2] += (nH / 2) - cY
    return cv2.warpAffine(image, M, (nW, nH))

# read and resize images
for filename in glob.glob(os.path.join(path1, '*.jpg')):
    # read
    ori_im = cv2.imread(filename)
    im = cv2.resize(ori_im, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_CUBIC)
    cv2.imshow('original', im)
    # resize

    imS = im
    #imS = cv2.resize(im, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_CUBIC)
    cv2.imshow('resized', imS)

    # rotate image
    angle = 0
    rot = rotate_bound(imS, angle)
    # clockwise rotation
    while (cv2.waitKey(0) & 0xFF == ord('r')):
        angle += 5
        rot = rotate_bound(imS, angle)
        cv2.imshow('resized', rot)
    # anti-clockwise rotation
    while (cv2.waitKey(0) & 0xFF == ord('e')):
        angle -= 5
        rot = rotate_bound(imS, angle)
        cv2.imshow('resized', rot)
    # crop on resized image
    cv2.setMouseCallback('resized', on_mouse)
    # display the image infinitely long until any keypress, if press q, quit
    if cv2.waitKey(0) & 0xFF == ord('q'):
        break
    
# clear all windows    
cv2.destroyAllWindows()
