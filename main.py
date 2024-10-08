import cv2
import easyocr
import matplotlib.pyplot as plt

#read image
img=cv2.imread("data/test3.png")
#instance text detector
reader=easyocr.Reader(["en"],gpu=False)
#detect text
text=reader.readtext(img)
threshold = 0.25
#draw bbod and text on image
for t in text:
    print(t)

    bbox,text,score=t
    if score > threshold:
        cv2.rectangle(img,bbox[0],bbox[2],(0,255,0),5)
        cv2.putText(img, text, bbox[0], cv2.FONT_HERSHEY_COMPLEX, 0.65, (255, 0, 0), 2)
# when working with plt we need to convert color from bgr to rgb first
plt.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))
plt.show()