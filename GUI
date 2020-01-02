import cv2
import numpy as np
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap, QImage

#GUI Setup
app = QApplication([])
window = QMainWindow()
label = QLabel()
#liveImage = QImage(r'C:\Users\kriso\feed.jpg')

#label.setPixmap(liveImage)
#window.setCentralWidget(label)

window.show()

#name of file to be written/read
fileName = r"C:\Users\kriso\feed.jpg"

#camera object
cam = cv2.VideoCapture(0)

#capture image and display rapidly
while True:
    #two variables (original image)
    ret, img = cam.read()
        
    #-convert opencvimage to qimage-------------------------------------
    height, width, channel = img.shape
    bytesPerLine = 3 * width
    qImg = QImage(img.data, width, height, bytesPerLine, QImage.Format_RGB888).rgbSwapped()
    #--------------------------------------
    
    if ret:
        #read image from img filepath
        #live = cv2.imread(r'C:\Users\kriso\feed.jpg')
        
        #show newly read image 
        ####cv2.imshow('Window',img)
        
        ###############################
        
        #fill label with newly read image
        label.setPixmap(QPixmap(qImg))
        #set newly read image as central widget
        window.setCentralWidget(label)
        
    #if boolean false
    else:
        print("Camera not working")
        break
        
    #wait one mS for a key stroke
    key = cv2.waitKey(1)&0xFF
    
#    if key==ord('q'):           #ord ASCII 
#        break
        
cv2.destroyAllWindows()
cam.release()
app.exit(app.exec_())
