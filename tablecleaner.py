import cv2
import numpy as np
r=0
img=cv2.imread("/home/oyyh/cv/photo/TableCleaner1.png",-1)
img1=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.namedWindow('img')                                                        
def img_intensity_change(x):
    global r
    r=cv2.getTrackbarPos('r','img')     
cv2.imshow('img0',img1)
cv2.createTrackbar('r','img',0,255,img_intensity_change)
while(1):
    ret, binary = cv2.threshold(img1,r, 255, cv2.THRESH_BINARY_INV)
    cv2.imshow('img',binary)
    if cv2.waitKey(1)==27:
        break
def contours_demo(img):
    contours, hierarchy = cv2.findContours(img,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
    draw_img = img.copy() #复制，不改变原图
    res = cv2.drawContours(draw_img,contours,-1,(0,255,0),1)
    cv2.imshow("res",res)
#方法1
'''while(1):
    #print((b,g,r))
    ret0, binary0 = cv2.threshold(B, b, 255, cv2.THRESH_BINARY)
    ret1, binary1= cv2.threshold(G, b, 255, cv2.THRESH_BINARY)
    ret2, binary2 = cv2.threshold(R, r, 255, cv2.THRESH_BINARY)
    cv2.imshow("ret0",binary0)
    cv2.imshow("ret1",binary1)
    cv2.imshow("ret2",binary2)
    merged[:, :, 0] = binary0
    merged[:, :, 1] = binary1
    merged[:, :, 2] = binary2
    cv2.imshow('merged',merged)
    if cv2.waitKey(1)==27:
        break
'''
kernel=np.ones((5,5),np.uint8)
o=np.ones((5,5),np.uint8)
#erosion=cv2.erode(o,kernel,cv2.BORDER_DEFAULT,iterations=5)
k=cv2.morphologyEx(binary,cv2.MORPH_CLOSE,kernel,iterations=4)
k=cv2.dilate(k,o,cv2.BORDER_DEFAULT,iterations=1)
contours_demo(k)
#找
contours, hierarchy = cv2.findContours(k, \
                                cv2.RETR_EXTERNAL, \
                                cv2.CHAIN_APPROX_SIMPLE)
n=len(contours)
print(n)
draw_img1 = img.copy()#如果是视屏可以删去节省时间
#res = cv2.drawContours(draw_img1,contours,-1,(0,255,0),1)
#cv2.imshow("c",res)
for i in range(n):
    if cv2.contourArea(contours[i])>150:
        draw_img1 = cv2.drawContours(draw_img1,contours,i,(0,255,0),1)
        #cnt=contours[i]
        x,y,w,h=cv2.boundingRect(contours[i])
        #mask=np.zeros(draw_img1.shape,np.uint8)
        brcnt=np.array([[[x,y]],[[x+w,y]],[[x+w,y+h]],[[x,y+h]]])
        cv2.drawContours(draw_img1,[brcnt],-1,(255,0,0),1)
cv2.imshow("luominjie_SB",draw_img1)
cv2.waitKey()
cv2.destroyAllWindows()
