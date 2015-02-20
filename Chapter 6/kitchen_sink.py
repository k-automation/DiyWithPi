#/usr/bin/env python

import time
import sys
import cv2.cv as cv



def main(debug=False, fromCam=False):
    vessels = 0
    thresh = 200
    while True:
        if fromCam == True:
            im = cv.QueryFrame(capture)
        
        gray = cv.CreateImage(cv.GetSize(im),8,1)
        edges = cv.CreateImage(cv.GetSize(im),cv.IPL_DEPTH_8U,1)

        cv.CvtColor(im,gray,cv.CV_BGR2GRAY)

        cv.Canny(gray,edges,200,100,3)
        cv.Smooth(gray,gray,cv.CV_GAUSSIAN,3,3)

        storage = cv.CreateMat(640,1,cv.CV_32FC3)
        cv.HoughCircles(gray,storage,cv.CV_HOUGH_GRADIENT,1,30,100,55,0,0)

        for i in range(storage.rows ):
            val = storage[i, 0] 

            radius = int(val[2])
            center = (int(val[0]), int(val[1]))
            cv.Circle(im, center, radius, (0, 0, 255), 3, 8, 0)

            
        
        cv.NamedWindow('Image')
        cv.ShowImage('Image',im)
        if cv.WaitKey(5) == 27:
            cv.DestroyAllWindows()
            break
            


if __name__ == '__main__':
    capture = cv.CaptureFromCAM(0)
    main(fromCam = True)
